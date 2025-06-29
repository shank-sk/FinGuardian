# 🛡️ FinGuardian – Your AI Co-Pilot for Financial Protection & Risk Intelligence

FinGuardian is a Streamlit-based AI application that helps users **analyze insurance policies**, **detect scams**, **generate personalized financial risk profiles**, and **learn financial concepts interactively**.

---

## 🚀 Features

- 📄 **Policy Analyzer** – Upload an insurance policy and get a summary with risky clauses flagged using LLMs.
- 🚨 **Scam Detector** – Scan suspicious messages or SMSes to identify potential scams using GenAI.
- 📈 **Risk Profile Generator** – Calculate and visualize your financial risk score dynamically.
- 🎓 **Financial Tutor** – Ask questions about finance and get AI-generated beginner-friendly answers.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit with custom UI/UX enhancements
- **LLMs**: Local inference (`llama-cpp` with Mistral-7B), or OpenRouter API for faster GenAI
- **Visualization**: Matplotlib & Plotly
- **Deployment**: Compatible with Streamlit Cloud, Render, or local hosting

---

## ⚙️ Installation

```bash
# 1. Clone the repo
git clone https://github.com/your-username/finguardian.git
cd finguardian

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate  # on Windows
# or
source venv/bin/activate  # on Linux/macOS

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
