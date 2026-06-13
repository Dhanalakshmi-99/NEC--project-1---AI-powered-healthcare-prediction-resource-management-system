import streamlit as st

st.title("🏥 Resource Allocation")

beds = st.number_input(
    "Available Beds",
    0,
    500,
    100
)

ventilators = st.number_input(
    "Ventilators",
    0,
    100,
    20
)

oxygen = st.number_input(
    "Oxygen Units",
    0,
    1000,
    500
)

st.metric("Beds", beds)
st.metric("Ventilators", ventilators)
st.metric("Oxygen", oxygen)

if beds < 20:
    st.warning("Low Bed Availability")

if ventilators < 5:
    st.error("Critical Ventilator Shortage")