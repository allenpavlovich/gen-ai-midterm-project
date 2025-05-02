# 🎓 UChicago MS in Applied Data Science – RAG Chatbot

This project implements a **Retrieval-Augmented Generation (RAG)** chatbot designed to answer questions about the University of Chicago's MS in Applied Data Science program using **LangGraph** and **LangChain**.

---

## 🚀 Project Overview

- Retrieves structured information from the [official UChicago MS in Applied Data Science website](https://datascience.uchicago.edu/education/masters-programs/ms-in-applied-data-science/)
- Converts webpage data into structured Markdown
- Generates semantic embeddings for efficient retrieval
- Provides an interactive conversational QA interface
- Offers a friendly frontend (Streamlit/Gradio)
- Ready for containerized deployment (Docker/GCP)

---

## 📁 Project Structure

```plaintext
uchicago-rag-chatbot/
├── data/
│   ├── raw/                  # Raw scraped HTML
│   ├── markdown/             # Converted Markdown files
│   └── chunks/               # Final Markdown chunks
├── embeddings/
│   └── vectors/              # Optional: embedding storage
├── notebooks/
│   └── exploratory.ipynb     # Prototyping notebook
├── src/
│   ├── scraping/
│   │   └── scrape.py
│   ├── preprocessing/
│   │   └── preprocess.py
│   ├── embeddings/
│   │   └── embed.py
│   ├── rag_app/
│   │   ├── app.py
│   │   └── retriever.py
│   └── frontend/
│       └── streamlit_app.py
├── tests/
│   ├── test_scraping.py
│   ├── test_preprocessing.py
│   └── test_embeddings.py
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md (you are here)
