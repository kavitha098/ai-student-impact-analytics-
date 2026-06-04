from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


def train_burnout_model(df):

    features = [
        "Weekly_GenAI_Hours",
        "Traditional_Study_Hours",
        "Perceived_AI_Dependency",
        "Anxiety_Level_During_Exams"
    ]

    X = df[features]

    y = df["Burnout_Risk_Level"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=10,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    report = classification_report(
        y_test,
        predictions,
        output_dict=True
    )

    matrix = confusion_matrix(
        y_test,
        predictions
    )

    return {
        "model": model,
        "accuracy": accuracy,
        "report": report,
        "matrix": matrix,
        "features": features
    }


def predict_burnout(
    model,
    weekly_ai_hours,
    study_hours,
    dependency,
    anxiety
):

    prediction = model.predict(
        [[
            weekly_ai_hours,
            study_hours,
            dependency,
            anxiety
        ]]
    )

    return prediction[0]
