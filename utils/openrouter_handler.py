import requests
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Get the API key securely from environment
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

def call_openrouter(prompt, model="mistralai/mistral-7b-instruct"):
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You're a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(BASE_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error contacting OpenRouter API: {e}"


