"""
This file contains the fixed version of the vector_database_v3.py script.
The key fix is in the load_data_for_chroma function to properly handle None values in metadata.
"""

def load_data_for_chroma(chunks_with_embeddings_filepath_str):
    """
    Load chunks, their pre-computed embeddings, and metadata from the JSON file.
    Prepares data in the format required by ChromaDB.
    
    FIXED: This version properly handles None values in metadata
    """
    chunks_file = Path(chunks_with_embeddings_filepath_str)
    if not chunks_file.exists():
        logger.error(f"Data file not found: {chunks_file}. Please run the embedding generation script first.")
        return None, None, None, None

    try:
        with open(chunks_file, "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
        
        logger.info(f"Loaded {len(loaded_data)} items from {chunks_file}")
        
        ids_list = []
        embeddings_list = []
        documents_list = []
        metadatas_list = []
        
        for i, item in enumerate(tqdm(loaded_data, desc="Preparing data for ChromaDB")):
            # Using page_content as the primary field, with fallback to content or text
            doc_content = item.get('page_content', item.get('content', item.get('text', '')))
            embedding_vector = item.get('embedding')
            
            # Initialize metadata_dict - start with an empty dict
            metadata_dict = {}
            
            # If metadata exists, copy it first
            if 'metadata' in item and isinstance(item['metadata'], dict):
                for k, v in item['metadata'].items():
                    if v is None:
                        # Convert None to string "None"
                        metadata_dict[k] = "None"
                    elif isinstance(v, (str, int, float, bool)):
                        metadata_dict[k] = v
                    else:
                        # Convert any other types to string
                        metadata_dict[k] = str(v)
            
            # Add other fields from the item to metadata, except embedding and content
            for key, value in item.items():
                if key not in ['embedding', 'page_content', 'content', 'text', 'metadata']:
                    if value is None:
                        metadata_dict[key] = "None"  # Convert None to string
                    elif isinstance(value, (str, int, float, bool)):
                        metadata_dict[key] = value
                    else:
                        metadata_dict[key] = str(value)  # Convert other types to string
            
            if not doc_content or embedding_vector is None:
                logger.warning(f"Skipping item at index {i} due to missing content or embedding.")
                continue
            
            # Add chunk_id as the document ID if available
            doc_id = item.get('chunk_id', item.get('id', f"doc_{i}"))
            
            ids_list.append(doc_id)
            embeddings_list.append(embedding_vector)
            documents_list.append(doc_content)
            metadatas_list.append(metadata_dict)
        
        if not ids_list:
            logger.error("No valid data to load for ChromaDB.")
            return None, None, None, None

        logger.info(f"Prepared {len(ids_list)} items for ChromaDB.")
        logger.info(f"Sample ID: {ids_list[0]}")
        logger.info(f"Sample Document (start): {documents_list[0][:100]}...")
        logger.info(f"Sample Metadata: {metadatas_list[0]}")
        
        return ids_list, embeddings_list, documents_list, metadatas_list
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing JSON file {chunks_file}: {e}")
        return None, None, None, None
    except Exception as e:
        logger.error(f"Unexpected error loading data for ChromaDB: {e}", exc_info=True)
        return None, None, None, None
