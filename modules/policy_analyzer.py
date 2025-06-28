from utils.pdf_utils import read_pdf
from utils.llm_handler import call_llm

def extract_text(uploaded_file):
    return read_pdf(uploaded_file)

def analyze_policy(text):
    prompt = f"""You're a policy analyst. Summarize and flag any risky clauses from this policy text:\n\n{text}\n\nSummary:"""
    return call_llm(prompt)
