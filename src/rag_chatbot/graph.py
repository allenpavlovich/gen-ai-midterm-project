"""
LangGraph Workflow for the RAG Chatbot.

This module implements the workflow graph for the RAG chatbot using LangGraph.
"""

from typing import Dict, List, Any, TypedDict, Annotated, Literal, cast, Optional, Union, Tuple
from langgraph.graph import StateGraph
# Remove checkpoint manager import completely
from .agents import SupervisorAgent, ReasonerAgent, SummarizerAgent, AgentAction
from .retriever import ChromaDBRetriever

# Define state type
class ChatbotState(TypedDict):
    """Type definition for the chatbot state."""
    messages: List[Dict[str, Any]]  # Chat messages
    query: str  # Current user query
    retrieved_docs: List[Dict[str, Any]]  # Retrieved documents
    current_answer: Optional[str]  # Current generated answer
    action: Optional[AgentAction]  # Next action to take
    error: Optional[str]  # Error message, if any


class RAGChatbotGraph:
    """
    Implements the LangGraph workflow for the RAG chatbot.
    """
    
    def __init__(self, model="gpt-4o", debug=False):
        """
        Initialize the RAG chatbot graph.
        
        Args:
            model (str): The OpenAI model to use for agents.
            debug (bool): Whether to print debug information.
        """
        # Initialize agents
        self.supervisor = SupervisorAgent(model=model)
        self.reasoner = ReasonerAgent(model=model)
        self.summarizer = SummarizerAgent(model=model)
        
        # Initialize retriever
        self.retriever = ChromaDBRetriever()
        self.retriever_initialized = False
        
        # Debug flag
        self.debug = debug
        
        # Create graph
        self.graph = self._build_graph()
    
    def _build_graph(self) -> StateGraph:
        """
        Build the LangGraph workflow.
        
        Returns:
            StateGraph: The workflow graph
        """
        # Create a simple StateGraph without checkpoint manager
        graph = StateGraph(ChatbotState)
        
        # Define graph nodes
        
        # 1. Supervisor node - decides the next action
        def supervisor_node(state: ChatbotState) -> ChatbotState:
            """Process the user query with the supervisor agent."""
            # Extract the last message as the query if not already set
            if not state.get("query"):
                messages = state.get("messages", [])
                if messages and messages[-1]["role"] == "user":
                    state["query"] = messages[-1]["content"]
                else:
                    state["query"] = ""
            
            # Run the supervisor agent
            result = self.supervisor.run(
                query=state["query"],
                chat_history=state.get("messages", [])[:-1],  # Exclude current query
                retrieved_docs=state.get("retrieved_docs", []),
                current_answer=state.get("current_answer", "")
            )
            
            # Update the state with the supervisor's decision
            state["action"] = result["action"]
            
            # Ensure all state fields are properly initialized
            if "current_answer" not in state:
                state["current_answer"] = ""
            if "error" not in state:
                state["error"] = ""
                
            return state
        
        # 2. Retriever node - gets documents from ChromaDB
        def retrieve_node(state: ChatbotState) -> ChatbotState:
            """Retrieve relevant documents from ChromaDB."""
            # Initialize the retriever if not already initialized
            if not self.retriever_initialized:
                success = self.retriever.initialize()
                if not success:
                    state["error"] = "Failed to initialize ChromaDB retriever."
                    state["action"] = "GENERATE"  # Continue without documents
                    return state
                self.retriever_initialized = True
            
            # Retrieve documents - increased to 30 for GPT-4-turbo's larger context window
            query = state["query"]
            documents = self.retriever.retrieve_documents(query, top_k=5)
            
            # Handle empty results
            if not documents:
                # Create a special document that indicates no results were found
                # This ensures the reasoner knows there are no documents
                state["retrieved_docs"] = [{
                    "id": "no_results",
                    "content": "NO RELEVANT DOCUMENTS FOUND. You must explicitly state that you don't have the information to answer this question and DO NOT fabricate a response based on general knowledge.",
                    "metadata": {"source": "system", "title": "No Results Notice"}
                }]
                state["error"] = "No relevant documents found."
            else:
                state["retrieved_docs"] = documents
                state["error"] = ""
            
            # Always go to generate after retrieving
            state["action"] = "GENERATE"
            
            return state
        
        # 3. Generate node - creates an answer using the reasoner agent
        def generate_node(state: ChatbotState) -> ChatbotState:
            """Generate an answer with the reasoner agent."""
            query = state["query"]
            retrieved_docs = state.get("retrieved_docs", [])
            
            # Add error context if there was one
            if state.get("error"):
                retrieved_docs.append({
                    "content": f"Note: {state['error']} This answer is based on general knowledge.",
                    "metadata": {}
                })
            
            # Generate the answer
            answer = self.reasoner.run(
                query=query,
                retrieved_docs=retrieved_docs,
                chat_history=state.get("messages", [])[:-1]  # Exclude current query
            )
            
            # Update the state
            state["current_answer"] = answer
            
            # Check if the answer is too long and needs summarization
            if len(answer) > 1500:  # Threshold for summarization
                state["action"] = "SUMMARIZE"
            else:
                state["action"] = "DONE"
            
            return state
        
        # 4. Summarize node - condenses lengthy answers
        def summarize_node(state: ChatbotState) -> ChatbotState:
            """Summarize a lengthy answer with the summarizer agent."""
            query = state["query"]
            current_answer = state["current_answer"]
            
            # Summarize the answer
            summarized_answer = self.summarizer.run(
                answer=current_answer,
                query=query
            )
            
            # Update the state
            state["current_answer"] = summarized_answer
            state["action"] = "DONE"
            
            return state
        
        # 5. Done node - formats and returns the final answer
        def done_node(state: ChatbotState) -> ChatbotState:
            """Format the final answer and add it to the messages."""
            answer = state["current_answer"]
            messages = state.get("messages", [])
            
            # Add the assistant's answer to the messages
            messages.append({
                "role": "assistant",
                "content": answer
            })
            
            # Update the state
            state["messages"] = messages
            
            # Clear temporary state fields
            state.pop("query", None)
            state.pop("retrieved_docs", None)
            state.pop("current_answer", None)
            state.pop("action", None)
            state.pop("error", None)
            
            return state
        
        # Add nodes to the graph
        graph.add_node("supervisor", supervisor_node)
        graph.add_node("retrieve", retrieve_node)
        graph.add_node("generate", generate_node)
        graph.add_node("summarize", summarize_node)
        graph.add_node("done", done_node)
        
        # Define conditional edges using current LangGraph API
        # Define a router function to handle the decision logic
        def router(state: ChatbotState) -> str:
            """Route to the next node based on the action field."""
            return state["action"]
        
        # Connect nodes through the router function based on action state
        # 1. Supervisor node routing
        graph.add_conditional_edges(
            "supervisor",
            router,
            {
                "RETRIEVE": "retrieve",
                "GENERATE": "generate",
                "SUMMARIZE": "summarize",
                "DONE": "done"
            }
        )
        
        # 2. Add standard edge from retrieve to generate
        graph.add_edge("retrieve", "generate")
        
        # 3. FIXED: Use conditional routing for generate node based on its action output
        # This allows summarization to happen when needed instead of bypassing it
        graph.add_conditional_edges(
            "generate",
            router,
            {
                "SUMMARIZE": "summarize",
                "DONE": "done"
            }
        )
        
        # 4. Summarizer always proceeds to done
        graph.add_edge("summarize", "done")
        
        # Set the entry point
        graph.set_entry_point("supervisor")
        
        # Compile the graph
        return graph.compile()

    def run(self, messages: List[Dict[str, Any]], stream: bool = False) -> Union[List[Dict[str, Any]], Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]]:
        """
        Run the chatbot workflow.

        Args:
            messages: List of chat messages
            stream: Whether to stream the output

        Returns:
            If stream=False: Updated list of chat messages
            If stream=True: Tuple of (updated messages, execution steps)
        """
        # Prepare the initial state with correct typing
        state: ChatbotState = {
            "messages": messages,
            "query": "",
            "retrieved_docs": [],
            "current_answer": "",
            "action": None,
            "error": ""
        }

        # Run the graph with proper error handling for specific error types
        try:
            if stream:
                # Try different API patterns based on LangGraph version
                try:
                    # Newer LangGraph versions (0.0.x)
                    if hasattr(self.graph, 'stream'):
                        result_stream = self.graph.stream(state)
                        
                        final_state = None
                        steps = []
                        
                        for step in result_stream:
                            final_state = step
                            steps.append(step)
                            if self.debug:
                                print(f"Step: {step.get('action', 'unknown')}")
                        
                        if final_state:
                            return final_state["messages"], steps
                        return messages, []
                    # Older LangGraph compatibility
                    elif hasattr(self.graph, 'run'):
                        if self.debug:
                            print("Using older LangGraph API with 'run' method")
                        result = self.graph.run(state)
                        return result["messages"], [result]
                    else:
                        # Last resort
                        if self.debug:
                            print("No suitable streaming method found, trying direct execution")
                        result = self.graph(state)
                        return result["messages"], [result]
                except Exception as stream_error:
                    if self.debug:
                        print(f"Error in stream mode: {stream_error}")
                    return messages, []
            else:
                # Normal mode - try different method patterns
                for method_name in ['invoke', 'run', '__call__']:
                    if hasattr(self.graph, method_name):
                        try:
                            method = getattr(self.graph, method_name)
                            if callable(method):
                                if self.debug:
                                    print(f"Using {method_name} method")
                                result = method(state)
                                return result["messages"]
                        except Exception as e:
                            if self.debug:
                                print(f"Error with {method_name}: {e}")
                            continue
                
                # If nothing works, try direct calling
                try:
                    if callable(self.graph):
                        result = self.graph(state)
                        return result["messages"]
                except Exception as e:
                    if self.debug:
                        print(f"Error with direct call: {e}")
                
                # If all fails, return original messages
                return messages

        except KeyError as e:
            print(f"State key error: {str(e)}")
            return messages if not stream else (messages, [])
        except ValueError as e:
            print(f"Value error in graph execution: {str(e)}")
            return messages if not stream else (messages, [])
        except Exception as e:
            print(f"Unexpected error executing graph: {str(e)}")
            return messages if not stream else (messages, [])

# The _execute_graph method is removed since we're now using the standard API directly
# in the run method with invoke and stream
