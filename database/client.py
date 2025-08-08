import os
import logging
import subprocess
import chromadb
from chromadb.utils.embedding_functions.ollama_embedding_function import OllamaEmbeddingFunction
from .collections import CollectionManager
from .schema import COLLECTION_SCHEMAS

class ChromaDBService:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=os.getenv("DB_PATH", "./chroma_db"))
        self.embedding_fn = OllamaEmbeddingFunction(
            url=os.getenv("OLLAMA_URL", "http://localhost:11434"),
            model_name=os.getenv("OLLAMA_MODEL", "jina/jina-embeddings-v2-base-en:latest")
        )

    def initialize_collections(self):
        """
        Creates collections if they don't exist, else it retrieves them
        """
        collections_manager = CollectionManager(
            client=self.client,
            embedding_fn=self.embedding_fn,
        )

        initialized_collections = {}

        for schema_name, collection_config in COLLECTION_SCHEMAS.items():
            try:
                collection = collections_manager.create_collection(collection_config)
                initialized_collections[schema_name] = collection

                count = collection.count()
                logging.info(f"{collection_config.name} initialized with {count} docs")
            except Exception as e:
                logging.error(f"Failed to initialize {schema_name}: {e}")

        return collections_manager, initialized_collections

    def run(self, host: str = "0.0.0.0", port: int = 8000):
        """
        Runs pipeline to initialize ChromaDB and its collections
        """
        logging.info("Starting ChromaDB server...")

        # Initialize collections
        manager, _ = self.initialize_collections()

        logging.info("Final Collection Status:")
        for collection in manager.get_collections():
            logging.info(f"  - {collection['name']}: {collection['count']} documents")

        # Start chromadb server
        cmd = [
            "chroma",
            "run",
            "--host", host,
            "--port", str(port),
            "--path", os.getenv("DB_PATH", "./chroma_db")
        ]
        subprocess.Popen(cmd)