import chromadb
import json
from typing import Dict, List, Any
from chromadb.api import ClientAPI
from chromadb.utils.embedding_functions.ollama_embedding_function import OllamaEmbeddingFunction

from pydantic import BaseModel

class CollectionConfig(BaseModel):
    name: str
    description: str
    metadata_schema: Dict[str, str]

class CollectionManager:
    def __init__(self, client: ClientAPI, embedding_fn: OllamaEmbeddingFunction):
        self.client = client
        self.collections = {}
        self.embedding_fn = embedding_fn

    def create_collection(self, collection_config: CollectionConfig) -> chromadb.Collection:
        """
        Create ChromaDB collection
        """
        collection = self.client.get_or_create_collection(
            name=collection_config.name,
            embedding_function=self.embedding_fn,
            metadata={
                "description": collection_config.description,
                "metadata_schema": json.dumps(collection_config.metadata_schema)
            }
        )

        self.collections[collection_config.name] = collection
        return collection

    def get_collections(self) -> List[Dict[str, Any]]:
        """
        Get and return all current collections in DB
        """
        collections = self.client.list_collections()
        collection_info = []

        for collection in collections:
            info = {
                "name": collection.name,
                "count": collection.count(),
                "metadata": collection.metadata if hasattr(collection, 'metadata') else {}
            }
            collection_info.append(info)

        return collection_info