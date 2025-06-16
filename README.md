# Document-Intelligence-Assistant
- A powerful RAG-based (Retrieval-Augmented Generation) assistant that allows you to upload .pdf, .docx, or .txt documents and interact with them using natural language queries.

🚀 Features
- Upload and parse documents (PDF, DOCX, TXT)
- Extract, chunk, and embed text using HuggingFace models
- Store and retrieve embeddings using FAISS
- Ask contextual questions about uploaded documents
- Clean, modern Streamlit interface with light theme
- FastAPI backend for scalable document processing
- Built with FastAPI, Streamlit, FAISS vector store, HuggingFace embeddings, and a Groq LLM.

🧱 Tech Stack
Layer              Technology
Frontend           Streamlit (Custom UI)
Backend            FastAPI
Embeddings         HuggingFace (MiniLM)
Vector Store       FAISS
LLM                Groq (Mixtral, or similar)
File Parsing       PyMuPDF, python-docx
