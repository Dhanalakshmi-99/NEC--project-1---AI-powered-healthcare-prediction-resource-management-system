import streamlit as st
import pandas as pd

st.title("👨‍⚕️ Staff Scheduling")

staff = st.text_input("Staff Name")

role = st.selectbox(
    "Role",
    ["Doctor","Nurse","Technician"]
)

shift = st.selectbox(
    "Shift",
    ["Morning","Evening","Night"]
)

if st.button("Assign Shift"):

    data = {
        "Name":[staff],
        "Role":[role],
        "Shift":[shift]
    }

    df = pd.DataFrame(data)

    st.success("Shift Assigned")
    st.dataframe(df)