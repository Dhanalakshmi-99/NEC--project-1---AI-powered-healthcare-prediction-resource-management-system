import streamlit as st
import sqlite3
import pandas as pd
import os

# --------------------------------
# DATABASE CONNECTION
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
CREATE TABLE IF NOT EXISTS beds(
    bed_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ward_name TEXT,
    bed_type TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

# --------------------------------
# PAGE TITLE
# --------------------------------

st.title("🛏 Bed Management System")

# --------------------------------
# ADD BED
# --------------------------------

st.subheader("➕ Add Bed")

col1, col2 = st.columns(2)

with col1:
    ward_name = st.text_input("Ward Name")

with col2:
    bed_type = st.selectbox(
        "Bed Type",
        [
            "General",
            "ICU",
            "Emergency",
            "Private"
        ]
    )

if st.button("Add Bed"):

    if ward_name.strip() == "":
        st.error("Ward Name Required")

    else:

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO beds
        (
            ward_name,
            bed_type,
            status
        )
        VALUES(?,?,?)
        """,
        (
            ward_name,
            bed_type,
            "Available"
        ))

        conn.commit()
        conn.close()

        st.success("Bed Added Successfully")
        st.rerun()

# --------------------------------
# LOAD DATA
# --------------------------------

conn = get_connection()

df = pd.read_sql_query(
    "SELECT * FROM beds",
    conn
)

conn.close()

# --------------------------------
# DASHBOARD METRICS
# --------------------------------

st.markdown("---")

total_beds = len(df)

available_beds = len(
    df[df["status"] == "Available"]
) if not df.empty else 0

occupied_beds = len(
    df[df["status"] == "Occupied"]
) if not df.empty else 0

icu_beds = len(
    df[df["bed_type"] == "ICU"]
) if not df.empty else 0

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Total Beds", total_beds)

with c2:
    st.metric("Available Beds", available_beds)

with c3:
    st.metric("Occupied Beds", occupied_beds)

with c4:
    st.metric("ICU Beds", icu_beds)

# --------------------------------
# VIEW BEDS
# --------------------------------

st.markdown("---")
st.subheader("📋 Bed Records")

st.dataframe(
    df,
    use_container_width=True
)

# --------------------------------
# OCCUPY BED
# --------------------------------

st.markdown("---")
st.subheader("🏥 Assign Bed")

if not df.empty:

    bed_id = st.selectbox(
        "Select Bed",
        df["bed_id"].tolist(),
        key="assign"
    )

    if st.button("Mark Occupied"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE beds
            SET status='Occupied'
            WHERE bed_id=?
            """,
            (bed_id,)
        )

        conn.commit()
        conn.close()

        st.success("Bed Assigned Successfully")
        st.rerun()

# --------------------------------
# RELEASE BED
# --------------------------------

st.markdown("---")
st.subheader("✅ Release Bed")

if not df.empty:

    release_id = st.selectbox(
        "Select Occupied Bed",
        df["bed_id"].tolist(),
        key="release"
    )

    if st.button("Release Bed"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE beds
            SET status='Available'
            WHERE bed_id=?
            """,
            (release_id,)
        )

        conn.commit()
        conn.close()

        st.success("Bed Released Successfully")
        st.rerun()

# --------------------------------
# DELETE BED
# --------------------------------

st.markdown("---")
st.subheader("🗑 Delete Bed")

if not df.empty:

    delete_id = st.selectbox(
        "Select Bed ID",
        df["bed_id"].tolist(),
        key="delete"
    )

    if st.button("Delete Bed"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM beds WHERE bed_id=?",
            (delete_id,)
        )

        conn.commit()
        conn.close()

        st.success("Bed Deleted Successfully")
        st.rerun()

else:

    st.info("No Beds Available")