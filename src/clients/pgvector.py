"""
Module for automatic configuration of the embedding client and Postgres vector store.
"""

import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_EMBEDDING_MODEL = os.getenv("GOOGLE_EMBEDDING_MODEL")
OPENAI_EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL")
PG_VECTOR_COLLECTION_NAME = os.getenv("PG_VECTOR_COLLECTION_NAME")
DATABASE_URL = os.getenv("DATABASE_URL")


def get_embedding():
    """
    Returns the embedding client automatically configured according to environment variables.
    Prioritizes Google if both keys are present.
    """
    if GOOGLE_API_KEY and GOOGLE_EMBEDDING_MODEL:
        try:
            return GoogleGenerativeAIEmbeddings(model=GOOGLE_EMBEDDING_MODEL)
        except Exception as e:
            raise RuntimeError(f"Error initializing Google embeddings: {e}")
    elif OPENAI_API_KEY and OPENAI_EMBEDDING_MODEL:
        try:
            return OpenAIEmbeddings(model=OPENAI_EMBEDDING_MODEL)
        except Exception as e:
            raise RuntimeError(f"Error initializing OpenAI embeddings: {e}")
    else:
        raise ValueError("Set the embedding and API_KEY environment variables for Google or OpenAI.")


embedding = get_embedding()

vector_store = PGVector(
    embeddings=embedding,
    collection_name=PG_VECTOR_COLLECTION_NAME,
    connection=DATABASE_URL
)


def get_vector_store():
    """
    Returns the configured vector store.
    """
    return vector_store