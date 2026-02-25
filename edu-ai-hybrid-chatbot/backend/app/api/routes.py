from fastapi import APIRouter, HTTPException
from services.llm_orchestrator import ask_llm
from services.security import detect_prompt_injection
from services.logger import log_chat
from services.monitor import system_stats
from config import MAX_INPUT_CHARS

router = APIRouter()

@router.post("/chat")
async def chat(query: str):
    if len(query) > MAX_INPUT_CHARS:
        raise HTTPException(413, "Input too long")

    if detect_prompt_injection(query):
        raise HTTPException(400, "Prompt injection detected")

    answer = ask_llm(query)
    log_chat(query, answer)
    return {"answer": answer}

@router.get("/admin/stats")
def stats():
    return system_stats()