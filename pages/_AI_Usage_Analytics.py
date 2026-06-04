import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/ai_student_impact_dataset.csv")

st.title("🤖 AI Usage Analytics")

fig = px.histogram(
    df,
    x="Weekly_GenAI_Hours",
    color="Year_of_Study",
    marginal="box"
)

st.plotly_chart(fig, use_container_width=True)

fig = px.treemap(
    df,
    path=["Major_Category"],
    values="Weekly_GenAI_Hours",
    title="AI Usage by Major"
)

st.plotly_chart(fig, use_container_width=True)

fig = px.violin(
    df,
    x="Year_of_Study",
    y="Weekly_GenAI_Hours"
)

st.plotly_chart(fig, use_container_width=True)
