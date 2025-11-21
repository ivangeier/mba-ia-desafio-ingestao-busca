"""
Script para ingestão de PDF no banco de dados vetorial.
Organizado conforme PEP8, com tratamento de erros e mensagens claras.
"""

import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.clients.pgvector import vector_store

load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")


def ingest_pdf():
    """
    Realiza a ingestão de um PDF, dividindo em chunks e salvando no banco vetorial.
    """
    print("Starting ingestion...")
    if not PDF_PATH:
        print("PDF_PATH not defined in environment.")
        return
    try:
        loader = PyPDFLoader(PDF_PATH)
        docs = loader.load()
        print(f"Loaded {len(docs)} documents.")
    except Exception as e:
        print(f"Erro ao carregar PDF: {e}")
        return

    print("Chunking documents...")
    try:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
        all_chunks = text_splitter.split_documents(docs)
        print(f"Created {len(all_chunks)} chunks.")
    except Exception as e:
        print(f"Erro ao dividir documentos: {e}")
        return

    print("Saving chunks to database...")
    try:
        docs_ids = vector_store.add_documents(all_chunks)
        print(f"Saved {len(docs_ids)} chunks to database.")
        print("PDF ingestion completed. You can now start the chat!")
    except Exception as e:
        print(f"Error while saving chunks on database: {e}")


if __name__ == "__main__":
    ingest_pdf()