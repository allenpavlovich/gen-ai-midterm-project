🎓 UChicago MS in Applied Data Science – RAG Chatbot
This project is a Retrieval-Augmented Generation (RAG) chatbot designed to answer detailed questions about the University of Chicago’s MS in Applied Data Science program using LangGraph and LangChain.

📌 Project Overview
The chatbot:

Retrieves and organizes structured information from the official UChicago MS in Applied Data Science website.

Converts web data to structured Markdown format.

Generates semantic embeddings from structured content.

Implements a conversational QA pipeline (RAG) using LangGraph and LangChain.

Provides a user-friendly frontend (Streamlit or Gradio).

Is prepared for future deployment on Google Cloud Platform (GCP).

🚀 Folder Structure
graphql
Copy
Edit
uchicago-rag-chatbot/
│
├── data/
│   ├── raw/                  # Scraped raw HTML data
│   ├── markdown/             # Markdown-converted content
│   └── chunks/               # Markdown chunks prepared for embedding
│
├── embeddings/
│   └── vectors/              # Optional local embedding storage
│
├── notebooks/
│   └── exploratory.ipynb     # Jupyter notebook for experiments/prototyping
│
├── src/
│   ├── scraping/
│   │   └── scrape.py         # Web scraping (requests + beautifulsoup4)
│   ├── preprocessing/
│   │   └── preprocess.py     # Convert HTML to Markdown and chunk text
│   ├── embeddings/
│   │   └── embed.py          # Embeddings generation (OpenAI/Sentence Transformers)
│   ├── rag_app/
│   │   ├── app.py            # LangGraph/LangChain RAG pipeline
│   │   └── retriever.py      # Retriever logic (ChromaDB/Qdrant)
│   └── frontend/
│       └── streamlit_app.py  # Frontend interface (Streamlit or Gradio)
│
├── tests/                    # Optional (recommended): Unit tests
│   ├── test_scraping.py
│   ├── test_preprocessing.py
│   └── test_embeddings.py
│
├── Dockerfile                # Containerization for deployment (GCP Cloud Run)
├── requirements.txt          # Python dependencies
├── .gitignore                # Ignored files for clean Git commits
└── README.md                 # (You are here) Documentation & Setup Guide
✅ Quick Start (Local Setup)
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/<your_username>/uchicago-rag-chatbot.git
cd uchicago-rag-chatbot
(Replace <your_username> with your GitHub username.)

2. Set up Python Environment (named ragchat)
Windows (VS Code Terminal):

bash
Copy
Edit
py -m venv ragchat
.\ragchat\Scripts\activate
Mac/Linux (VS Code Terminal):

bash
Copy
Edit
python3 -m venv ragchat
source ragchat/bin/activate
3. Install Required Libraries
Install Python libraries clearly from requirements.txt:

bash
Copy
Edit
pip install -r requirements.txt
4. Setup Jupyter Notebook Kernel (optional, for notebooks)
bash
Copy
Edit
pip install ipykernel
python -m ipykernel install --user --name=ragchat
Then select the "ragchat" kernel in Jupyter/VS Code notebook.

⚙️ Dependencies
These are automatically handled by installing from requirements.txt, but listed here clearly for clarity:

Core Libraries:

langchain

langgraph

openai

sentence-transformers

Vector Store (choose clearly):

chromadb (simple, recommended initially)
or

qdrant-client (robust, for larger production deployments)

Data Extraction & Preprocessing:

requests

beautifulsoup4

markdownify

Frontend & Visualization:

streamlit

gradio

Environment & API Key Management:

python-dotenv

Notebook Kernel (optional for notebook users):

ipykernel