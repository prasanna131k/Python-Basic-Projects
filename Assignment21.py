#Q1. Setup and Libraries)
# Create a new Python file named app.py.
# Import the required libraries: streamlit, pandas, and joblib.
# Write comments explaining the purpose of each library.
print("Q1")

# Streamlit is used to create the web application interfaace
import streamlit as st

# Pandas is used to work with data in DataFrame format.
import pandas as pd

# Joblib is used to load the seved machine learning model and preprocessing files.
import joblib

print("All required libraries imported successfully!")

print("-----------------------------------------------------------------------")

print("\n")
#Q2. Loading Model and Preprocessing Objects)
# Write code to load the saved files:
# LR_model.pkl (trained model)
# scaler.pkl StandardScaler)
# columns.pkl (encoded column names)
# Use joblib.load() and store them in variables model, scaler, and encoded_columns.
print("Q2")

model = joblib.load("LR_ford_car.pkl")

scaler = joblib.load("scaler.pkl")

encode_columns = joblib.load("columns.pkl")

print("Model, Scaler, and Encoded Columns loaded successfully!")

print("-------------------------------------------------------------------------")

print("\n")
#Q3. Page Configuration)
# Configure the Streamlit page using st.set_page_config().
# Set page_title as "Ford Car Price Predictor".
# Set layout as "centered".
# Add a comment explaining why these settings are used.
print("Q3")

# Configure the Streamlit page.
# page_title sets the title shown in the browser tab.
# layout="centered" keeps the app content centered for a clean and simple interface.

st.set_page_config(
    page_title="Ford Car Price Predictor",
    layout="centered"
)

print("--------------------------------------------------------------------------")

print("\n")
#Q4. Title and Description)
# Display:
# A main title using st.title().
# A short description using st.write().
# Example: "Enter the car details below to predict its selling price."
print("Q4")

st.title("Ford Car Price Predictor")
st.write("Enter the car details below to predict its selling price.")

print("--------------------------------------------------------------------------")

print("\n")
#Q5. Numerical Input Fields)
# Create input fields using st.number_input() for the following:
# Manufacturing Year (year)
# Mileage
# Road Tax (tax)
# MPG
# Engine Size
# Set appropriate min_value, max_value, and default value.
print("Q5")

# Manufacturing Year
year = st.number_input(
    "Manufacturing Year",
    min_value=1996,
    max_value=2025,
    value=2018
)

# Mileage
mileage = st.number_input(
    "Mileage",
    min_value=0,
    max_value=300000,
    value=20000
)

# Road Tax 
tax = st.number_input(
    "Road Tax",
    min_value=0,
    max_value=600,
    value=145
)

# MPG
mpg = st.number_input(
    "MPG",
    min_value=0.0,
    max_value=150.0,
    value=55.0
)

# Engine Size
engineSize = st.number_input(
    "Engine Size",
    min_value=0.0,
    max_value=6.0,
    value=1.5
)

print("------------------------------------------------------------------------")

print("\n")
#Q6. Categorical Input using Dropdowns)
# Create dropdowns using st.selectbox() for:
# Transmission Automatic, Manual, Semi-Auto)
# Fuel Type Petrol, Diesel, Hybrid, etc.)
# Add comments explaining the advantage of using selectbox.
print("Q6")

# Selectbox is used to display a dropdown list.
# It prevents invalid user input and allows users to choose only valid outputs.

# Transmission dropdown
transmission = st.selectbox(
    "Transmission",
    ["Automatic", "Manual", "Semi-Auto"]
)

# Fuel Type dropdown
fuelType = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "Electric"]
)

print("----------------------------------------------------------------------")

print("\n")
#Q7. Text Input and Predict Button)
# Take car model name using st.text_input().
# Create a Predict Price button using st.button().
print("Q7")

# Create a button to start the price prediction.
model_name = st.text_input("Enter car Model Name...")

# Create a button to start the price prediction.
predic_button = st.button("Predict Price...")

print("------------------------------------------------------------------------")

print("\n")
#Q8. Creating Input DataFrame & Encoding)
# When the Predict button is clicked:
# Create a pandas DataFrame from user inputs.
# Perform One-Hot Encoding using pd.get_dummies().
# Align the columns with the training columns (encoded_columns).
print("Q8")

if predic_button:

    # Create DataFrame from user inputs
    input_data = pd.DataFrame({
        "model": [model_name],
        "year": [year],
        "transmission": [transmission],
        "mileage": [mileage],
        "fuelType": [fuelType],
        "tax": [tax],
        "mpg": [mpg],
        "engineSize": [engineSize]
    })

    # Perform One-Hot Encoding
    input_encoded = pd.get_dummies(input_data)

    # Align columns with training data
    input_encoded = input_encoded.reindex(
        columns=encode_columns,
        fill_value=0
    )

    # Display the encoded input
    st.write("Encoded Input Data :-")
    st.dataframe(input_encoded)

    print("-----------------------------------------------------------------------------")
    print("\n")

    #Q9. Feature Scaling and Prediction)
    # Identify numerical columns and apply the loaded scaler.
    # Make prediction using the loaded model.
    # Display the predicted price.
    print("Q9")

    # Identify numerical columns
    numerical_columns = ["year", "mileage", "tax", "mpg", "engineSize"]

    # Apply the loaded StandardScaler
    input_encoded[numerical_columns] = scaler.transform(
        input_encoded[numerical_columns]
    )
    try:
        # Make prediction using the trained model
        predicted_price = model.predict(input_encoded)

        # Display the predicted price
        st.success(f" Predicted Car Price : £{predicted_price[0]:,.2f}")
    except Exception as e :
        st.error(f"Error : (e)")

print("-----------------------------------------------------------------------------")

# Q10. Mini Project Summary
# This Streamlit application predicts the selling price of a Ford car.
# The user enters the car details, the data is encoded and scaled,
# and the trained Linear Regression model predicts the price.
# The predicted price is displayed in a user-friendly format.


