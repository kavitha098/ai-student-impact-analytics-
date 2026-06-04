import pandas as pd


def preprocess_data(df: pd.DataFrame):

    df = df.copy()

    # GPA Improvement
    if (
        "Pre_Semester_GPA" in df.columns
        and "Post_Semester_GPA" in df.columns
    ):
        df["GPA_Improvement"] = (
            df["Post_Semester_GPA"]
            - df["Pre_Semester_GPA"]
        )

    # AI Usage Category
    if "Weekly_GenAI_Hours" in df.columns:

        df["AI_Usage_Level"] = pd.cut(
            df["Weekly_GenAI_Hours"],
            bins=[0, 5, 10, 20, 100],
            labels=[
                "Low",
                "Moderate",
                "High",
                "Very High"
            ]
        )

    return df
