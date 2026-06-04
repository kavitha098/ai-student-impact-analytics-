import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/ai_student_impact_dataset.csv")

st.title("🏛 Institutional Policy Impact")

fig = px.violin(
    df,
    x="Institutional_Policy",
    y="Post_Semester_GPA",
    color="Institutional_Policy"
)

st.plotly_chart(fig, use_container_width=True)

fig = px.box(
    df,
    x="Institutional_Policy",
    y="Weekly_GenAI_Hours"
)

st.plotly_chart(fig, use_container_width=True)

policy_summary = (
    df.groupby("Institutional_Policy")
    .agg(
        Avg_GPA=("Post_Semester_GPA", "mean"),
        Avg_AI_Hours=("Weekly_GenAI_Hours", "mean")
    )
)

st.dataframe(policy_summary)
