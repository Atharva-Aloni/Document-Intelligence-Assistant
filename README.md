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
- Layer              Technology
- Frontend           Streamlit (Custom UI)
- Backend            FastAPI
- Embeddings         HuggingFace (MiniLM)
- Vector Store       FAISS
- LLM                Groq (Mixtral, or similar)
- File Parsing       PyMuPDF, python-docx

📂 Project Structure

![Screenshot 2025-06-16 151102](https://github.com/user-attachments/assets/1f6fab3b-49c6-4821-a5c2-e05aec061129)

⚙️ Setup Instructions

1. Clone the Repository
- cmd : git clone https://github.com/your-username/document-intelligence-assistant.git
- cd document-intelligence-assistant

2. Create and Activate Virtual Environment
- cmd : python -m venv .venv
- activation command : .venv\Scripts\activate

3. Install Requirements
- cmd : pip install -r requirements.txt

4. Set Environment Variables
create .env file and mention the below content in it :-
- GROQ_API_KEY=your-groq-key
- GROQ_BASE_URL=https://api.groq.com/openai/v1
- GROQ_MODEL=llama3-8b-8192

 5.Run Backend (FastAPI) 
- cmd : uvicorn main:app --reload

6. Run Frontend (Streamlit)
- cmd : streamlit run app.py
