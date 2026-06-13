import streamlit as st
import pandas as pd

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Treatment Recommendation",
    page_icon="💊",
    layout="wide"
)

st.title("💊 AI Treatment Recommendation System")

st.info(
    "Get AI-Based Treatment Recommendations"
)

# -----------------------------------
# INPUT SECTION
# -----------------------------------

st.subheader("🏥 Select Disease")

disease = st.selectbox(
    "Disease",
    [
        "Diabetes",
        "Heart Disease",
        "Kidney Disease",
        "Hypertension",
        "Asthma",
        "Healthy"
    ]
)

# -----------------------------------
# RECOMMENDATION ENGINE
# -----------------------------------

if st.button("Generate Recommendation"):

    st.markdown("---")

    if disease == "Diabetes":

        st.subheader("🩺 Disease")
        st.success("Diabetes")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("💊 Treatment Plan")

            st.write("• Blood Sugar Monitoring")
            st.write("• Daily Exercise")
            st.write("• Low Sugar Diet")
            st.write("• Regular Follow-ups")

        with col2:
            st.subheader("👨‍⚕️ Specialist")

            st.write("• Endocrinologist")
            st.write("• Dietitian")

        st.subheader("🧪 Recommended Tests")

        st.write("• HbA1c Test")
        st.write("• Fasting Blood Sugar")
        st.write("• Kidney Function Test")

    # -----------------------------------

    elif disease == "Heart Disease":

        st.subheader("🩺 Disease")
        st.error("Heart Disease")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("💊 Treatment Plan")

            st.write("• Blood Pressure Control")
            st.write("• Cholesterol Management")
            st.write("• Cardiac Rehabilitation")
            st.write("• Lifestyle Modification")

        with col2:
            st.subheader("👨‍⚕️ Specialist")

            st.write("• Cardiologist")

        st.subheader("🧪 Recommended Tests")

        st.write("• ECG")
        st.write("• Echocardiogram")
        st.write("• Lipid Profile")

    # -----------------------------------

    elif disease == "Kidney Disease":

        st.subheader("🩺 Disease")
        st.error("Kidney Disease")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("💊 Treatment Plan")

            st.write("• Blood Pressure Monitoring")
            st.write("• Kidney-Friendly Diet")
            st.write("• Fluid Management")
            st.write("• Medication Monitoring")

        with col2:
            st.subheader("👨‍⚕️ Specialist")

            st.write("• Nephrologist")

        st.subheader("🧪 Recommended Tests")

        st.write("• Creatinine Test")
        st.write("• Urine Analysis")
        st.write("• GFR Test")

    # -----------------------------------

    elif disease == "Hypertension":

        st.subheader("🩺 Disease")
        st.warning("Hypertension")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("💊 Treatment Plan")

            st.write("• Salt Reduction")
            st.write("• Weight Management")
            st.write("• Daily Exercise")
            st.write("• Stress Control")

        with col2:
            st.subheader("👨‍⚕️ Specialist")

            st.write("• General Physician")
            st.write("• Cardiologist")

        st.subheader("🧪 Recommended Tests")

        st.write("• Blood Pressure Monitoring")
        st.write("• ECG")

    # -----------------------------------

    elif disease == "Asthma":

        st.subheader("🩺 Disease")
        st.warning("Asthma")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("💊 Treatment Plan")

            st.write("• Inhaler Usage")
            st.write("• Avoid Allergens")
            st.write("• Breathing Exercises")

        with col2:
            st.subheader("👨‍⚕️ Specialist")

            st.write("• Pulmonologist")

        st.subheader("🧪 Recommended Tests")

        st.write("• Lung Function Test")
        st.write("• Chest X-Ray")

    # -----------------------------------

    else:

        st.success("Healthy")

        st.subheader("✅ Recommendations")

        st.write("• Maintain Balanced Diet")
        st.write("• Daily Exercise")
        st.write("• Good Sleep")
        st.write("• Annual Health Checkup")

# -----------------------------------
# TREATMENT SUMMARY TABLE
# -----------------------------------

st.markdown("---")

st.subheader("📊 Supported Treatments")

data = pd.DataFrame(
    {
        "Disease":[
            "Diabetes",
            "Heart Disease",
            "Kidney Disease",
            "Hypertension",
            "Asthma"
        ],
        "Specialist":[
            "Endocrinologist",
            "Cardiologist",
            "Nephrologist",
            "Cardiologist",
            "Pulmonologist"
        ]
    }
)

st.dataframe(
    data,
    use_container_width=True
)

# -----------------------------------
# FOOTER
# -----------------------------------

st.markdown("---")

st.success(
    "✅ Treatment Recommendation Module Loaded Successfully"
)