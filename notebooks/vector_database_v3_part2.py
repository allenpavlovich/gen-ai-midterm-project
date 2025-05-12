# ChromaDB client and collection initialization
def initialize_chroma_client_and_collection(db_path_str, collection_name_str):
    """
    Initialize ChromaDB client and create/get a collection.
    
    Args:
        db_path_str (str): Path to the ChromaDB persistent directory
        collection_name_str (str): Name of the collection to create or get
        
    Returns:
        tuple: (client, collection) instances or (None, None) if error
    """
    try:
        logger.info(f"Initializing ChromaDB client with persistence path: {db_path_str}")
        client = chromadb.PersistentClient(path=db_path_str)
        
        # Create a new collection or get existing one
        try:
            # Try to get existing collection
            collection = client.get_collection(name=collection_name_str)
            logger.info(f"Loaded existing collection '{collection_name_str}' with {collection.count()} documents")
        except Exception:
            # Create new collection if it doesn't exist
            logger.info(f"Creating new collection '{collection_name_str}'")
            collection = client.create_collection(
                name=collection_name_str,
                metadata={"description": "UChicago MS in Applied Data Science documents"}
            )
            logger.info(f"Created new collection '{collection_name_str}'")
        
        return client, collection
    except Exception as e:
        logger.error(f"Error initializing ChromaDB client or collection: {e}", exc_info=True)
        return None, None

# Add data to ChromaDB collection
def add_data_to_chroma_collection(collection_instance, ids_list, embeddings_list, documents_list, metadatas_list, batch_size=CHROMA_ADD_BATCH_SIZE):
    """
    Add data to the ChromaDB collection in batches.
    
    Args:
        collection_instance: ChromaDB collection instance
        ids_list: List of document IDs
        embeddings_list: List of embedding vectors
        documents_list: List of document texts
        metadatas_list: List of document metadata dictionaries
        batch_size: Number of documents to add in each batch
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        n_items = len(ids_list)
        logger.info(f"Adding {n_items} documents to collection in batches of {batch_size}")
        
        for i in tqdm(range(0, n_items, batch_size), desc="Adding batches to ChromaDB"):
            batch_end_idx = min(i + batch_size, n_items)
            
            current_batch_ids = ids_list[i:batch_end_idx]
            current_batch_embeddings = embeddings_list[i:batch_end_idx]
            current_batch_documents = documents_list[i:batch_end_idx]
            current_batch_metadatas = metadatas_list[i:batch_end_idx]
            
            collection_instance.add(
                ids=current_batch_ids,
                embeddings=current_batch_embeddings,
                documents=current_batch_documents,
                metadatas=current_batch_metadatas
            )
            
        logger.info(f"Successfully added all {n_items} documents to ChromaDB collection")
        return True
    except Exception as e:
        logger.error(f"Error adding data to ChromaDB: {e}", exc_info=True)
        return False

# Initialize query embedding model
def initialize_query_embedding_model(model_name=QUERY_EMBEDDING_MODEL_NAME):
    """
    Initialize the Sentence Transformer model for encoding query texts.
    
    Args:
        model_name (str): Name of the pre-trained model to use
        
    Returns:
        SentenceTransformer: Initialized model or None if error
    """
    try:
        logger.info(f"Loading query embedding model: {model_name}")
        model = SentenceTransformer(model_name)
        
        # Check if we can use GPU
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        model.to(device)
        logger.info(f"Query embedding model loaded and using device: {device}")
        
        return model
    except Exception as e:
        logger.error(f"Error loading query embedding model '{model_name}': {e}", exc_info=True)
        return None

# Query function for the ChromaDB collection
def query_chroma_collection(collection_instance, query_text, embedding_model, top_n_results=5, metadata_filter_dict=None):
    """
    Query the ChromaDB collection using the given query text.
    
    Args:
        collection_instance: ChromaDB collection instance
        query_text (str): The query text to search for
        embedding_model: SentenceTransformer model for encoding the query
        top_n_results (int): Number of results to return
        metadata_filter_dict (dict, optional): Dictionary for filtering results by metadata fields
        
    Returns:
        dict: Query results from ChromaDB
    """
    try:
        # Generate embedding for the query text
        query_embedding = embedding_model.encode(query_text)
        
        # Query the collection
        results = collection_instance.query(
            query_embeddings=[query_embedding],
            n_results=top_n_results,
            where=metadata_filter_dict,  # Optional metadata filter
            include=["documents", "metadatas", "distances"]
        )
        
        return results
    except Exception as e:
        logger.error(f"Error querying ChromaDB: {e}", exc_info=True)
        return None

# Display query results
def display_query_search_results(results, query_text):
    """
    Display the results of a ChromaDB query in a readable format.
    
    Args:
        results (dict): Results from a ChromaDB query
        query_text (str): The original query text
    """
    if not results or not results.get('documents'):
        logger.info(f"No results found for query: '{query_text}'")
        return
    
    docs = results.get('documents', [[]])[0]
    metadatas = results.get('metadatas', [[]])[0]
    distances = results.get('distances', [[]])[0]
    
    logger.info(f"\n--- Results for query: '{query_text}' ---")
    
    for i, (doc, meta, dist) in enumerate(zip(docs, metadatas, distances)):
        logger.info(f"\nResult #{i+1} (Distance: {dist:.4f}):")
        
        # Display metadata
        if meta:
            title = meta.get('document_title', meta.get('title', 'Unknown'))
            section = meta.get('section', '')
            subsection = meta.get('subsection', '')
            logger.info(f"Document: {title}")
            if section:
                logger.info(f"Section: {section}")
            if subsection:
                logger.info(f"Subsection: {subsection}")
        
        # Display document snippet
        doc_snippet = doc[:300] + "..." if len(doc) > 300 else doc
        logger.info(f"Content: {doc_snippet}")

# Function to build a context for retrieval-augmented generation
def build_retrieval_context(query_text, top_k_docs, collection_inst, query_embed_model_inst):
    """
    Build a retrieval context by querying the ChromaDB collection.
    This context can be used for RAG applications.
    
    Args:
        query_text (str): The query text
        top_k_docs (int): Number of documents to retrieve
        collection_inst: ChromaDB collection instance
        query_embed_model_inst: SentenceTransformer model instance
        
    Returns:
        list: List of retrieved context strings
    """
    results = query_chroma_collection(
        collection_inst, 
        query_text, 
        query_embed_model_inst, 
        top_n_results=top_k_docs
    )
    
    if not results or not results.get('documents'):
        logger.warning(f"No documents retrieved for query: '{query_text}'")
        return []
    
    # Extract documents and their metadata
    retrieved_contexts = []
    docs = results.get('documents', [[]])[0]
    metadatas = results.get('metadatas', [[]])[0]
    
    for i, (doc, meta) in enumerate(zip(docs, metadatas)):
        # Create a formatted context string with metadata and content
        title = meta.get('document_title', meta.get('title', 'Unknown'))
        section = meta.get('section', '')
        subsection = meta.get('subsection', '')
        
        context_header = f"Source {i+1}: {title}"
        if section:
            context_header += f" | Section: {section}"
        if subsection:
            context_header += f" | Subsection: {subsection}"
            
        context_str = f"{context_header}\n\n{doc}\n"
        retrieved_contexts.append(context_str)
    
    return retrieved_contexts

# Main execution
db_creation_start_time = time.time()

logger.info("Starting vector database creation process")

# 1. Load the data
ids, embeddings, documents, metadatas = load_data_for_chroma(CHUNKS_WITH_EMBEDDINGS_FILE)

if ids:
    # 2. Initialize ChromaDB
    chroma_client, chroma_collection_instance = initialize_chroma_client_and_collection(
        CHROMA_DB_DIR, COLLECTION_NAME
    )
    
    if chroma_collection_instance:
        # 3. Add data to ChromaDB
        success = add_data_to_chroma_collection(
            chroma_collection_instance, ids, embeddings, documents, metadatas
        )
        
        if success:
            logger.info(f"ChromaDB collection '{COLLECTION_NAME}' created successfully with {len(ids)} documents")
            
            # 4. Initialize the embedding model for queries
            query_model = initialize_query_embedding_model(QUERY_EMBEDDING_MODEL_NAME)
            
            if query_model:
                # 5. Test some queries
                sample_test_queries = [
                    "What are the core courses for the MS in Applied Data Science?",
                    "Tell me about the faculty specializing in machine learning.",
                    "What are the admission requirements?",
                    "How is the capstone project structured?"
                ]
                for test_q in sample_test_queries:
                    results = query_chroma_collection(chroma_collection_instance, test_q, query_model, top_n_results=3)
                    display_query_search_results(results, test_q)
                
                # Test with metadata filter (example)
                if metadatas: # Check if metadatas list is not empty
                    sample_category = metadatas[0].get('category')
                    if sample_category:
                        logger.info(f"\n--- Testing Query with Metadata Filter (category: {sample_category}) ---")
                        filtered_query = "capstone project"
                        filter_criteria = {"category": sample_category} 
                        # Example of more complex filter: {"$and": [{"category": "education"}, {"title": {"$contains": "Online"}}]}
                        
                        filtered_results = query_chroma_collection(
                            chroma_collection_instance, filtered_query, query_model, 
                            top_n_results=2, metadata_filter_dict=filter_criteria
                        )
                        display_query_search_results(filtered_results, f"{filtered_query} (filtered by category: {sample_category})")
                    else:
                        logger.info("Skipping metadata filter test as no sample category found in the first chunk.")
                
                # 6. Test the context retrieval function
                logger.info("\n--- Testing Context Retrieval Function ---")
                retrieved_contexts = build_retrieval_context(
                    "What are the core courses?", 
                    top_k_docs=2, 
                    collection_inst=chroma_collection_instance, # Pass instances
                    query_embed_model_inst=query_model           # Pass instances
                )
                for i, ctx in enumerate(retrieved_contexts):
                    logger.info(f"\nRetrieved Context #{i+1}:\n{ctx}")
            else:
                logger.error("Query embedding model could not be initialized. Query testing skipped.")
        else:
            logger.error("Failed to add data to ChromaDB collection. Process halted.")
    else:
        logger.error("ChromaDB collection could not be initialized. Process halted.")
else:
    logger.error(f"Failed to load data from {CHUNKS_WITH_EMBEDDINGS_FILE}. Process halted.")

db_creation_end_time = time.time()
elapsed_processing_time = db_creation_end_time - db_creation_start_time
logger.info(f"--- Vector Database Process Completed in {elapsed_processing_time:.2f} seconds ---")
