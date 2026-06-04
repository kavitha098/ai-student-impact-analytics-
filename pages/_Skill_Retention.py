import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/ai_student_impact_dataset.csv")

st.title("🧠 Skill Retention Analytics")

fig = px.scatter(
    df,
    x="Perceived_AI_Dependency",
    y="Skill_Retention_Score",
    color="Burnout_Risk_Level",
    trendline="ols"
)

st.plotly_chart(fig, use_container_width=True)

fig = px.box(
    df,
    x="Prompt_Engineering_Skill",
    y="Skill_Retention_Score",
    color="Prompt_Engineering_Skill"
)

st.plotly_chart(fig, use_container_width=True)

st.metric(
    "Average Retention",
    round(
        df["Skill_Retention_Score"].mean(),
        1
    )
)
