import streamlit as st
import sqlite3
import pandas as pd
import os

# ----------------------------
# DATABASE CONNECTION
# ----------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="Patient Dashboard",
    page_icon="👤",
    layout="wide"
)

st.title("👤 Patient Dashboard")

# ----------------------------
# LOAD DATA
# ----------------------------

conn = get_connection()

try:
    patients_df = pd.read_sql_query(
        "SELECT * FROM patients",
        conn
    )
except:
    patients_df = pd.DataFrame()

try:
    appointments_df = pd.read_sql_query(
        "SELECT * FROM appointments",
        conn
    )
except:
    appointments_df = pd.DataFrame()

conn.close()

# ----------------------------
# DASHBOARD METRICS
# ----------------------------

total_patients = len(patients_df)

total_appointments = len(appointments_df)

pending_appointments = 0
approved_appointments = 0

if not appointments_df.empty:

    pending_appointments = len(
        appointments_df[
            appointments_df["status"] == "Pending"
        ]
    )

    approved_appointments = len(
        appointments_df[
            appointments_df["status"] == "Approved"
        ]
    )

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Total Patients",
        total_patients
    )

with c2:
    st.metric(
        "Appointments",
        total_appointments
    )

with c3:
    st.metric(
        "Pending",
        pending_appointments
    )

with c4:
    st.metric(
        "Approved",
        approved_appointments
    )

# ----------------------------
# PATIENT RECORDS
# ----------------------------

st.markdown("---")
st.subheader("📋 Patient Records")

if not patients_df.empty:

    st.dataframe(
        patients_df,
        use_container_width=True
    )

else:
    st.info("No Patient Records Found")

# ----------------------------
# APPOINTMENTS
# ----------------------------

st.markdown("---")
st.subheader("📅 Appointment History")

if not appointments_df.empty:

    st.dataframe(
        appointments_df,
        use_container_width=True
    )

else:
    st.info("No Appointments Found")

# ----------------------------
# PATIENT SEARCH
# ----------------------------

st.markdown("---")
st.subheader("🔍 Search Patient")

if not patients_df.empty:

    search_name = st.text_input(
        "Enter Patient Name"
    )

    if search_name:

        result = patients_df[
            patients_df["name"]
            .str.contains(
                search_name,
                case=False,
                na=False
            )
        ]

        if not result.empty:

            st.success(
                f"{len(result)} Patient Found"
            )

            st.dataframe(
                result,
                use_container_width=True
            )

        else:

            st.warning(
                "No Patient Found"
            )

# ----------------------------
# HEALTH SUMMARY
# ----------------------------

st.markdown("---")
st.subheader("🏥 Health Summary")

if not patients_df.empty:

    male_count = len(
        patients_df[
            patients_df["gender"] == "Male"
        ]
    )

    female_count = len(
        patients_df[
            patients_df["gender"] == "Female"
        ]
    )

    other_count = len(
        patients_df[
            patients_df["gender"] == "Other"
        ]
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Male Patients",
            male_count
        )

    with col2:
        st.metric(
            "Female Patients",
            female_count
        )

    with col3:
        st.metric(
            "Other Patients",
            other_count
        )

# ----------------------------
# RECENT PATIENTS
# ----------------------------

st.markdown("---")
st.subheader("🆕 Recent Patients")

if not patients_df.empty:

    recent = patients_df.tail(5)

    st.dataframe(
        recent,
        use_container_width=True
    )

else:

    st.info("No Data Available")