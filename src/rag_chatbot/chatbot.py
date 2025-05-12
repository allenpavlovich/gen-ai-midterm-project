"""
User-facing interface for the RAG Chatbot.

This module provides a simple interface to interact with the RAG chatbot.
"""

from typing import List, Dict, Any, Optional, Tuple, Union
from .graph import RAGChatbotGraph

class RAGChatbot:
    """
    User-facing interface for the RAG chatbot.
    """
    
    def __init__(self, model="gpt-4o", debug=False):
        """
        Initialize the RAG chatbot.
        
        Args:
            model (str): The OpenAI model to use.
            debug (bool): Whether to print debug information.
        """
        self.graph = RAGChatbotGraph(model=model, debug=debug)
        self.messages = []
        self.debug = debug
    
    def reset(self):
        """
        Reset the conversation history.
        """
        self.messages = []
        
    def add_message(self, role: str, content: str):
        """
        Add a message to the conversation history.
        
        Args:
            role (str): The role of the message sender (user or assistant).
            content (str): The content of the message.
        """
        self.messages.append({"role": role, "content": content})
    
    def chat(self, user_message: str, stream: bool = False) -> Union[str, Tuple[str, List[Dict[str, Any]]]]:
        """
        Process a user message and return the assistant's response.
        
        Args:
            user_message (str): The user's message.
            stream (bool): Whether to stream the output (for debugging).
            
        Returns:
            If stream=False: str - The assistant's response
            If stream=True: Tuple[str, List] - The assistant's response and debug steps
        """
        # Add the user message
        self.add_message("user", user_message)
        
        # Process the message
        if stream:
            updated_messages, steps = self.graph.run(self.messages.copy(), stream=True)
            
            # Update the conversation history
            self.messages = updated_messages
            
            # Return the assistant's response and the debug steps
            return self.messages[-1]["content"], steps
        else:
            updated_messages = self.graph.run(self.messages.copy(), stream=False)
            
            # Update the conversation history
            self.messages = updated_messages
            
            # Return just the assistant's response
            return self.messages[-1]["content"]
    
    def get_conversation_history(self) -> List[Dict[str, str]]:
        """
        Get the full conversation history.
        
        Returns:
            List[Dict[str, str]]: The conversation history.
        """
        return self.messages
