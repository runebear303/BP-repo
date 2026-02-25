import requests

def ask_local(prompt):
    res = requests.post(
        "http://ollama:11434/api/generate",
        json={"model": "phi3", "prompt": prompt}
    )
    return res.json()["response"]