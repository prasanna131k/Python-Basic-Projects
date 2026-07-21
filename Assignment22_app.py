import streamlit as st

#Q9. Streamlit Input Interface

st.set_page_config(page_title="Heart Disease Prediction", layout="centered")

st.title("Heart Disease Prediction")
st.write("Enter Patient Details")


age = st.number_input("Age", min_value=1, max_value=120, value=40)

sex = st.selectbox("Sex", ["M", "F"])

chest_pain = st.selectbox(
    "Chest Pain Type",
    ["ATA", "NAP", "ASY", "TA"]
)

resting_bp = st.number_input("Resting Blood Pressure", min_value=0, value=120)

cholesterol = st.number_input("Cholesterol", min_value=0, value=200)

fasting_bs = st.selectbox("Fasting Blood Sugar", [0, 1])

resting_ecg = st.selectbox(
    "Resting ECG",
    ["Normal", "ST", "LVH"]
)

max_hr = st.number_input("Maximum Heart Rate", min_value=60, max_value=250, value=150)

exercise_angina = st.selectbox(
    "Exercise Angina",
    ["N", "Y"]
)

oldpeak = st.number_input("Oldpeak", value=0.0)

st_slope = st.selectbox(
    "ST Slope",
    ["Up", "Flat", "Down"]
)


predict = st.button("Predict")


import pandas as pd
import joblib

#Q10. Complete Streamlit Web App

# Load Saved Model and Preprocessing Objects
model = joblib.load("heart_model.pkl")
scaler = joblib.load("heart_scaler.pkl")
columns = joblib.load("heart_columns.pkl")

if predict:

    input_data = pd.DataFrame({
        "Age": [age],
        "RestingBP": [resting_bp],
        "Cholesterol": [cholesterol],
        "FastingBS": [fasting_bs],
        "MaxHR": [max_hr],
        "Oldpeak": [oldpeak],
        "Sex": [sex],
        "ChestPainType": [chest_pain],
        "RestingECG": [resting_ecg],
        "ExerciseAngina": [exercise_angina],
        "ST_Slope": [st_slope]
    })

    input_encoded = pd.get_dummies(input_data)

    input_encoded = input_encoded.reindex(columns=columns, fill_value=0)

    input_scaled = scaler.transform(input_encoded)

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("Heart Disease : Yes")
    else:
        st.success("Heart Disease : No")


