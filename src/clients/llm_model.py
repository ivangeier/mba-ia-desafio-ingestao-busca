import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_MODEL = os.getenv("GOOGLE_MODEL", "gemini-2.5-flash-lite")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5-nano")


def get_llm_model():
    """
    Returns the language model automatically configured according to environment variables.
    Prioritizes Google if both keys are present.
    """
    if GOOGLE_API_KEY:
        try:
            return ChatGoogleGenerativeAI(model=GOOGLE_MODEL)
        except Exception as e:
            raise RuntimeError(f"Error initializing Google model: {e}")
    elif OPENAI_API_KEY:
        try:
            return ChatOpenAI(model=OPENAI_MODEL)
        except Exception as e:
            raise RuntimeError(f"Error initializing OpenAI model: {e}")
    else:
        raise ValueError("Set the GOOGLE_API_KEY or OPENAI_API_KEY environment variable.")
