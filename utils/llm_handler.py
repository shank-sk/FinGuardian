from llama_cpp import Llama

# Load the local quantized model
llm = Llama(
    model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=4  # Optional: adjust based on your CPU
)

def call_llm(prompt: str, max_tokens=300):
    try:
        response = llm(prompt=prompt, max_tokens=max_tokens, stop=["</s>", "###"])
        return response["choices"][0]["text"].strip()
    except Exception as e:
        return f"LLM Error: {e}"
