from utils.openrouter_handler import call_openrouter

def call_tutor(topic, level):
    prompt = f"Act as a financial tutor for a {level} learner. Explain this topic simply:\n\n{topic}"
    return call_openrouter(prompt)
