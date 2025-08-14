import pandas as pd

df = pd.read_csv("dataset/MH1.csv")
df.head()
df.info()
df.isnull().sum()
df.describe()
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


# Split
X = df.drop('treatment ', axis=1)
y = df['treatment ']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

import joblib
joblib.dump(model, "../models/mental_health_model.pkl")
#joblib.dump(label_enc, "../models/label_encoder.pkl")

import streamlit as st
import pandas as pd
import joblib

st.title("Mental Health Risk Predictor")

model = joblib.load("mental_health_model.pkl")

# User inputs
age = st.number_input("Age", 18, 100)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
remote_work = st.selectbox("Do you work remotely?", ["Yes", "No"])

if st.button("Predict"):
    # Manually map inputs to match Excel encoding
    gender_map = {"Male": 1, "Female": 2, "Other": 3}
    remote_map = {"No": 2, "Yes": 1}

    input_df = pd.DataFrame([[age, gender_map[gender], remote_map[remote_work]]],
                            columns=["Age", "Gender", "remote_work"])

    pred = model.predict(input_df)[0]
    st.write("Prediction:", "At Risk" if pred == 1 else "Not at Risk")

    import os
print(os.getcwd())