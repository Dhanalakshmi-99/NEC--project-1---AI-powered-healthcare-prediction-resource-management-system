import streamlit as st
import pandas as pd

st.title("📄 Reports")

report_type = st.selectbox(
    "Select Report",
    [
        "Disease Statistics",
        "Bed Occupancy",
        "Doctor Performance",
        "Recovery Report"
    ]
)

if st.button("Generate Report"):

    df = pd.DataFrame({
        "Metric":[
            "Sample1",
            "Sample2",
            "Sample3"
        ],
        "Value":[
            100,
            80,
            60
        ]
    })

    st.dataframe(df)

    st.success(
        "Report Generated Successfully"
    )