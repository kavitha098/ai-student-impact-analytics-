import streamlit as st


def show_kpis(df):

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Students",
        f"{len(df):,}"
    )

    col2.metric(
        "Avg GPA",
        round(
            df["Post_Semester_GPA"].mean(),
            2
        )
    )

    col3.metric(
        "Avg AI Hours",
        round(
            df["Weekly_GenAI_Hours"].mean(),
            1
        )
    )

    col4.metric(
        "Skill Retention",
        round(
            df["Skill_Retention_Score"].mean(),
            1
        )
    )

    burnout_pct = (
        df["Burnout_Risk_Level"]
        .eq("High")
        .mean()
        * 100
    )

    col5.metric(
        "Burnout %",
        f"{burnout_pct:.1f}%"
    )
