import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import pdfplumber
import os

load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_API_KEY']=OPENAI_API_KEY

def get_pdf_text(pdf_docs):
    all_text = ""
    for pdf in pdf_docs:
        with pdfplumber.open(pdf) as pdf_file:
            for page in pdf_file.pages:
                text = page.extract_text()
                if text:
                    all_text += text
    return all_text if all_text.strip() else None


def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_embeddings(text_chunks):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vector_store


def get_conversational_chain(vector_store):
  llm = ChatOpenAI(temperature=0)
  memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
  conversational_chain = ConversationalRetrievalChain.from_llm(
      llm=llm,
      retriever=vector_store.as_retriever(),
      memory=memory
  )
  return conversational_chain