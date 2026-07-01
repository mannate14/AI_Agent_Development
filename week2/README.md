# 📚 Week 2 - RAG Study Buddy

## Overview

This project extends the Week 1 Study Buddy by introducing **Retrieval-Augmented Generation (RAG)**.

Instead of relying only on the LLM's general knowledge, the application retrieves relevant information from a local knowledge base before generating an answer. This allows the chatbot to answer questions based specifically on the user's own notes.

---

## Features

- Load notes from Markdown files
- Split large documents into chunks
- Generate embeddings using Sentence Transformers
- Store embeddings in a FAISS vector database
- Retrieve the most relevant note chunks
- Generate context-aware answers using Google Gemini
- Command-line chatbot interface

---

## Project Structure

```
week2/
│
├── README.md
├── my_notes.md
└── study_buddy_rag.py
```

---

## Technologies Used

- Python
- LangChain
- Google Gemini
- Sentence Transformers
- FAISS
- python-dotenv

---

## Workflow

```
User Question
      │
      ▼
Convert question to embedding
      │
      ▼
Search similar chunks in FAISS
      │
      ▼
Retrieve relevant context
      │
      ▼
Combine Context + Question
      │
      ▼
Send Prompt to Gemini
      │
      ▼
Generate Final Answer
```

---

## Example

### Question

```
What should a good introduction include?
```

### Retrieved Context

```
A good introduction should cover:

- Name
- College
- Branch
- Skills
- Projects
```

### Final Response

```
A good interview introduction should briefly mention your name,
college, branch, technical skills, projects, and career interests.
```

---

## Key Learning Outcomes

During this project, I learned:

- Fundamentals of Retrieval-Augmented Generation (RAG)
- Vector embeddings
- Semantic search
- FAISS vector database
- Prompt engineering
- Context-aware LLM responses
- LangChain workflow

---

## Future Improvements

- PDF support
- Multiple document indexing
- Chat history memory
- Streamlit web interface
- Source citations
- Hybrid search (Keyword + Semantic Search)

---

## Author

**Mannate Jain**

NIT Silchar

Learning AI Agent Development 🚀
