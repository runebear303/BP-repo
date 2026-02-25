from app.rag.rag import search_docs
from app.services.llm_local import ask_local
from app.services.security import sanitize_prompt

def ask_ai_with_sources(vraag: str):
    # Security filter
    vraag = sanitize_prompt(vraag)

    # Zoek relevante documenten
    docs = search_docs(vraag, k=3)

    # Context bouwen
    context = "\n".join([d["text"] for d in docs])

    prompt = f"""
Je bent een academische FAQ-chatbot voor studenten van UNASAT.
Gebruik ALLEEN de onderstaande context om te antwoorden.
Als het antwoord niet in de context staat, zeg: 
"Dit staat niet in de studentenhandleiding of het orde reglement."

Context:
{context}

Vraag: {vraag}

Antwoord in correct en duidelijk Nederlands.
"""

    antwoord = ask_local(prompt, max_tokens=500)

    return {
        "answer": antwoord,
        "sources": docs
    }