import streamlit as st
import sqlite3
import pandas as pd
import os
import plotly.express as px

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

st.set_page_config(page_title="Admin Dashboard", layout="wide")

st.title("🏥 Healthcare AI Admin Dashboard")

conn = get_connection()

try:
    patients = pd.read_sql_query("SELECT * FROM patients", conn)
except:
    patients = pd.DataFrame()

try:
    doctors = pd.read_sql_query("SELECT * FROM doctors", conn)
except:
    doctors = pd.DataFrame()

try:
    appointments = pd.read_sql_query("SELECT * FROM appointments", conn)
except:
    appointments = pd.DataFrame()

conn.close()

c1, c2, c3, c4 = st.columns(4)

c1.metric("👨 Patients", len(patients))
c2.metric("👨‍⚕️ Doctors", len(doctors))
c3.metric("📅 Appointments", len(appointments))
c4.metric("🛏 Resources", 100)

st.markdown("---")

chart_df = pd.DataFrame({
    "Category": ["Patients", "Doctors", "Appointments"],
    "Count": [len(patients), len(doctors), len(appointments)]
})

fig = px.bar(
    chart_df,
    x="Category",
    y="Count",
    title="Hospital Statistics"
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.pie(
    chart_df,
    names="Category",
    values="Count",
    title="Resource Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("📋 Recent Appointments")

if not appointments.empty:
    st.dataframe(
        appointments.tail(10),
        use_container_width=True
    )
else:
    st.info("No appointments available")