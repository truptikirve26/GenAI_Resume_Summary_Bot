# main.py --- Streamlit UI for Resume Summary Bot

import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from model_utils import load_llm


# load env variables from .env
load_dotenv()

# Streamlit app configuration
st.set_page_config(page_title="Resume Summary Bot")
st.title("Resume Summary Bot")
st.markdown("Upload a Resume (PDF) and ask questions like \"What are this candidate's Python skills ?\" or \"Summarize their experience with AWS.\"")


#load the LLM pipeline (Falcon via HuggingFace wrapped in Langchain
llm = load_llm()

# File uploader UI in streamlit
uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

# Once the file is uploaded, begin processing
if uploaded_file:
    # save uploaded file temporarily
    with open("resume_temp.pdf","wb") as f:
        f.write(uploaded_file.read())


    # load and parse the pdf doc
    loader = PyPDFLoader("resume_temp.pdf")
    pages = loader.load()


    # split the document into chunks suitable for semantic search
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = splitter.split_documents(pages)

    #Generate vector embeddings for the document chunks
    embeddings = HuggingFaceEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings) # FAISS index created in memory
    retriever = vectorstore.as_retriever() # Langchain compatible retriever

    # Create a Retrieval AUgmented QA chain using the model and retriever
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True  #Include document sources in the response
    )

    #Prompt input from user
    query = st.text_input("Ask something about the resume:")

    #If user asks the question, run the QA chain
    if query:
        result = qa_chain(query)

        #display the answer
        st.subheader("Answer")
        st.write(result['result'])

        #show source snippets from the resume used to generate the answer
        st.subheader("Source Snippets")
        for doc in result['source_documents']:
            st.caption(doc.page_content[:300])



