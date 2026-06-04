import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/ai_student_impact_dataset.csv")

st.title("🎓 GPA Impact Analysis")

df["GPA_Improvement"] = (
    df["Post_Semester_GPA"]
    - df["Pre_Semester_GPA"]
)

fig = px.histogram(
    df,
    x="GPA_Improvement",
    nbins=40,
    title="GPA Improvement Distribution"
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.box(
    df,
    x="Prompt_Engineering_Skill",
    y="GPA_Improvement",
    color="Prompt_Engineering_Skill",
    title="Prompt Skill vs GPA Gain"
)

st.plotly_chart(fig2, use_container_width=True)

corr = df[
    ["Weekly_GenAI_Hours", "GPA_Improvement"]
].corr().iloc[0, 1]

st.metric(
    "Correlation",
    round(corr, 3)
)
