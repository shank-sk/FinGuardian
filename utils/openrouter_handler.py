import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://github.com/shank-sk/FinGuardian",  # ✅ Your GitHub repo URL
    "X-Title": "FinGuardian"
}

BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

def call_openrouter(prompt, model="mistralai/mistral-7b-instruct"):
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(BASE_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error contacting OpenRouter API: {e}"
