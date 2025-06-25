# app.py
import streamlit as st
import numpy as np
from optimizer import run_pso_optimization

st.set_page_config(page_title="Reverse Optimization", layout="wide")

st.markdown("""
    <h1 style='text-align: center; color: black;'>🎯 Reverse Optimization for Biochar Properties</h1>
    <div style='text-align: center; font-size: 16px;'>
    Enter biomass features and assign weights to output properties to search for the best experiment condition.
    </div><br>
""", unsafe_allow_html=True)

# ----------------------
# Input Biomass Features
# ----------------------
st.sidebar.header("📝 Input Biomass Properties")
biomass_labels = [
    "Ash (%)", "Volatile matter (%)", "Fixed carbon (%)", "Carbon (%)",
    "Hydrogen (%)", "Oxygen (%)", "Nitrogen (%)"
]
fixed_properties = []
for label in biomass_labels:
    val = st.sidebar.number_input(label, value=0.0)
    fixed_properties.append(val)

# ----------------------
# Input Optimization Weights
# ----------------------
st.sidebar.header("⚖️ Output Property Weights")
output_labels = [
    "Yield (%)", "pH", "Ash (%)", "Volatile matter (%)", "Nitrogen (%)",
    "Fixed carbon (%)", "Carbon (%)", "H/C ratio", "O/C ratio"
]
weights = []
for label in output_labels:
    val = st.sidebar.number_input(f"{label} weight", value=0, step=1, format="%d")
    weights.append(val)

# ----------------------
# Run Optimization
# ----------------------
if st.sidebar.button("Run Optimization"):
    with st.spinner("Optimizing using PSO..."):
        optimal_conditions, predicted_outputs = run_pso_optimization(fixed_properties, weights)

        st.success("✅ Optimization completed!")

        # 显示最优实验条件
        st.markdown("### 🔧 Optimal Experimental Conditions")
        condition_labels = ["Highest temperature (℃)", "Heating rate (℃/min)", "Residence time (min)"]
        cols1 = st.columns(3)
        for i, val in enumerate(optimal_conditions):
            cols1[i].markdown(f"<div style='padding:10px; border:1px solid #ddd; border-radius:10px; background-color:#f4f4f4;'>
                <b>{condition_labels[i]}</b><br><span style='font-size:20px;'>{val:.2f}</span>
                </div>", unsafe_allow_html=True)

        # 显示预测输出
        st.markdown("### 📈 Predicted Biochar Properties")
        cols2 = st.columns(3)
        for i, val in enumerate(predicted_outputs):
            cols2[i % 3].markdown(f"<div style='padding:10px; border:1px solid #ddd; border-radius:10px; background-color:#f9f9f9;'>
                <b>{output_labels[i]}</b><br><span style='font-size:20px;'>{val:.2f}</span>
                </div>", unsafe_allow_html=True)

else:
    st.info("👈 Please enter input values and press 'Run Optimization'.")


