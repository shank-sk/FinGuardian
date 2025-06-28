from utils.openrouter_handler import call_openrouter

def detect_scam(text):
    prompt = f"Analyze the following message and determine if it's a scam. Explain why and what law it may violate:\n\n{text}"
    return call_openrouter(prompt)
