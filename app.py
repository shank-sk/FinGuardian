import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from modules.policy_analyzer import extract_text, analyze_policy
from modules.scam_detector import detect_scam
from modules.risk_profile import calculate_risk, plot_risk, get_risk_advice
from modules.financial_tutor import call_tutor

st.set_page_config(page_title="🛡️ FinGuardian", layout="wide", page_icon="🛡️")

st.markdown("""
    <style>
    .big-title {
        font-size: 36px !important;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .subtext {
        font-size: 16px;
        color: #888;
    }
    .metric-container {
        background-color: #f1f3f6;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🛡️ FinGuardian: Your Financial Co-Pilot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Analyze. Detect. Protect. Learn.</div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs([
    "📄 Analyze Policy", 
    "🚨 Scan Scam", 
    "📈 Risk Profile", 
    "🎓 Financial Tutor"
])

# --- TAB 1: POLICY ANALYZER ---
with tab1:
    st.header("📄 Smart Policy Analyzer")
    st.caption("Upload a term/health/life insurance policy. We'll summarize and flag risky clauses.")

    uploaded_file = st.file_uploader("📎 Upload your policy document (PDF or text)")
    if uploaded_file:
        text = extract_text(uploaded_file)
        with st.spinner("Analyzing your policy... 🧠"):
            summary = analyze_policy(text)

        with st.expander("📋 Policy Summary", expanded=True):
            if summary.startswith("⚠️") or summary.startswith("❌"):
                st.error(summary)
            else:
                st.success(summary)

# --- TAB 2: SCAM DETECTOR ---
with tab2:
    st.header("🚨 Scam Detector")
    st.caption("Paste an SMS/email/message to check if it's fraudulent using AI")

    scam_input = st.text_area("📝 Paste the suspicious content here")

    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🔍 Analyze"):
            if scam_input.strip():
                with st.spinner("Scanning..."):
                    result = detect_scam(scam_input)
                with st.expander("🚨 Scam Analysis Result"):
                    st.warning(result)
            else:
                st.info("Please paste something to analyze.")

# --- TAB 3: RISK PROFILE GENERATOR ---
with tab3:
    st.header("📈 Custom Financial Risk Profile")
    st.caption("Answer a few quick questions and get your risk heatmap and advice")

    with st.form("risk_form"):
        age = st.slider("🎂 Age", 18, 70, 30)
        income = st.number_input("💰 Monthly Income (₹)", min_value=0)
        loan = st.number_input("🏦 Monthly Loan EMI (₹)", min_value=0)
        submitted = st.form_submit_button("Evaluate My Risk")

        if submitted:
            score = calculate_risk(age, income, loan)

            # Dynamic Color Display
            if score <= 3:
                color = "green"
            elif score <= 6:
                color = "orange"
            else:
                color = "red"

            st.markdown(f"""
                <div class='metric-container'>
                    <h4 style='color:{color}'>Risk Score: {score} / 10</h4>
                </div>
            """, unsafe_allow_html=True)

            st.info(get_risk_advice(score))
            plot_risk(score)

# --- TAB 4: FINANCIAL TUTOR ---
with tab4:
    st.header("🎓 Financial Literacy Coach")
    st.caption("Ask any finance-related question. Learn in your language and comfort level.")

    topic = st.text_input("🧠 What do you want to learn about?")
    level = st.radio("📘 Your current understanding level", ["Beginner", "Intermediate", "Expert"], horizontal=True)

    if st.button("💡 Get Explanation"):
        if topic:
            with st.spinner("Explaining in your language..."):
                answer = call_tutor(topic, level)
            with st.expander("📘 Explanation"):
                st.success(answer)
        else:
            st.warning("Please ask something first.")
