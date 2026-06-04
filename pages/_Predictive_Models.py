import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

df = pd.read_csv(
    "data/ai_student_impact_dataset.csv"
)

st.title("🤖 Predictive Analytics")

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
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

preds = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    preds
)

st.metric(
    "Model Accuracy",
    f"{accuracy:.2%}"
)

st.subheader("Feature Importance")

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

st.dataframe(
    importance.sort_values(
        "Importance",
        ascending=False
    )
)

st.subheader("Confusion Matrix")

cm = confusion_matrix(
    y_test,
    preds
)

st.write(cm)

st.subheader("Classification Report")

st.text(
    classification_report(
        y_test,
        preds
    )
)
