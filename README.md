# 🛡️ FinGuardian – Your AI Co-Pilot for Financial Protection & Risk Intelligence

>FinGuardian is a Streamlit-based AI application that helps users **analyze insurance policies**, **detect scams**, **generate personalized financial risk profiles**, and **learn financial concepts interactively**.

---

## 🚀 Key Features

- 📄 **Policy Analyzer** – Upload an insurance policy and get a summary with risky clauses flagged using LLMs.
- 🚨 **Scam Detector** – Scan suspicious messages or SMSes to identify potential scams using GenAI.
- 📈 **Risk Profile Generator** – Calculate and visualize your financial risk score dynamically.
- 🎓 **Financial Tutor** – Ask questions about finance and get AI-generated beginner-friendly answers.

---

## 🧱 System Architecture

FinGuardian follows a modular, layered architecture combining GenAI capabilities with financial domain logic:

1.  **PDF/Text Processing**:Parses uploaded insurance policies, cleans text, and extracts clause-level information.
2.  **LLM Integration**:Uses OpenRouter API to summarize policy clauses,detect scam patterns in user messages and explain finance concepts conversationally
3.  **Risk Calculation & Visualization**: A structured questionnaire captures user inputs to compute a financial risk score, which is visualized using Matplotlib and Plotly charts.
4.  **Utility Layer**:Handles API interactions, model routing, and formatting logic for consistent response parsing and LLM communication.
5.  **Streamlit Interface**: Provides an intuitive web-based user experience

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
```

# 2. Create a virtual environment (optional)
```bash
python -m venv venv
venv\Scripts\activate  # on Windows
# or
source venv/bin/activate  # on Linux/macOS
```
# 3. Install dependencies
```bash
pip install -r requirements.txt
```
# 4. Run the app
```bash
streamlit run app.py
```
---

## ▶️ Usage

1. Launch the app using `streamlit run app.py`.
2. Navigate through the sidebar to access the modules:
   - **Policy Analyzer**: Upload a `.pdf` or `.txt` insurance policy file.
   - **Scam Detector**: Paste suspicious text or SMS content.
   - **Risk Profile Generator**: Answer a few financial questions to generate a risk profile.
   - **Financial Tutor**: Ask finance-related questions for AI-powered explanations.
## 🤝 Contributing

We welcome contributions! Follow these steps:
1. Fork the repository
2. Create a new branch: `git checkout -b feature/YourFeature`
3. Make your changes and commit: `git commit -m 'Add your message'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Create a Pull Request
## 🙌 Credits

Built with ❤️ by [Shashank Arya](https://github.com/shank-sk)  
Thanks to OpenAI, Streamlit, and the open-source community.
