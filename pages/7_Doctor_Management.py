import streamlit as st
import sqlite3
import pandas as pd
import os

# --------------------------------
# DATABASE
# --------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database.db")


def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


# --------------------------------
# CREATE TABLE
# --------------------------------

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors(
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialization TEXT,
    qualification TEXT,
    experience INTEGER,
    available_slots TEXT
)
""")

conn.commit()
conn.close()

# --------------------------------
# PAGE TITLE
# --------------------------------

st.set_page_config(
    page_title="Doctor Management",
    layout="wide"
)

st.title("👨‍⚕️ Doctor Management System")

# --------------------------------
# ADD DOCTOR
# --------------------------------

st.subheader("➕ Add Doctor")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Doctor Name")
    specialization = st.text_input("Specialization")
    qualification = st.text_input("Qualification")

with col2:
    experience = st.number_input(
        "Experience (Years)",
        min_value=0,
        max_value=50,
        value=1
    )

    available_slots = st.text_input(
        "Available Slots",
        placeholder="10AM-1PM"
    )

if st.button("Add Doctor"):

    if name.strip() == "":
        st.error("Doctor Name Required")

    else:

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO doctors
        (
            name,
            specialization,
            qualification,
            experience,
            available_slots
        )
        VALUES(?,?,?,?,?)
        """,
        (
            name,
            specialization,
            qualification,
            experience,
            available_slots
        ))

        conn.commit()
        conn.close()

        st.success("Doctor Added Successfully")
        st.rerun()

# --------------------------------
# VIEW DOCTORS
# --------------------------------

st.markdown("---")
st.subheader("📋 Doctor Records")

conn = get_connection()

df = pd.read_sql_query(
    "SELECT * FROM doctors",
    conn
)

conn.close()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Doctors",
        len(df)
    )

with col2:
    st.metric(
        "Specializations",
        df["specialization"].nunique() if not df.empty else 0
    )

search = st.text_input(
    "🔍 Search Doctor"
)

if search:
    df = df[
        df["name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

st.dataframe(
    df,
    use_container_width=True
)

# --------------------------------
# UPDATE DOCTOR
# --------------------------------

st.markdown("---")
st.subheader("✏️ Update Doctor")

if not df.empty:

    selected_id = st.selectbox(
        "Select Doctor ID",
        df["doctor_id"].tolist()
    )

    row = df[df["doctor_id"] == selected_id].iloc[0]

    new_name = st.text_input(
        "Name",
        row["name"]
    )

    new_specialization = st.text_input(
        "Specialization",
        row["specialization"]
    )

    new_qualification = st.text_input(
        "Qualification",
        row["qualification"]
    )

    new_experience = st.number_input(
        "Experience",
        0,
        50,
        int(row["experience"])
    )

    new_slots = st.text_input(
        "Available Slots",
        row["available_slots"]
    )

    if st.button("Update Doctor"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE doctors
        SET
            name=?,
            specialization=?,
            qualification=?,
            experience=?,
            available_slots=?
        WHERE doctor_id=?
        """,
        (
            new_name,
            new_specialization,
            new_qualification,
            new_experience,
            new_slots,
            selected_id
        ))

        conn.commit()
        conn.close()

        st.success("Doctor Updated Successfully")
        st.rerun()

# --------------------------------
# DELETE DOCTOR
# --------------------------------

st.markdown("---")
st.subheader("🗑 Delete Doctor")

if not df.empty:

    delete_id = st.selectbox(
        "Select Doctor ID",
        df["doctor_id"].tolist(),
        key="delete"
    )

    if st.button("Delete Doctor"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM doctors WHERE doctor_id=?",
            (delete_id,)
        )

        conn.commit()
        conn.close()

        st.success("Doctor Deleted Successfully")
        st.rerun()

else:

    st.info("No Doctors Available")