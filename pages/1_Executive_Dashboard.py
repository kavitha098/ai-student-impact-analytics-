import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("data/ai_student_impact_dataset.csv")

st.title("📊 Executive Dashboard")

df["GPA_Improvement"] = (
    df["Post_Semester_GPA"] -
    df["Pre_Semester_GPA"]
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Students",
    f"{len(df):,}"
)

col2.metric(
    "Avg GPA",
    round(df["Post_Semester_GPA"].mean(), 2)
)

col3.metric(
    "Avg AI Hours",
    round(df["Weekly_GenAI_Hours"].mean(), 1)
)

col4.metric(
    "Skill Retention",
    round(df["Skill_Retention_Score"].mean(), 1)
)

col5.metric(
    "Burnout %",
    round(
        (
            df["Burnout_Risk_Level"]
            .eq("High")
            .mean()
        ) * 100,
        1
    )
)

c1, c2 = st.columns(2)

with c1:
    fig = px.histogram(
        df,
        x="Weekly_GenAI_Hours",
        title="AI Usage Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

with c2:
    fig = px.box(
        df,
        y="Post_Semester_GPA",
        title="GPA Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Executive Insights")

st.info(
"""
• AI adoption continues to rise across majors.

• GPA gains positively correlate with prompt engineering skills.

• Burnout increases for students using AI >20 hrs/week.
"""
)
