import streamlit as st
import sqlite3
import pandas as pd
import os
from datetime import datetime

# ---------------------------------
# DATABASE CONNECTION
# ---------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database.db")

UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

# ---------------------------------
# CREATE TABLE
# ---------------------------------

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ehr_records(
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    report_type TEXT,
    report_date TEXT,
    notes TEXT,
    file_name TEXT
)
""")

conn.commit()
conn.close()

# ---------------------------------
# PAGE TITLE
# ---------------------------------

st.set_page_config(
    page_title="EHR Records",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Electronic Health Records (EHR)")

# ---------------------------------
# LOAD PATIENTS
# ---------------------------------

conn = get_connection()

try:
    patients_df = pd.read_sql_query(
        "SELECT name FROM patients",
        conn
    )
except:
    patients_df = pd.DataFrame()

conn.close()

# ---------------------------------
# ADD RECORD
# ---------------------------------

st.subheader("➕ Add Medical Record")

if patients_df.empty:

    st.warning(
        "No Patients Available. Add Patients First."
    )

else:

    patient_name = st.selectbox(
        "Select Patient",
        patients_df["name"].tolist()
    )

    report_type = st.selectbox(
        "Report Type",
        [
            "Blood Test",
            "ECG",
            "MRI",
            "CT Scan",
            "X-Ray",
            "Prescription",
            "Vaccination",
            "Lab Report"
        ]
    )

    report_date = st.date_input(
        "Report Date"
    )

    notes = st.text_area(
        "Doctor Notes / Remarks"
    )

    uploaded_file = st.file_uploader(
        "Upload Report",
        type=[
            "pdf",
            "png",
            "jpg",
            "jpeg"
        ]
    )

    if st.button("Save Record"):

        filename = ""

        if uploaded_file is not None:

            filename = uploaded_file.name

            save_path = os.path.join(
                UPLOAD_DIR,
                filename
            )

            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO ehr_records
        (
            patient_name,
            report_type,
            report_date,
            notes,
            file_name
        )
        VALUES(?,?,?,?,?)
        """,
        (
            patient_name,
            report_type,
            str(report_date),
            notes,
            filename
        ))

        conn.commit()
        conn.close()

        st.success(
            "Medical Record Saved Successfully"
        )

        st.rerun()

# ---------------------------------
# VIEW RECORDS
# ---------------------------------

st.markdown("---")
st.subheader("📑 Medical Records")

conn = get_connection()

try:

    records_df = pd.read_sql_query(
        "SELECT * FROM ehr_records",
        conn
    )

except:

    records_df = pd.DataFrame()

conn.close()

st.metric(
    "Total Records",
    len(records_df)
)

if not records_df.empty:

    st.dataframe(
        records_df,
        use_container_width=True
    )

else:

    st.info(
        "No Medical Records Found"
    )

# ---------------------------------
# SEARCH RECORDS
# ---------------------------------

st.markdown("---")
st.subheader("🔍 Search Patient Records")

if not records_df.empty:

    search_name = st.text_input(
        "Enter Patient Name"
    )

    if search_name:

        result = records_df[
            records_df["patient_name"]
            .str.contains(
                search_name,
                case=False,
                na=False
            )
        ]

        if not result.empty:

            st.success(
                f"{len(result)} Records Found"
            )

            st.dataframe(
                result,
                use_container_width=True
            )

        else:

            st.warning(
                "No Records Found"
            )

# ---------------------------------
# DELETE RECORD
# ---------------------------------

st.markdown("---")
st.subheader("🗑 Delete Record")

if not records_df.empty:

    delete_id = st.selectbox(
        "Select Record ID",
        records_df["record_id"].tolist()
    )

    if st.button("Delete Record"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM ehr_records
            WHERE record_id=?
            """,
            (delete_id,)
        )

        conn.commit()
        conn.close()

        st.success(
            "Record Deleted Successfully"
        )

        st.rerun()

# ---------------------------------
# RECENT RECORDS
# ---------------------------------

st.markdown("---")
st.subheader("🆕 Recent Medical Records")

if not records_df.empty:

    st.dataframe(
        records_df.tail(5),
        use_container_width=True
    )

# ---------------------------------
# FOOTER
# ---------------------------------

st.markdown("---")

st.success(
    "✅ Electronic Health Records Module Loaded Successfully"
)