import streamlit as st
import sqlite3
import pandas as pd
import os
from datetime import date

# -----------------------------
# DATABASE CONNECTION
# -----------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

# -----------------------------
# CREATE TABLE
# -----------------------------

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments(
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    doctor_name TEXT,
    appointment_date TEXT,
    appointment_time TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

# -----------------------------
# PAGE TITLE
# -----------------------------

st.title("📅 Appointment Booking System")

# -----------------------------
# LOAD PATIENTS
# -----------------------------

conn = get_connection()

try:
    patients_df = pd.read_sql_query(
        "SELECT name FROM patients",
        conn
    )
except:
    patients_df = pd.DataFrame()

try:
    doctors_df = pd.read_sql_query(
        "SELECT name FROM doctors",
        conn
    )
except:
    doctors_df = pd.DataFrame()

conn.close()

# -----------------------------
# BOOK APPOINTMENT
# -----------------------------

st.subheader("➕ Book Appointment")

if patients_df.empty:
    st.warning("No Patients Available")
elif doctors_df.empty:
    st.warning("No Doctors Available")
else:

    patient_name = st.selectbox(
        "Select Patient",
        patients_df["name"].tolist()
    )

    doctor_name = st.selectbox(
        "Select Doctor",
        doctors_df["name"].tolist()
    )

    appointment_date = st.date_input(
        "Appointment Date",
        date.today()
    )

    appointment_time = st.selectbox(
        "Appointment Time",
        [
            "09:00 AM",
            "10:00 AM",
            "11:00 AM",
            "12:00 PM",
            "02:00 PM",
            "03:00 PM",
            "04:00 PM"
        ]
    )

    if st.button("Book Appointment"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO appointments
        (
            patient_name,
            doctor_name,
            appointment_date,
            appointment_time,
            status
        )
        VALUES(?,?,?,?,?)
        """,
        (
            patient_name,
            doctor_name,
            str(appointment_date),
            appointment_time,
            "Pending"
        ))

        conn.commit()
        conn.close()

        st.success("Appointment Booked Successfully")
        st.rerun()

# -----------------------------
# VIEW APPOINTMENTS
# -----------------------------

st.markdown("---")
st.subheader("📋 Appointment Records")

conn = get_connection()

df = pd.read_sql_query(
    "SELECT * FROM appointments",
    conn
)

conn.close()

st.metric(
    "Total Appointments",
    len(df)
)

st.dataframe(
    df,
    use_container_width=True
)

# -----------------------------
# APPROVE APPOINTMENT
# -----------------------------

st.markdown("---")
st.subheader("✅ Approve Appointment")

if not df.empty:

    approve_id = st.selectbox(
        "Select Appointment ID",
        df["appointment_id"].tolist()
    )

    if st.button("Approve Appointment"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE appointments
            SET status='Approved'
            WHERE appointment_id=?
            """,
            (approve_id,)
        )

        conn.commit()
        conn.close()

        st.success("Appointment Approved")
        st.rerun()

# -----------------------------
# CANCEL APPOINTMENT
# -----------------------------

st.markdown("---")
st.subheader("❌ Cancel Appointment")

if not df.empty:

    cancel_id = st.selectbox(
        "Select Appointment",
        df["appointment_id"].tolist(),
        key="cancel"
    )

    if st.button("Cancel Appointment"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM appointments WHERE appointment_id=?",
            (cancel_id,)
        )

        conn.commit()
        conn.close()

        st.success("Appointment Cancelled")
        st.rerun()