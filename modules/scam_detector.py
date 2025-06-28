from utils.llm_handler import call_llm

def detect_scam(message: str) -> str:
    prompt = f"""
You're a financial security analyst. Analyze the following message for signs of fraud or scam:

Message:
\"\"\"{message}\"\"\"

If it's a scam, explain **why**, citing patterns like urgency, personal info requests, fake rewards, etc. Also give suggestions on what to do next.

Label: Scam or Not
"""
    return call_llm(prompt)
