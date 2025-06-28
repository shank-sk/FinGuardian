from utils.pdf_utils import read_pdf
from utils.openrouter_handler import call_openrouter

def extract_text(uploaded_file):
    return read_pdf(uploaded_file)

def analyze_policy(policy_text):
    prompt = f"You're a policy analyst. Summarize and flag any risky clauses from this policy text:\n\n{policy_text}"
    return call_openrouter(prompt)
