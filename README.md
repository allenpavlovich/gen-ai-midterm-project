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
│   ├── raw/                   # Raw scraped HTML
│   ├── markdown/              # Converted Markdown files
├── embeddings/
│   └── vectors/               # Optional: embedding storage
├── notebooks/
│   ├── exploratory.ipynb      # Prototyping notebook
│   ├── uchicago_scraper.ipynb # Converted Markdown files
├── src/
│   ├── scraping/
│   │   └── scrape.py          # Optional: could be all .ipynb maybe
│   ├── preprocessing/
│   │   └── preprocess.py      # Optional: could be all .ipynb maybe
│   ├── embeddings/
│   │   └── embed.py           # Optional: could be all .ipynb maybe
│   ├── rag_app/
│   │   ├── app.py             # Optional: could be all .ipynb maybe
│   │   └── retriever.py       # Optional: could be all .ipynb maybe
│   └── frontend/
│       └── streamlit_app.py   # Optional: could be all .ipynb maybe
├── tests/
│   ├── test_scraping.py       # Optional: could remove later
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
