import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data/faiss_index"
DOCS_DIR = BASE_DIR / "data/source_docs"

DATA_DIR.mkdir(parents=True, exist_ok=True)

# Load model (small for 8GB RAM)
model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
texts = []

# Simple text loader
def load_documents():
    for file in DOCS_DIR.glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()

        # Chunking (important!)
        chunks = [text[i:i+500] for i in range(0, len(text), 500)]

        for i, chunk in enumerate(chunks):
            documents.append({
                "text": chunk,
                "source": file.name,
                "chunk_id": i
            })
            texts.append(chunk)

# Load docs
load_documents()

# Create embeddings
embeddings = model.encode(texts, show_progress_bar=True)

# FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Save index + metadata
faiss.write_index(index, str(DATA_DIR / "index.faiss"))
with open(DATA_DIR / "docs.pkl", "wb") as f:
    pickle.dump(documents, f)

print(f"FAISS index built with {len(texts)} chunks")
print("Saved to:", DATA_DIR)