import streamlit as st

st.title("🔔 Notifications")

message = st.text_area(
    "Notification Message"
)

channel = st.selectbox(
    "Channel",
    [
        "Email",
        "SMS",
        "WhatsApp"
    ]
)

if st.button("Send"):

    st.success(
        f"{channel} Notification Sent"
    )