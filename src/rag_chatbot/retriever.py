"""
ChromaDB Retriever for the RAG Chatbot.

This module handles connections to ChromaDB and retrieves relevant documents
based on semantic similarity to a user query.
"""

import os
import re
import chromadb
from sentence_transformers import SentenceTransformer
from typing import List, Dict, Any, Optional, Union

# Constants
CHROMA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/chroma_db/header_chunks"))
#COLLECTION_NAME = "uchicago_ms_applied_ds"
COLLECTION_NAME = "uchicago_ms_applied_ds_header_chunks"

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
    
    def retrieve_documents(self, query, top_k=5, similarity_threshold=0.5, use_mmr=True, diversity_factor=0.3, use_hybrid_search=True):
        """
        Retrieve relevant documents based on the query using advanced retrieval techniques.
        
        Args:
            query (str): User query to search for.
            top_k (int): Number of documents to retrieve (increased default for GPT-4-turbo).
            similarity_threshold (float): Minimum similarity score threshold [0-1].
            use_mmr (bool): Whether to use Maximum Marginal Relevance for diversity.
            diversity_factor (float): Balance between relevance and diversity [0-1].
                                      Higher values favor diversity.
            
        Returns:
            list: List of documents with their metadata, or empty list if retrieval fails.
        """
        if not self.collection or not self.embedding_model:
            print("ChromaDB retriever not initialized. Call initialize() first.")
            return []
        
        try:
            # Implement query expansion for better results
            expanded_queries = self._expand_query(query)
            
            # Generate query embedding(s)
            query_embeddings = [self.embedding_model.encode(q).tolist() for q in expanded_queries]
            main_query_embedding = query_embeddings[0]  # Original query embedding
            
            # Perform simpler hybrid search that works with all ChromaDB versions
            if use_hybrid_search:
                try:
                    # Simple keyword search implementation
                    keyword_results = self.collection.query(
                        query_texts=query,  # Use query_texts parameter which works in newer ChromaDB versions
                        n_results=top_k // 2
                    )
                except Exception as e:
                    print(f"Keyword search failed, trying alternative method: {e}")
                    try:
                        # Alternative approach for older ChromaDB versions
                        keyword_results = self.collection.query(
                            query_texts=[query],  # Some versions expect a list
                            n_results=top_k // 2
                        )
                    except Exception as e2:
                        print(f"All keyword search methods failed: {e2}")
                        keyword_results = None
            else:
                keyword_results = None
                
            # For specific queries about courses, add a direct content filter
            course_related = False
            if any(term in query.lower() for term in ["course", "courses", "core", "curriculum", "class", "classes"]):
                course_related = True
            
            # Query the collection with MMR if enabled
            if use_mmr and hasattr(self.collection, 'query_with_mmr'):
                vector_results = self.collection.query_with_mmr(
                    query_embeddings=main_query_embedding,
                    n_results=top_k,
                    lambda_mult=diversity_factor,
                    include=['documents', 'metadatas', 'distances', 'embeddings']
                )
            else:
                # Standard vector search
                vector_results = self.collection.query(
                    query_embeddings=main_query_embedding,
                    n_results=top_k,
                    include=['documents', 'metadatas', 'distances', 'embeddings']
                )
                
            # Combine results if we have both keyword and vector results
            if keyword_results and vector_results:
                results = self._combine_results(keyword_results, vector_results, top_k)
            else:
                results = vector_results
            
            # Filter and format the results
            documents = []
            if results and len(results["ids"]) > 0:
                for i in range(len(results["ids"][0])):
                    # Skip if below similarity threshold (distances are typically normalized in [0,1] or [0,2])
                    # Higher distance = less similar, so we want distance < (1-threshold) for dist in [0,1]
                    # or distance < (2-threshold*2) for dist in [0,2]
                    if "distances" in results and results["distances"][0][i] > (1 - similarity_threshold):
                        # For course-related queries, be more lenient with threshold
                        if not course_related:
                            continue
                        
                    document = {
                        "id": results["ids"][0][i],
                        "content": results["documents"][0][i],
                        "metadata": results["metadatas"][0][i] if "metadatas" in results else {},
                        "similarity": 1 - results["distances"][0][i] if "distances" in results else 1.0
                    }
                    documents.append(document)
            
            # For core course queries, always explicitly scan through collection even if we found documents
            if course_related and "core" in query.lower():
                print("Performing direct course search due to poor retrieval results")
                try:
                    # Get more documents from the collection
                    all_results = self.collection.query(
                        query_embeddings=main_query_embedding,
                        n_results=50  # Get many more to scan through
                    )
                    
                    # Look for documents with core course keywords
                    if all_results and len(all_results["ids"]) > 0:
                        course_documents = []
                        max_content_length = 15000  # Truncate content to 500 chars max
                        
                        # Set a hard limit on the max number of course docs
                        max_course_docs = 20  
                        
                        for i in range(len(all_results["ids"][0])):
                            content = all_results["documents"][0][i]
                            # More selective filtering - prefer exact matches for core courses
                            if any(marker in content.lower() for marker in [
                                "core course", "required course", "core courses", "required courses", 
                                "curriculum"]):
                                
                                # Truncate content to reduce token count
                                if len(content) > max_content_length:
                                    truncated_content = content[:max_content_length] + "..."
                                else:
                                    truncated_content = content
                                    
                                doc = {
                                    "id": all_results["ids"][0][i],
                                    "content": truncated_content,
                                    "metadata": all_results["metadatas"][0][i] if "metadatas" in all_results else {},
                                    "similarity": 0.9  # High assumed relevance for these
                                }
                                course_documents.append(doc)
                                
                                # Enforce hard limit on document count
                                if len(course_documents) >= max_course_docs:
                                    break
                        
                        # Add these to our results if we found any
                        if course_documents:
                            print(f"Found {len(course_documents)} course-related documents through direct search")
                            documents.extend(course_documents)
                except Exception as e:
                    print(f"Direct course search failed: {e}")
            
            # Sort by similarity score for consistent ordering
            documents.sort(key=lambda x: x.get("similarity", 0), reverse=True)
            
            return documents
            
        except Exception as e:
            print(f"Error retrieving documents: {e}")
            return []
    
    def _expand_query(self, query: str) -> List[str]:
        """
        Expand the original query to improve retrieval by adding variations.
        
        Args:
            query: The original user query
            
        Returns:
            A list of query variations, with the original query as the first element
        """
        expanded_queries = [query]  # Always keep the original query first
        
        # 1. Add a version that focuses on course-related keywords if relevant
        course_keywords = ["course", "courses", "class", "classes", "program", "curriculum"]
        if any(keyword in query.lower() for keyword in course_keywords):
            if "core" in query.lower():
                expanded_queries.append(f"curriculum core courses {query}")
                expanded_queries.append(f"required core courses in the program")
            if "elective" in query.lower():
                expanded_queries.append(f"elective courses options {query}")
            expanded_queries.append(f"course list for {query}")
            expanded_queries.append(f"course descriptions {query}")
        
        # 2. Add a version that extracts key entities from the query
        words = query.lower().split()
        if len(words) > 3:  # Only for longer queries where extraction makes sense
            # Extract nouns and important keywords using a simple heuristic
            stop_words = ["a", "an", "the", "of", "in", "for", "to", "on", "with", "what", "are", "is", "do", "does"]
            content_words = [w for w in words if w not in stop_words]
            if content_words:
                expanded_queries.append(" ".join(content_words))
        
        # 3. Add search variations for specific query patterns
        if "what" in query.lower() and "core courses" in query.lower():
            expanded_queries.append("core courses curriculum")
            expanded_queries.append("required foundation courses")
            expanded_queries.append("core course list descriptions")
        
        return expanded_queries
    
    def _combine_results(self, keyword_results, vector_results, top_k):
        """
        Combine keyword search and vector search results, removing duplicates.
        
        Args:
            keyword_results: Results from keyword search
            vector_results: Results from vector search
            top_k: Maximum number of results to return
            
        Returns:
            Combined results dictionary
        """
        # Initialize with the structure from vector results
        combined = {
            "ids": [[]],
            "distances": [[]],
            "documents": [[]],
            "metadatas": [[]]
        }
        
        # Track seen IDs to avoid duplicates
        seen_ids = set()
        
        # Helper to add a result
        def add_result(result_dict, idx):
            result_id = result_dict["ids"][0][idx]
            if result_id in seen_ids:
                return
            
            seen_ids.add(result_id)
            combined["ids"][0].append(result_id)
            combined["documents"][0].append(result_dict["documents"][0][idx])
            
            # Handle optional fields
            if "distances" in result_dict and result_dict["distances"]:
                combined["distances"][0].append(result_dict["distances"][0][idx])
            if "metadatas" in result_dict and result_dict["metadatas"]:
                combined["metadatas"][0].append(result_dict["metadatas"][0][idx])
        
        # First add keyword results which are usually more precise
        if keyword_results and "ids" in keyword_results and keyword_results["ids"]:
            for i in range(min(len(keyword_results["ids"][0]), top_k // 2)):
                add_result(keyword_results, i)
        
        # Then add vector results
        if vector_results and "ids" in vector_results and vector_results["ids"]:
            for i in range(min(len(vector_results["ids"][0]), top_k)):
                if len(combined["ids"][0]) >= top_k:
                    break
                add_result(vector_results, i)
        
        return combined
    
    def format_for_prompt(self, documents, include_similarity=True, max_docs=None):
        """
        Format retrieved documents for inclusion in a prompt.
        
        Args:
            documents (list): List of document dictionaries.
            include_similarity (bool): Whether to include similarity scores.
            max_docs (int): Optional limit on the number of documents to format.
            
        Returns:
            str: Formatted string of documents with source information.
        """
        if not documents:
            return "No relevant information found."
        
        # Apply document limit if specified
        if max_docs is not None and max_docs > 0:
            documents = documents[:max_docs]
            
        formatted_docs = []
        for i, doc in enumerate(documents):
            content = doc["content"]
            metadata = doc["metadata"]
            similarity = doc.get("similarity", None)
            
            # Format source information
            source = metadata.get("source", "Unknown source")
            title = metadata.get("title", "")
            
            # Include additional metadata if available
            page = metadata.get("page", "")
            filename = metadata.get("filename", "")
            
            # Build source string
            source_parts = []
            if source and source != "Unknown source":
                source_parts.append(f"Source: {source}")
            if title:
                source_parts.append(f"Title: {title}")
            if page:
                source_parts.append(f"Page: {page}")
            if filename:
                source_parts.append(f"File: {filename}")
            if include_similarity and similarity is not None:
                source_parts.append(f"Relevance: {similarity:.2f}")
                
            source_info = "[" + ", ".join(source_parts) + "]" if source_parts else "[Unknown source]"
            
            # Format the document with separation for readability
            formatted_doc = f"Document {i+1}:\n{'-' * 40}\n{content}\n{source_info}\n{'-' * 40}"
            formatted_docs.append(formatted_doc)
        
        return "\n".join(formatted_docs)
