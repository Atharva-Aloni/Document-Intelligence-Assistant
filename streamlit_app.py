import streamlit as st
import requests
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()
BACKEND_URL = "http://127.0.0.1:8000"

# Set page config
st.set_page_config(page_title="📄 Document Intelligence Assistant", layout="wide", page_icon="📄")

# --- Custom Styling ---
st.markdown("""
    <style>
    .main, .stApp {
        background-color: #e3f2fd;
        color: #000000;
    }
    .stMarkdown, .stText, .stCaption, .stSubheader, .stTitle, .stHeader, .stExpander, .uploadedFileName, .chunk {
        color: #000000 !important;
    }
    .stButton>button {
        background-color: #4dabf7;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.6em 1.2em;
        border: none;
        margin-top: 10px;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #2196f3;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff;
        color: #000000 !important;
        border-radius: 6px;
        padding: 10px;
        border: 1px solid #90caf9;
    }
    .stFileUploader>div>div>div>input {
        background-color: #ffffff;
        padding: 10px;
        border: 1px solid #90caf9;
        border-radius: 6px;
    }
    .uploadedFileName {
        color: #1976d2;
        font-weight: 600;
    }
    .chunk {
        background-color: #ffffff;
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 6px;
        border: 1px solid #bbdefb;
        box-shadow: 0 2px 4px rgba(33, 150, 243, 0.15);
    }
    section[data-testid="stSidebar"] {
        background-color: #e3f2fd !important;
        color: #000000 !important;
        border-right: 1px solid #bbdefb;
    }
    section[data-testid="stSidebar"] button {
        background-color: #000000 !important;
        color: #ffffff !important;
    }
    .stTextInput label {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title & Caption ---
st.title("📄 Document Intelligence Assistant")
st.caption("Interact with your documents using RAG + Groq LLM 🔍")

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ System Information")
    st.markdown("- **Backend:** FastAPI")
    st.markdown("- **Vector Store:** FAISS")
    st.markdown(f"- **LLM Model:** `{os.getenv('GROQ_MODEL', 'groq/mixtral')}`")
    st.markdown("---")

# --- Upload Document ---
st.subheader("📤 Upload a Document")
st.markdown("Supported formats: `.pdf`, `.docx`, `.txt`")

uploaded_file = st.file_uploader("Choose a file to upload", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    with st.container():
        st.markdown(f"<div class='uploadedFileName'>📎 Selected File: {uploaded_file.name}</div>", unsafe_allow_html=True)

    if st.button("🚀 Upload & Embed"):
        with st.spinner("Uploading and processing your document..."):
            try:
                files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                response = requests.post(f"{BACKEND_URL}/upload", files=files)

                if response.status_code == 200:
                    st.success(f"✅ `{uploaded_file.name}` uploaded and indexed successfully.")
                    with st.expander("📑 Document Metadata"):
                        st.json(response.json())
                else:
                    st.error("❌ Upload failed. Please check backend logs.")
                    st.text(response.text)
            except Exception as e:
                st.error(f"❌ Connection error during upload:\n\n{e}")

# --- Ask a Question ---
st.subheader("💬 Ask a Question")
st.markdown("Ask anything related to your uploaded document.")

query = st.text_input("Type your question here", placeholder="e.g., What are the skills mentioned in the resume?", label_visibility="visible")

if st.button("🤖 Get Response") and query:
    with st.spinner("Generating response..."):
        try:
            response = requests.post(f"{BACKEND_URL}/chat", json={"query": query})
            if response.status_code == 200:
                data = response.json()
                st.markdown("### 📬 Response from Assistant")
                st.markdown(f"<div style='color: black; font-weight: 500; font-size: 16px;'>{data.get('answer', 'No answer returned.')}</div>", unsafe_allow_html=True)

                with st.expander("📚 Retrieved Chunks"):
                    for i, chunk in enumerate(data.get("context_chunks", [])):
                        st.markdown(f"<div class='chunk'><strong>Chunk {i+1}:</strong><br>{chunk}</div>", unsafe_allow_html=True)
            else:
                st.error("❌ Query failed. Check backend logs.")
                st.text(response.text)
        except Exception as e:
            st.error(f"❌ Connection error during chat:\n\n{e}")
