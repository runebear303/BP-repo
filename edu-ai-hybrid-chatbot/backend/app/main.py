from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Edu AI Hybrid Chatbot")

app.include_router(router, prefix="/api")

@app.get("/")
def health():
    return {"status": "running"}


  

