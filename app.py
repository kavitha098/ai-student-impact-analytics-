import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Student Impact Analytics",
    layout="wide"
)

st.title("🎓 AI Student Impact Analytics Platform")

df = pd.read_csv(
    "data/ai_student_impact_dataset.csv"
)

st.sidebar.header("Filters")

major = st.sidebar.multiselect(
    "Major",
    df["Major_Category"].unique()
)

if major:
    df = df[df["Major_Category"].isin(major)]

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Students",
    f"{len(df):,}"
)

col2.metric(
    "Avg GPA",
    round(df["Post_Semester_GPA"].mean(),2)
)

col3.metric(
    "Avg AI Hours",
    round(df["Weekly_GenAI_Hours"].mean(),1)
)

col4.metric(
    "Skill Retention",
    round(df["Skill_Retention_Score"].mean(),1)
)
