import streamlit as st

#Q9. Streamlit Input Interface

st.set_page_config(page_title="Loan Approval Prediction", layout="centered")

st.title("Loan Approval Prediction")

st.write("Enter the applicant details below.")


dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, value=0)

income = st.number_input("Annual Income", min_value=0, value=500000)

loan_amount = st.number_input("Loan Amount", min_value=0, value=1000000)

loan_term = st.number_input("Loan Term (Years)", min_value=1, max_value=30, value=10)

cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900, value=750)

residential_assets = st.number_input("Residential Assets Value", min_value=0, value=1000000)

commercial_assets = st.number_input("Commercial Assets Value", min_value=0, value=500000)

luxury_assets = st.number_input("Luxury Assets Value", min_value=0, value=500000)

bank_assets = st.number_input("Bank Assets Value", min_value=0, value=1000000)


education = st.selectbox(
    "Education",
    [" Graduate", " Not Graduate"]
)

self_employed = st.selectbox(
    "Self Employed",
    [" Yes", " No"]
)

predict = st.button("Predict Loan Status")


import pandas as pd
import joblib

#Q10. Complete Streamlit Web App

model = joblib.load("loan_model.pkl")
scaler = joblib.load("loan_scaler.pkl")
columns = joblib.load("loan_columns.pkl")

if predict:

    input_data = pd.DataFrame({
        "no_of_dependents": [dependents],
        "education": [education],
        "self_employed": [self_employed],
        "income_annum": [income],
        "loan_amount": [loan_amount],
        "loan_term": [loan_term],
        "cibil_score": [cibil_score],
        "residential_assets_value": [residential_assets],
        "commercial_assets_value": [commercial_assets],
        "luxury_assets_value": [luxury_assets],
        "bank_asset_value": [bank_assets]
    })

    input_encoded = pd.get_dummies(input_data)

    input_encoded = input_encoded.reindex(columns=columns, fill_value=0)

    input_scaled = scaler.transform(input_encoded)

    prediction = model.predict(input_scaled)

    if prediction[0] == " Approved":
        st.success("Loan Status : Approved")
    else:
        st.error("Loan Status : Rejected")

