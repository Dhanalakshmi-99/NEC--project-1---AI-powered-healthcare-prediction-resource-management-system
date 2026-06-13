import streamlit as st
import sqlite3
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

st.set_page_config(
    page_title="Doctor Dashboard",
    layout="wide"
)

st.title("👨‍⚕️ Doctor Dashboard")

conn = get_connection()

try:
    doctors = pd.read_sql_query(
        "SELECT * FROM doctors",
        conn
    )

    appointments = pd.read_sql_query(
        "SELECT * FROM appointments",
        conn
    )

except:
    doctors = pd.DataFrame()
    appointments = pd.DataFrame()

conn.close()

col1,col2,col3 = st.columns(3)

with col1:
    st.metric(
        "Total Doctors",
        len(doctors)
    )

with col2:
    st.metric(
        "Appointments",
        len(appointments)
    )

with col3:
    pending = 0

    if not appointments.empty:
        pending = len(
            appointments[
                appointments["status"]=="Pending"
            ]
        )

    st.metric(
        "Pending",
        pending
    )

st.markdown("---")

st.subheader("Today's Appointments")

if not appointments.empty:
    st.dataframe(
        appointments,
        use_container_width=True
    )
else:
    st.info("No Appointments Found")