"""
ChromaDB Retriever for the RAG Chatbot.

This module handles connections to ChromaDB and retrieves relevant documents
based on semantic similarity to a user query.
"""

import os
import chromadb
from sentence_transformers import SentenceTransformer

# Constants
CHROMA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/chroma_db"))
COLLECTION_NAME = "ms_applied_data_science"

class ChromaDBRetriever:
    """
    A class to handle connections to ChromaDB and retrieve relevant documents.
    """
    
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        """
        Initialize the ChromaDB retriever.
        
        Args:
            model_name (str): Name of the sentence transformer model to use for embeddings.
        """
        self.client = None
        self.collection = None
        self.embedding_model = None
        self.model_name = model_name
        
    def initialize(self):
        """
        Initialize the ChromaDB client, collection, and embedding model.
        
        Returns:
            bool: True if initialization successful, False otherwise.
        """
        try:
            # Initialize sentence transformer model
            self.embedding_model = SentenceTransformer(self.model_name)
            
            # Initialize ChromaDB client
            self.client = chromadb.PersistentClient(path=CHROMA_DIR)
            
            # Get the collection
            try:
                self.collection = self.client.get_collection(name=COLLECTION_NAME)
                print(f"Retrieved existing collection '{COLLECTION_NAME}'")
            except Exception:
                # Collection doesn't exist - this is an error state as collection should be pre-created
                print(f"Error: Collection '{COLLECTION_NAME}' not found in ChromaDB.")
                return False
                
            return True
            
        except Exception as e:
            print(f"Error initializing ChromaDB retriever: {e}")
            return False
    
    def retrieve_documents(self, query, top_k=5):
        """
        Retrieve relevant documents based on the query.
        
        Args:
            query (str): User query to search for.
            top_k (int): Number of documents to retrieve.
            
        Returns:
            list: List of documents with their metadata, or empty list if retrieval fails.
        """
        if not self.collection or not self.embedding_model:
            print("ChromaDB retriever not initialized. Call initialize() first.")
            return []
        
        try:
            # Generate query embedding
            query_embedding = self.embedding_model.encode(query).tolist()
            
            # Query the collection
            results = self.collection.query(
                query_embeddings=query_embedding,
                n_results=top_k
            )
            
            # Format the results
            documents = []
            if results and len(results["ids"]) > 0:
                for i in range(len(results["ids"][0])):
                    document = {
                        "id": results["ids"][0][i],
                        "content": results["documents"][0][i],
                        "metadata": results["metadatas"][0][i] if "metadatas" in results else {}
                    }
                    documents.append(document)
            
            return documents
            
        except Exception as e:
            print(f"Error retrieving documents: {e}")
            return []
    
    def format_for_prompt(self, documents):
        """
        Format retrieved documents for inclusion in a prompt.
        
        Args:
            documents (list): List of document dictionaries.
            
        Returns:
            str: Formatted string of documents with source information.
        """
        if not documents:
            return "No relevant information found."
        
        formatted_docs = []
        for i, doc in enumerate(documents):
            content = doc["content"]
            metadata = doc["metadata"]
            
            # Format source information
            source = metadata.get("source", "Unknown source")
            title = metadata.get("title", "")
            source_info = f"[Source: {source}" + (f", {title}" if title else "") + "]"
            
            # Format the document
            formatted_doc = f"Document {i+1}:\n{content}\n{source_info}\n"
            formatted_docs.append(formatted_doc)
        
        return "\n".join(formatted_docs)
