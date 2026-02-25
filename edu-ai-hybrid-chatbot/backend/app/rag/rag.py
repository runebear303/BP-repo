import faiss
import pickle
from sentence_transformers import SentenceTransformer
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
FAISS_PATH = BASE_DIR / "data/faiss_index"

_model = None
def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model

if not (FAISS_PATH / "index.faiss").exists():
    raise RuntimeError("FAISS index niet gevonden. Run build_index.py.")

index = faiss.read_index(str(FAISS_PATH / "index.faiss"))

with open(FAISS_PATH / "docs.pkl", "rb") as f:
    documents = pickle.load(f)

def sanitize_query(q: str):
    blacklist = [
        "system:", "ignore instructions", "jailbreak", 
        "developer mode", "role:",
        "negeer instructies", "systeem prompt", "omzeil"
    ]
    for b in blacklist:
        q = q.replace(b, "")
    return q[:500]

def search_docs(query: str, k=3):
    query = sanitize_query(query)
    model = get_model()
    emb = model.encode([query])

    D, I = index.search(emb, k)
    results = []

    for score, idx in zip(D[0], I[0]):
        doc = documents[idx]
        doc["score"] = float(score)
        results.append(doc)

    return results