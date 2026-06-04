import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/ai_student_impact_dataset.csv")

st.title("🔥 Burnout Risk Analytics")

burnout = (
    df["Burnout_Risk_Level"]
    .value_counts()
    .reset_index()
)

fig = px.pie(
    burnout,
    names="Burnout_Risk_Level",
    values="count"
)

st.plotly_chart(fig, use_container_width=True)

fig = px.scatter(
    df,
    x="Weekly_GenAI_Hours",
    y="Anxiety_Level_During_Exams",
    color="Burnout_Risk_Level"
)

st.plotly_chart(fig, use_container_width=True)

fig = px.box(
    df,
    x="Burnout_Risk_Level",
    y="Weekly_GenAI_Hours"
)

st.plotly_chart(fig, use_container_width=True)
