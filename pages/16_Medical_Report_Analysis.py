import streamlit as st

st.title("🧪 Medical Report Analysis")

report = st.file_uploader(
    "Upload Report",
    ["pdf","jpg","png"]
)

if report:

    st.success("Report Uploaded")

    st.subheader("AI Analysis")

    st.write("Hemoglobin : Normal")
    st.write("Sugar : Normal")
    st.write("Cholesterol : Borderline")

    st.warning(
        "Follow-up test recommended"
    )