import logging
from dotenv import load_dotenv
from database.client import ChromaDBService

load_dotenv()

logging.basicConfig(filename='chromadb-service.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def main():
    """
    Starts the ChromaDB server to access the DB
    """
    chromadb_service = ChromaDBService()
    chromadb_service.run(host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()