# GenAI_Resume_Summary_Bot
This script allows users to upload resumes (PDFs) and ask questions about them using a small LLM. Uses HuggingFace + LangChain + RAG 


Resume Summary Bot

A conversational AI app that lets you upload a resume (PDF) and ask natural language questions like:
- What are this candidate's Python skills ?
- Summarize their experience with AWS ?
- Do they have any management experience ?

Built using:
- LangChain for LLM Orchestration
- Hugging Face Falcon-RW-1B for text generation
- FAISS or vector based document retrieval
- Streamlit for UI


Features:
- Upload any resume in PDF format
- Ask contextual questions about the candidate's experience
- Answers are generated using Retrieval-Augmented Generation (RAG)
- View source snippets used by the model to support transparency



# How to run
1. Install dependencies
  pip install -r requirements.txt
2. Add .env file
  If using private models or HF inference API:
 HF_TOKEN=Huggingface_Token
3. Start streamlit app
  streamlit run app/main.py


# How it works

1. uploads a PDF resume
2. Chunks the resume using LangChain's textsplitter
3. Embeds the chunks using Hugging Face embeddings
4. Stores chunks in FAISS for fast vector-based retrieval
5. Uses RAG pipeline to retrieve relevant chunks and pass them to LLM
6. Displays grounded, contextual answers with source snippets


# Sample questions to ask
- What projects has this candidate worked on ?
- Are they familiar with SQL ?
- Do they have experience with cloud platforms ?
- What kind of roles they have held ?



