import streamlit as st
import sqlite3
import pandas as pd
import os

# -----------------------------
# DATABASE CONNECTION
# -----------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database.db")


def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


# -----------------------------
# CREATE TABLE IF NOT EXISTS
# -----------------------------

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    weight REAL,
    height REAL,
    blood_group TEXT,
    allergies TEXT,
    medical_history TEXT,
    insurance TEXT
)
""")

conn.commit()
conn.close()

# -----------------------------
# PAGE TITLE
# -----------------------------

st.set_page_config(
    page_title="Patient Management",
    layout="wide"
)

st.title("🏥 Patient Management System")

# -----------------------------
# ADD PATIENT
# -----------------------------

st.subheader("➕ Add New Patient")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Patient Name")
    age = st.number_input("Age", min_value=1, max_value=120, value=25)
    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=1.0,
        value=60.0
    )

with col2:
    height = st.number_input(
        "Height (cm)",
        min_value=1.0,
        value=170.0
    )

    blood_group = st.selectbox(
        "Blood Group",
        ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    )

    insurance = st.text_input("Insurance Details")

allergies = st.text_area("Allergies")
medical_history = st.text_area("Medical History")

if st.button("Add Patient"):

    if name.strip() == "":
        st.error("Patient Name is Required")

    else:

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
            INSERT INTO patients
            (
                name,
                age,
                gender,
                weight,
                height,
                blood_group,
                allergies,
                medical_history,
                insurance
            )
            VALUES(?,?,?,?,?,?,?,?,?)
            """,
            (
                name,
                age,
                gender,
                weight,
                height,
                blood_group,
                allergies,
                medical_history,
                insurance
            ))

            conn.commit()
            conn.close()

            st.success("✅ Patient Added Successfully")
            st.rerun()

        except Exception as e:
            st.error(f"Error: {e}")

# -----------------------------
# VIEW PATIENTS
# -----------------------------

st.markdown("---")
st.subheader("📋 Patient Records")

try:

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM patients",
        conn
    )

    conn.close()

    st.metric(
        "Total Patients",
        len(df)
    )

    st.dataframe(
        df,
        use_container_width=True
    )

except Exception as e:

    st.error(f"Database Error: {e}")
    df = pd.DataFrame()

# -----------------------------
# DELETE PATIENT
# -----------------------------

st.markdown("---")
st.subheader("🗑 Delete Patient")

if not df.empty:

    patient_id = st.selectbox(
        "Select Patient ID",
        df["patient_id"].tolist()
    )

    if st.button("Delete Patient"):

        try:

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM patients WHERE patient_id=?",
                (patient_id,)
            )

            conn.commit()
            conn.close()

            st.success("Patient Deleted Successfully")
            st.rerun()

        except Exception as e:

            st.error(f"Error: {e}")

else:

    st.info("No Patients Available")