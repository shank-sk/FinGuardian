import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import plotly.graph_objs as go
from utils.openrouter_handler import call_openrouter


def calculate_risk(age, income, loan):
    score = 100

    if age < 25:
        score -= 10
    elif age > 55:
        score -= 15

    if income < 20000:
        score -= 25
    elif income < 40000:
        score -= 10

    if loan > income * 0.5:
        score -= 30
    elif loan > income * 0.3:
        score -= 15
    elif loan > income * 0.1:
        score -= 5

    return max(0, min(score, 100))


def get_risk_advice(score):
    if score >= 80:
        return "✅ Low Risk: You're financially stable. Maintain your habits."
    elif score >= 50:
        return "⚠️ Medium Risk: Consider reducing debt or increasing savings."
    else:
        return "🚨 High Risk: Reassess spending, increase income, and reduce liabilities."


def plot_risk(score, mode="plotly"):
    if mode == "matplotlib":
        fig, ax = plt.subplots(figsize=(6, 1))
        if score >= 80:
            color = "green"
            label = "Low Risk"
        elif score >= 50:
            color = "orange"
            label = "Medium Risk"
        else:
            color = "red"
            label = "High Risk"

        ax.barh([0], [score], color=color, height=0.3)
        ax.set_xlim([0, 100])
        ax.set_yticks([])
        ax.set_xticks([0, 25, 50, 75, 100])
        ax.set_title(f"Risk Heatmap: {label} ({score}%)", fontsize=12)
        ax.text(score + 2, 0, f"{score}%", va='center', ha='left', fontsize=10)

        st.pyplot(fig)

    elif mode == "plotly":
        if score >= 80:
            label, color = "Low Risk", "green"
        elif score >= 50:
            label, color = "Medium Risk", "orange"
        else:
            label, color = "High Risk", "red"

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            title={'text': f"Financial Risk: {label}"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': color},
                'steps': [
                    {'range': [0, 50], 'color': '#ffcccc'},
                    {'range': [50, 80], 'color': '#ffe599'},
                    {'range': [80, 100], 'color': '#d9ead3'}
                ]
            }
        ))
        st.plotly_chart(fig, use_container_width=True)
