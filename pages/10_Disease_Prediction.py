import streamlit as st
import pandas as pd
import sqlite3
import os

# ----------------------------------
# DATABASE CONNECTION
# ----------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Disease Prediction",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Disease Prediction System")

st.info(
    "Predict Disease Risk using Patient Health Parameters"
)

# ----------------------------------
# INPUT SECTION
# ----------------------------------

st.subheader("📋 Patient Health Information")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30
    )

    blood_pressure = st.number_input(
        "Blood Pressure",
        min_value=50,
        max_value=250,
        value=120
    )

    sugar = st.number_input(
        "Blood Sugar",
        min_value=50,
        max_value=500,
        value=100
    )

with col2:

    cholesterol = st.number_input(
        "Cholesterol",
        min_value=50,
        max_value=500,
        value=180
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=22.0
    )

    heart_rate = st.number_input(
        "Heart Rate",
        min_value=30,
        max_value=200,
        value=72
    )

# ----------------------------------
# PREDICTION LOGIC
# ----------------------------------

if st.button("🔍 Predict Disease Risk"):

    disease = "Healthy"
    risk = "Low"
    severity = "Low"

    # Diabetes

    if sugar > 140:
        disease = "Diabetes Risk"
        risk = "High"
        severity = "Moderate"

    # Heart Disease

    if (
        blood_pressure > 140
        and cholesterol > 220
    ):
        disease = "Heart Disease Risk"
        risk = "High"
        severity = "High"

    # Kidney Disease

    if (
        blood_pressure > 150
        and sugar > 180
    ):
        disease = "Kidney Disease Risk"
        risk = "Very High"
        severity = "Critical"

    # ----------------------------------
    # RESULTS
    # ----------------------------------

    st.markdown("---")
    st.subheader("📊 Prediction Results")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Predicted Disease",
            disease
        )

    with c2:
        st.metric(
            "Risk Level",
            risk
        )

    with c3:
        st.metric(
            "Severity",
            severity
        )

    # ----------------------------------
    # RECOMMENDATIONS
    # ----------------------------------

    st.markdown("---")
    st.subheader("💊 Recommendations")

    if disease == "Healthy":

        st.success(
            "Maintain Healthy Lifestyle"
        )

        st.write(
            "• Exercise Daily"
        )

        st.write(
            "• Balanced Diet"
        )

        st.write(
            "• Regular Health Checkups"
        )

    elif disease == "Diabetes Risk":

        st.warning(
            "Possible Diabetes Risk Detected"
        )

        st.write(
            "• Consult Endocrinologist"
        )

        st.write(
            "• Reduce Sugar Intake"
        )

        st.write(
            "• HbA1c Test Recommended"
        )

    elif disease == "Heart Disease Risk":

        st.error(
            "Heart Disease Risk Detected"
        )

        st.write(
            "• Consult Cardiologist"
        )

        st.write(
            "• ECG Recommended"
        )

        st.write(
            "• Monitor Blood Pressure"
        )

    elif disease == "Kidney Disease Risk":

        st.error(
            "Kidney Disease Risk Detected"
        )

        st.write(
            "• Consult Nephrologist"
        )

        st.write(
            "• Kidney Function Test"
        )

        st.write(
            "• Immediate Medical Review"
        )

# ----------------------------------
# DISEASE INFORMATION
# ----------------------------------

st.markdown("---")

st.subheader("📚 Supported Disease Predictions")

data = pd.DataFrame({
    "Disease":[
        "Diabetes",
        "Heart Disease",
        "Kidney Disease"
    ],
    "Parameters":[
        "Sugar Level",
        "BP + Cholesterol",
        "BP + Sugar"
    ]
})

st.dataframe(
    data,
    use_container_width=True
)

# ----------------------------------
# FOOTER
# ----------------------------------

st.markdown("---")

st.success(
    "✅ Disease Prediction Module Loaded Successfully"
)