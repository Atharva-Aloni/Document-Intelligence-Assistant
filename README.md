# Document-Intelligence-Assistant
📄 Document Intelligence AssistantA powerful RAG-based (Retrieval-Augmented Generation) assistant that allows you to upload .pdf, .docx, or .txt documents and interact with them using natural language queries. Built with FastAPI, Streamlit, FAISS vector store, HuggingFace embeddings, and a Groq LLM.
🚀 FeaturesUpload and parse documents (PDF, DOCX, TXT)
Extract, chunk, and embed text using HuggingFace models
Store and retrieve embeddings using FAISS
Ask contextual questions about uploaded documents
Clean, modern Streamlit interface with light theme
FastAPI backend for scalable document processing
🧱 Tech StackLayerTechnologyFrontendStreamlit (Custom UI)BackendFastAPIEmbeddingsHuggingFace (MiniLM)Vector StoreFAISSLLMGroq (Mixtral, or similar)File ParsingPyMuPDF, python-docx📂 Project StructureDocument_Intelligence/
├── app.py                  # Streamlit frontend
├── main.py                 # FastAPI backend
├── requirements.txt        # Dependencies
├── .env                    # Environment variables
├── uploads/                # Uploaded files
├── faiss_index/            # Local vector DB
└── README.md               # Project overview⚙️ Setup Instructions1. Clone the Repositorygit clone https://github.com/your-username/document-intelligence-assistant.git
cd document-intelligence-assistant2. Create and Activate Virtual Environmentpython -m venv .venv
.venv\Scripts\activate  # On Windows3. Install Requirementspip install -r requirements.txt4. Set Environment VariablesCreate a .env file:
GROQ_API_KEY=your-groq-key
GROQ_MODEL=mixtral-8x7b-327685. Run Backend (FastAPI)uvicorn main:app --reload6. Run Frontend (Streamlit)streamlit run app.py📬 API EndpointsMethodEndpointDescriptionPOST/uploadUpload and embed documentPOST/chatAsk questions on the content📌 Sample Query"What are my technical skills mentioned in the resume?"
👨‍💻 AuthorDeveloped by Aayush 🚀Modified and styled by Atharva Aloni ✨
📝 LicenseMIT License. Feel free to use and contribute!
💡 Future EnhancementsAdd support for Gemini, OpenRouter, and Claude
Add document summarization feature
Support for multi-document search
Export answers with sources to PDF/JSON
