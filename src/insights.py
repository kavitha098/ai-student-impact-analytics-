import pandas as pd


def generate_insights(df):

    insights = []

    avg_ai = df["Weekly_GenAI_Hours"].mean()

    insights.append(
        f"Average AI usage is {avg_ai:.1f} hours per week."
    )

    top_major = (
        df.groupby("Major_Category")
        ["Weekly_GenAI_Hours"]
        .mean()
        .idxmax()
    )

    insights.append(
        f"{top_major} students are the heaviest AI users."
    )

    best_skill = (
        df.groupby("Prompt_Engineering_Skill")
        ["Post_Semester_GPA"]
        .mean()
        .idxmax()
    )

    insights.append(
        f"{best_skill} prompt users achieve the highest GPA."
    )

    return insights


def display_insights(st, insights):

    st.success(
        "\n\n".join(
            [f"• {x}" for x in insights]
        )
    )
