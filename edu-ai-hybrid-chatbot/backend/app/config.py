import os

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")  # ollama | openai
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

MAX_INPUT_CHARS = 2000
DB_PATH = "data/chat_logs.db"
FAISS_PATH = "data/faiss_index/index.faiss"