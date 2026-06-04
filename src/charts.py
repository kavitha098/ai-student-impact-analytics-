import plotly.express as px


def ai_usage_histogram(df):

    return px.histogram(
        df,
        x="Weekly_GenAI_Hours",
        nbins=40,
        title="AI Usage Distribution"
    )


def gpa_improvement_chart(df):

    return px.box(
        df,
        x="Prompt_Engineering_Skill",
        y="GPA_Improvement",
        color="Prompt_Engineering_Skill",
        title="Prompt Skill vs GPA Gain"
    )


def skill_retention_scatter(df):

    return px.scatter(
        df,
        x="Perceived_AI_Dependency",
        y="Skill_Retention_Score",
        color="Burnout_Risk_Level",
        trendline="ols",
        title="Dependency vs Skill Retention"
    )


def burnout_pie(df):

    burnout = (
        df["Burnout_Risk_Level"]
        .value_counts()
        .reset_index()
    )

    return px.pie(
        burnout,
        names="Burnout_Risk_Level",
        values="count",
        title="Burnout Distribution"
    )


def policy_violin(df):

    return px.violin(
        df,
        x="Institutional_Policy",
        y="Post_Semester_GPA",
        color="Institutional_Policy",
        box=True
    )
