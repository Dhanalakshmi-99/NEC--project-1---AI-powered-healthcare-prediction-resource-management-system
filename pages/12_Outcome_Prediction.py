import streamlit as st

st.set_page_config(
    page_title="Patient Outcome Prediction",
    layout="wide"
)

st.title("📈 Patient Outcome Prediction")

age = st.number_input("Age", 1, 120, 40)
bp = st.number_input("Blood Pressure", 50, 250, 120)
sugar = st.number_input("Sugar Level", 50, 500, 100)

if st.button("Predict Outcome"):

    recovery = 95
    stay = 2
    icu = "No"
    mortality = "Low"

    if bp > 140 or sugar > 180:
        recovery = 75
        stay = 5
        icu = "Possible"
        mortality = "Medium"

    if bp > 170 and sugar > 250:
        recovery = 50
        stay = 10
        icu = "Required"
        mortality = "High"

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Recovery %", f"{recovery}%")
    c2.metric("Stay Duration", f"{stay} Days")
    c3.metric("ICU Need", icu)
    c4.metric("Mortality Risk", mortality)