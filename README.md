# 🟦 ChromaDB Service

This repository contains the setup and configuration for running the **ChromaDB vector database** locally.  
It acts as the backbone of the system, storing all document embeddings that are later used by the **Document Ingestion** pipeline and the **Reporter** multi-agent system.

<br>

## 🚀 Features
- Local setup of **ChromaDB**.
- Persistent vector storage for documents and embeddings.
- Provides the data layer for ingestion and report generation.

<br>

## 📦 Installation & Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/your-org/chromadb.git
   cd chromadb
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run ChromaDB locally:

   ```bash
   python main.py
   ```

<br>

# 🔗 Related Repositories
- [document-ingestion](https://github.com/JuaniLlaberia/document-ingestion) → Extracts and ingests documents into ChromaDB.
- [reporter](https://github.com/JuaniLlaberia/reporter) → Uses ChromaDB data for multi-agent report generation.

<br>

# 📌 Coming Soon
- Cloud-ready deployment of ChromaDB.
- User Interface for using the application (Chat-like UI)
