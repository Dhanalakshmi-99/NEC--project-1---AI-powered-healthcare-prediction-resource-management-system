import streamlit as st
import sqlite3
import pandas as pd
import os

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Healthcare AI System",
    page_icon="🏥",
    layout="wide"
)

# -----------------------------------
# DATABASE
# -----------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

# -----------------------------------
# SIDEBAR
# -----------------------------------

try:
    st.sidebar.image(
        "assets/hospital_logo.png",
        width=180
    )
except:
    pass

st.sidebar.title("🏥 Healthcare AI")

st.sidebar.success(
    "AI Powered Healthcare Prediction & Resource Management System"
)

# -----------------------------------
# LOAD DATA
# -----------------------------------

conn = get_connection()

try:
    patients = pd.read_sql_query(
        "SELECT * FROM patients",
        conn
    )
except:
    patients = pd.DataFrame()

try:
    doctors = pd.read_sql_query(
        "SELECT * FROM doctors",
        conn
    )
except:
    doctors = pd.DataFrame()

try:
    appointments = pd.read_sql_query(
        "SELECT * FROM appointments",
        conn
    )
except:
    appointments = pd.DataFrame()

try:
    beds = pd.read_sql_query(
        "SELECT * FROM beds",
        conn
    )
except:
    beds = pd.DataFrame()

conn.close()

# -----------------------------------
# HEADER
# -----------------------------------

st.title(
    "🏥 AI Powered Healthcare Prediction & Resource Management System"
)

st.markdown("""
### Welcome to the Intelligent Healthcare Platform

This platform helps hospitals:

✅ Predict Diseases

✅ Recommend Treatments

✅ Manage Patients

✅ Optimize Hospital Resources

✅ Monitor Bed Availability

✅ Analyze Medical Reports

✅ Generate Healthcare Analytics
""")

st.markdown("---")

# -----------------------------------
# METRICS
# -----------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "👨 Patients",
        len(patients)
    )

with c2:
    st.metric(
        "👨‍⚕️ Doctors",
        len(doctors)
    )

with c3:
    st.metric(
        "📅 Appointments",
        len(appointments)
    )

with c4:
    st.metric(
        "🛏 Beds",
        len(beds)
    )

st.markdown("---")

# -----------------------------------
# MODULES
# -----------------------------------

st.subheader("🚀 System Modules")

col1, col2, col3 = st.columns(3)

with col1:

    st.success("👤 Authentication")
    st.success("🏥 Patient Management")
    st.success("👨‍⚕️ Doctor Management")
    st.success("📅 Appointment Booking")
    st.success("📋 EHR Records")
    st.success("🧠 Disease Prediction")

with col2:

    st.info("💊 Treatment Recommendation")
    st.info("📈 Outcome Prediction")
    st.info("🛏 Bed Management")
    st.info("👩‍⚕️ Staff Scheduling")
    st.info("📦 Resource Allocation")

with col3:

    st.warning("📄 Medical Report Analysis")
    st.warning("🚨 Emergency Alerts")
    st.warning("🤖 AI Chatbot")
    st.warning("📊 Analytics Dashboard")
    st.warning("📑 Reports")

st.markdown("---")

# -----------------------------------
# QUICK STATS
# -----------------------------------

st.subheader("📊 Hospital Overview")

overview = pd.DataFrame({
    "Category": [
        "Patients",
        "Doctors",
        "Appointments",
        "Beds"
    ],
    "Count": [
        len(patients),
        len(doctors),
        len(appointments),
        len(beds)
    ]
})

st.bar_chart(
    overview.set_index("Category")
)

# -----------------------------------
# RECENT APPOINTMENTS
# -----------------------------------

st.subheader("📅 Recent Appointments")

if not appointments.empty:

    st.dataframe(
        appointments.tail(10),
        use_container_width=True
    )

else:

    st.info(
        "No Appointments Available"
    )

st.markdown("---")

st.success(
    "✅ Healthcare AI System Loaded Successfully"
)