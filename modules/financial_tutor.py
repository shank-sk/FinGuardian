# modules/financial_tutor.py

from llama_cpp import Llama

# Load your local LLaMA or Mistral model (quantized `.gguf`)
llm = Llama(model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf", n_ctx=2048)

def call_tutor(topic, level):
    prompt = f"""You're a financial tutor. Explain the following topic to a {level.lower()} user in simple terms:

Topic: {topic}

Answer:"""

    output = llm(prompt=prompt, max_tokens=300)
    return output["choices"][0]["text"].strip()
