"""
Agents for the RAG Chatbot.

This module contains the Supervisor, Reasoner, and Summarizer agents
for the RAG chatbot architecture.
"""

import json
from typing import List, Dict, Any, Optional, Literal, TypedDict, Union, cast
from openai import OpenAI

# Agent action types
AgentAction = Literal["RETRIEVE", "GENERATE", "SUMMARIZE", "DONE"]

class SupervisorAgent:
    """
    The Supervisor Agent evaluates the quality of user queries and context,
    and decides which action to take next in the workflow.
    """
    
    def __init__(self, model="gpt-4o"):
        """
        Initialize the Supervisor Agent.
        
        Args:
            model (str): The OpenAI model to use.
        """
        self.client = OpenAI()
        self.model = model
        
    def run(self, 
            query: str, 
            chat_history: List[Dict[str, str]] = None, 
            retrieved_docs: List[Dict[str, Any]] = None,
            current_answer: str = None) -> Dict[str, Any]:
        """
        Run the Supervisor Agent to decide the next action.
        
        Args:
            query: The user's current query
            chat_history: List of conversation history dictionaries
            retrieved_docs: Documents retrieved for the current query
            current_answer: Current answer being generated (if any)
            
        Returns:
            Dict with action decision and any additional context
        """
        if chat_history is None:
            chat_history = []
        
        # Build the system prompt
        system_prompt = """You are the Supervisor for a university's Applied Data Science program chatbot.
Your role is to analyze the user's question and decide the next steps in our workflow:

1. RETRIEVE: Get documents from the database if more information is needed
2. GENERATE: Create a detailed answer using the retrieved documents
3. SUMMARIZE: Condense a lengthy answer to be more concise
4. DONE: Return the current answer as it is satisfactory

The Applied Data Science program is a master's degree focusing on data science,
machine learning, statistics, and programming skills.

Return your decision as JSON with the format: {"action": "ACTION_TYPE", "reasoning": "your reasoning"}
"""

        # Build conversation messages
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": self._build_user_prompt(query, chat_history, retrieved_docs, current_answer)}
        ]
        
        # Call the OpenAI API
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                response_format={"type": "json_object"},
                temperature=0.0  # Set to 0 to minimize hallucination
            )
            
            # Parse the response
            response_text = response.choices[0].message.content
            result = json.loads(response_text)
            
            # Validate the response contains the required fields
            if "action" not in result:
                result = {"action": "RETRIEVE", "reasoning": "Default action due to malformed response"}
            
            return result
            
        except Exception as e:
            print(f"Error running Supervisor Agent: {e}")
            # Default to retrieve if there's an error
            return {"action": "RETRIEVE", "reasoning": f"Default action due to error: {str(e)}"}
    
    def _build_user_prompt(self, query: str, chat_history: List[Dict[str, str]], 
                          retrieved_docs: List[Dict[str, Any]] = None, 
                          current_answer: str = None) -> str:
        """
        Build the user prompt with all available context.
        
        Args:
            query: User query
            chat_history: Conversation history
            retrieved_docs: Retrieved documents
            current_answer: Current answer being generated
            
        Returns:
            Formatted prompt string
        """
        prompt_parts = [f"User Question: {query}\n"]
        
        # Add chat history
        if chat_history and len(chat_history) > 0:
            prompt_parts.append("Chat History:")
            for message in chat_history:
                role = message.get("role", "unknown")
                content = message.get("content", "")
                prompt_parts.append(f"{role}: {content}")
            prompt_parts.append("")
        
        # Add retrieved documents
        if retrieved_docs and len(retrieved_docs) > 0:
            prompt_parts.append("Retrieved Documents:")
            for i, doc in enumerate(retrieved_docs):
                content = doc.get("content", "")
                prompt_parts.append(f"Document {i+1}: {content[:500]}...")
            prompt_parts.append("")
        
        # Add current answer
        if current_answer:
            prompt_parts.append(f"Current Answer: {current_answer}")
        
        # Add decision request
        prompt_parts.append("\nBased on the above, what action should we take next? Choose from RETRIEVE, GENERATE, SUMMARIZE, or DONE.")
        prompt_parts.append("Please evaluate if we need more information, need to generate an answer, need to summarize a lengthy answer, or if the current answer is already good.")
        
        return "\n".join(prompt_parts)


class ReasonerAgent:
    """
    The Reasoner Agent generates detailed answers based on retrieved documents and user queries.
    """
    
    def __init__(self, model="gpt-4o"):
        """
        Initialize the Reasoner Agent.
        
        Args:
            model (str): The OpenAI model to use.
        """
        self.client = OpenAI()
        self.model = model
    
    def run(self, query: str, retrieved_docs: List[Dict[str, Any]], 
           chat_history: List[Dict[str, str]] = None) -> str:
        """
        Generate an answer based on the query and retrieved documents.
        
        Args:
            query: User's query
            retrieved_docs: List of retrieved documents
            chat_history: Conversation history
            
        Returns:
            Generated answer string
        """
        if chat_history is None:
            chat_history = []
        
        # Build the system prompt
        system_prompt = """You are a knowledgeable expert for a university's Applied Data Science program chatbot.
Your role is to provide detailed, accurate answers about the program based on the retrieved documents.

Guidelines:
1. Ground your answer in ONLY the provided documents.
2. IMPORTANT: If no relevant documents are found or the documents don't contain the necessary information to answer the question, explicitly state this limitation and DO NOT generate an answer based on general knowledge.
3. Never hallucinate or make up information not present in the documents.
4. Provide comprehensive yet concise answers when documents contain relevant information.
5. Use a professional, helpful tone appropriate for academic advising.
6. Organize information logically for ease of understanding.
"""

        # Format the documents for the prompt
        formatted_docs = self._format_documents(retrieved_docs)
        
        # Build the user prompt
        user_prompt = f"""Question: {query}

Retrieved Information:
{formatted_docs}

Based on the above information, please provide a comprehensive answer to the question."""

        # Add context from chat history if available
        if chat_history and len(chat_history) > 0:
            # Extract recent context
            context = "\nRelevant conversation context:\n"
            for message in chat_history[-3:]:  # Get last 3 messages for context
                role = message.get("role", "unknown")
                content = message.get("content", "")
                context += f"{role}: {content}\n"
            user_prompt += context

        # Call the OpenAI API
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )
            
            # Return the generated answer
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"Error running Reasoner Agent: {e}")
            return "I apologize, but I encountered an error while generating your answer. Please try again."
    
    def _format_documents(self, documents: List[Dict[str, Any]]) -> str:
        """
        Format retrieved documents for inclusion in the prompt.
        
        Args:
            documents: List of document dictionaries
            
        Returns:
            Formatted string of documents
        """
        # Handle the special case for no documents or the explicit "no results" document
        if not documents:
            return "IMPORTANT: NO RELEVANT DOCUMENTS FOUND. You must explicitly state that you don't have the information to answer this question and DO NOT fabricate a response based on general knowledge."
        
        # Check if the single document is our special "no results" marker
        if len(documents) == 1 and documents[0].get("id") == "no_results":
            return documents[0].get("content", "NO RELEVANT DOCUMENTS FOUND. You must explicitly state that you don't have the information to answer this question and DO NOT fabricate a response based on general knowledge.")
        
        formatted_parts = []
        for i, doc in enumerate(documents):
            content = doc.get("content", "")
            metadata = doc.get("metadata", {})
            
            # Add source information if available
            source = metadata.get("source", "Unknown source")
            title = metadata.get("title", "")
            source_info = f"Source: {source}" + (f", {title}" if title else "")
            
            formatted_parts.append(f"Document {i+1}:\n{content}\n{source_info}\n")
        
        return "\n".join(formatted_parts)


class SummarizerAgent:
    """
    The Summarizer Agent condenses lengthy information into concise answers.
    """
    
    def __init__(self, model="gpt-4o"):
        """
        Initialize the Summarizer Agent.
        
        Args:
            model (str): The OpenAI model to use.
        """
        self.client = OpenAI()
        self.model = model
    
    def run(self, answer: str, query: str) -> str:
        """
        Summarize a lengthy answer into a more concise response.
        
        Args:
            answer: The detailed answer to summarize
            query: The original user query for context
            
        Returns:
            Summarized answer
        """
        # Build the system prompt
        system_prompt = """You are a summarization expert for a university's Applied Data Science program chatbot.
Your task is to condense lengthy, detailed answers into clear, concise responses while preserving
the most important information and maintaining accuracy.

Guidelines:
1. Maintain all key facts and important details
2. Remove redundant or excessive examples
3. Use clear, concise language
4. Keep the professional, helpful tone
5. Focus on directly answering the user's question
"""

        # Build the user prompt
        user_prompt = f"""Original Question: {query}

Detailed Answer:
{answer}

Please summarize the above answer to be more concise while preserving all important information."""

        # Call the OpenAI API
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )
            
            # Return the summarized answer
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"Error running Summarizer Agent: {e}")
            # Return the original answer if there's an error
            return answer
