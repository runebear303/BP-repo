import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def ask_cloud(prompt):
    res = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}]
    )
    return res.choices[0].message.content