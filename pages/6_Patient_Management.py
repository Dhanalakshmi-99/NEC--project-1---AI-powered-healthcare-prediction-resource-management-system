import streamlit as st

st.title("Patient Management")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Patient Name")
    age = st.number_input("Age", 1, 120)

with col2:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

if st.button("Submit"):
    st.success(f"Patient Added: {name}")