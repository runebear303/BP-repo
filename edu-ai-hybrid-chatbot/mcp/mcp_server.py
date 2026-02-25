from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Education MCP Tool Server")

COURSES = ["Software Engineering", "AI", "Cyber Security"]
POLICY = "No plagiarism allowed. Follow academic integrity rules."

@app.get("/")
def health():
    return {"status": "MCP running"}

# MCP Tool 1
@app.post("/tool/courses")
def get_courses():
    logging.info("MCP tool called: courses")
    return {"courses": COURSES}

# MCP Tool 2
@app.post("/tool/policy")
def get_policy():
    logging.info("MCP tool called: policy")
    return {"policy": POLICY}

# MCP Tool 3
@app.post("/tool/faq")
def faq(question: str):
    logging.info(f"MCP FAQ question: {question}")
    if "plagiaat" in question.lower():
        return {"answer": POLICY}
    if "opleiding" in question.lower():
        return {"answer": "UNASAT Software Engineering opleiding."}
    return {"answer": "Geen antwoord gevonden in MCP knowledge base."}

