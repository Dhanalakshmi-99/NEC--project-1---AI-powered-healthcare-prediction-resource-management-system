import streamlit as st
from utils.database import get_connection
from utils.auth import hash_password

st.title("User Registration")

name = st.text_input("Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

role = st.selectbox(
    "Role",
    ["Patient", "Doctor", "Admin"]
)

if st.button("Register"):

    conn = get_connection()
    cursor = conn.cursor()

    hashed = hash_password(password)

    cursor.execute(
        "INSERT INTO users(name,email,password,role) VALUES(?,?,?,?)",
        (name,email,hashed,role)
    )

    conn.commit()
    conn.close()

    st.success("Registered Successfully")