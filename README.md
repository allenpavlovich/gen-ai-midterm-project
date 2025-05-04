# 🎓 UChicago MS in Applied Data Science – RAG Chatbot

# UChicago MS in Applied Data Science - RAG Chatbot Project

This project implements a **Retrieval-Augmented Generation (RAG)** chatbot designed to answer questions about the University of Chicago's MS in Applied Data Science program by leveraging web content, vector embeddings, and LLM integration.

---

## 🚀 Project Overview

- Extracts comprehensive information from the entire [UChicago Data Science Institute website](https://datascience.uchicago.edu/)
- Uses a two-phase approach: link discovery followed by content processing
- Converts webpage data into structured Markdown files with metadata
- Will generate semantic embeddings for efficient retrieval
- Aims to provide an interactive conversational QA interface

---

## 📁 Project Structure

```plaintext
gen-ai-midterm-project/
├── data/
│   ├── discovered_links.json   # Links discovered during crawling phase
│   ├── processed_links.json    # Status tracking of content processing
│   ├── markdown/               # Converted Markdown files
│   ├── category_summary.csv    # Summary of content by category
│   └── word_count_summary.csv  # Analysis of content length
├── logs/
│   └── .gitkeep                # Directory for logging output
├── notebooks/
│   ├── link_discovery.ipynb    # Phase 1: Web crawling to identify content
│   └── content_processor.ipynb # Phase 2: Content extraction and conversion
├── requirements.txt            # Project dependencies
├── .gitignore                  # Git exclusion rules
└── README.md                   # Project documentation
```

## 📊 Project Phases

### Phase 1: Link Discovery ✅
- Comprehensive crawling of the datascience.uchicago.edu domain
- Intelligent filtering of relevant content
- Storage of discovered links for subsequent processing

### Phase 2: Content Processing ✅
- Extraction of content from discovered links
- Conversion to structured Markdown format
- Metadata addition (title, URL, category, date)
- Basic content analysis (word count, category distribution)

### Phase 3: Data Cleanup 🔄
- Removal of boilerplate content (navigation, share buttons)
- Text normalization
- Handling of special characters and formatting
- Deduplication of similar content

### Phase 4: Vector Embedding (Pending)
- Chunking strategy implementation
- Embedding generation
- Integration with vector database

### Phase 5: RAG Implementation (Pending)
- Retrieval component development using vector similarity search
- Agent-based implementation with **LangGraph** for complex reasoning
- Generation component integration with LLM
- Conversational interface with memory and state tracking

---

## 🛠️ Setup and Usage

### Prerequisites
- Python 3.8+ installed on your system
- Git installed on your system
- Jupyter environment (Jupyter Lab or Notebook)

### Installation

**Windows:**
```powershell
# Clone the repository
git clone <repository-url>
cd gen-ai-midterm-project

# Create and activate virtual environment (optional but recommended)
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**macOS/Linux:**
```bash
# Clone the repository
git clone <repository-url>
cd gen-ai-midterm-project

# Create and activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Project (already done, no need to repeat)

1. Launch Jupyter Lab/Notebook:
   ```
   jupyter lab
   # or
   jupyter notebook
   ```

2. Run notebooks in sequence:
   - First run `notebooks/link_discovery.ipynb` to collect all website links
   - Then run `notebooks/content_processor.ipynb` to extract and process content

### Project Output

After running the notebooks, you'll find:
- Processed markdown files in the `data/markdown/` directory
- Analysis files in the `data/` directory
- Log files in the `logs/` directory

---
