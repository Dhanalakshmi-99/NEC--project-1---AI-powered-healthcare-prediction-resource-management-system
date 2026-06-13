import streamlit as st
import pandas as pd

st.title("📊 Healthcare Analytics")

data = pd.DataFrame(
{
"Patients":[120],
"Doctors":[25],
"Beds":[100],
"Appointments":[80]
}
)

st.dataframe(data)

st.bar_chart(data.T)