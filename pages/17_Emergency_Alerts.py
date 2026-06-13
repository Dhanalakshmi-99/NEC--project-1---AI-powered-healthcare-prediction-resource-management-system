import streamlit as st

st.title("🚨 Emergency Alert System")

oxygen = st.number_input(
    "Oxygen Level",
    0,
    100,
    98
)

pulse = st.number_input(
    "Pulse Rate",
    0,
    200,
    80
)

if st.button("Check Status"):

    if oxygen < 90:

        st.error(
            "Critical Emergency Alert"
        )

        st.write(
            "Doctor Notified"
        )

        st.write(
            "Nurse Notified"
        )

        st.write(
            "Family Alert Sent"
        )

    else:

        st.success("Patient Stable")