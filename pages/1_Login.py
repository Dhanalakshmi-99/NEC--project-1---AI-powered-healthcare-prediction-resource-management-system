import streamlit as st
from utils.database import get_connection
import bcrypt

st.title("Login")

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    if user:

        stored_password = user[3]

        if bcrypt.checkpw(
            password.encode("utf-8"),
            stored_password
        ):

            st.success(
                f"Welcome {user[1]}"
            )

            st.session_state.logged_in = True
            st.session_state.role = user[4]

        else:

            st.error(
                "Invalid Password"
            )

    else:

        st.error(
            "User Not Found"
        )