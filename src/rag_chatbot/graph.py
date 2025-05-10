"""
LangGraph Workflow for the RAG Chatbot.

This module implements the workflow graph for the RAG chatbot using LangGraph.
"""

from typing import Dict, List, Any, TypedDict, Annotated, Literal, cast
from langgraph.graph import StateGraph, MessagesState
from .agents import SupervisorAgent, ReasonerAgent, SummarizerAgent
from .retriever import ChromaDBRetriever

# Define state type
class ChatbotState(TypedDict):
    """Type definition for the chatbot state."""
    messages: List[Dict[str, Any]]  # Chat messages
    query: str  # Current user query
    retrieved_docs: List[Dict[str, Any]]  # Retrieved documents
    current_answer: str  # Current generated answer
    action: Literal["RETRIEVE", "GENERATE", "SUMMARIZE", "DONE"]  # Next action to take
    error: str  # Error message, if any


class RAGChatbotGraph:
    """
    Implements the LangGraph workflow for the RAG chatbot.
    """
    
    def __init__(self, model="gpt-3.5-turbo", debug=False):
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
        # Create a new graph
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
            
            # Retrieve documents
            query = state["query"]
            documents = self.retriever.retrieve_documents(query, top_k=5)
            
            # Handle empty results
            if not documents:
                state["retrieved_docs"] = []
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
        
        # Connect supervisor to other nodes through the router
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
        
        # Add standard edges
        graph.add_edge("retrieve", "generate")
        # Break the recursion cycle by having generate go directly to decision points
        # instead of back to supervisor, which can cause infinite loops
        graph.add_edge("generate", "done")
        graph.add_edge("summarize", "done")
        
        # Set the entry point
        graph.set_entry_point("supervisor")
        
        # Compile the graph
        return graph.compile()
    
    def run(self, messages: List[Dict[str, Any]], stream: bool = False) -> List[Dict[str, Any]]:
        """
        Run the chatbot workflow.
        
        Args:
            messages: List of chat messages
            stream: Whether to stream the output
            
        Returns:
            Updated list of chat messages
        """
        # Initialize state with all required fields
        state = {
            "messages": messages,
            "query": "",  # Will be set by supervisor node
            "retrieved_docs": [],  # Will be populated by retrieve node
            "current_answer": "",  # Will be populated by generate node
            "action": "",  # Will be set by supervisor node
            "error": ""  # For error handling
        }
        
        # In LangGraph 0.4.3, the compiled graph has specific execution methods
        try:
            if stream:
                # Stream mode
                if self.debug:
                    available_methods = [method for method in dir(self.graph) if not method.startswith('_')]
                    print(f"Debug - Available methods on compiled graph: {available_methods}")
                
                # Try different streaming methods
                if hasattr(self.graph, 'stream'):
                    result_stream = self.graph.stream(state)
                else:
                    # Fallback if stream isn't available
                    print("Warning: stream method not available. Using non-streaming approach.")
                    # Try to execute with normal mode and wrap in a list for consistent return type
                    try:
                        result = self._execute_graph(state)
                        return result["messages"], [result]
                    except Exception as inner_e:
                        print(f"Inner execution error: {str(inner_e)}")
                        return messages, []
                
                # Process the stream results
                final_state = None
                steps = []
                
                for step in result_stream:
                    final_state = step
                    steps.append(step)
                
                if final_state:
                    return final_state["messages"], steps
                return messages, []
            else:
                # Normal mode
                result = self._execute_graph(state)
                return result["messages"]
        except Exception as e:
            print(f"Error executing graph: {str(e)}")
            # If there's an exception, return the original messages
            return messages
    
    def _execute_graph(self, state):
        """Execute the compiled graph using available methods."""
        # Print available methods for debugging only when debug flag is set
        if self.debug:
            available_methods = [method for method in dir(self.graph) if not method.startswith('_')]
            print(f"Debug - Available methods: {available_methods}")
        
        # Try execution methods in order of likelihood
        if hasattr(self.graph, 'invoke'):
            return self.graph.invoke(state)
        elif hasattr(self.graph, 'start_and_run'):
            return self.graph.start_and_run(state)
        elif hasattr(self.graph, 'run'):
            return self.graph.run(state)
        elif hasattr(self.graph, 'run_executor'):
            return self.graph.run_executor(state)
        else:
            # Last resort: try to find any method with 'run' in its name
            for method_name in available_methods:
                if 'run' in method_name.lower() or 'exec' in method_name.lower():
                    try:
                        method = getattr(self.graph, method_name)
                        if callable(method):
                            return method(state)
                    except Exception as e:
                        print(f"Failed with method {method_name}: {str(e)}")
                        continue
            
            # If all else fails, try to diagnose
            if callable(self.graph):
                # Some versions expect direct calling
                try:
                    return self.graph(state)
                except Exception as e:
                    print(f"Failed with direct call: {str(e)}")
            
            # Try to find any property that might help us understand the graph state
            for method_name in available_methods:
                try:
                    attr = getattr(self.graph, method_name)
                    if not callable(attr):
                        print(f"Property {method_name}: {attr}")
                except Exception:
                    pass
            
            raise RuntimeError("Could not find a way to execute the compiled graph.")


