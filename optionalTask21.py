# Q1. Setup and Libraries
# Import the required libraries:
# streamlit, pandas and joblib.

print("Q1")

# Streamlit is used to create the web application.
import streamlit as st

# Pandas is used to create and manipulate DataFrames.
import pandas as pd

# Joblib is used to load the trained machine learning model.
import joblib

print("All required libraries imported successfully!")

print("------------------------------------------------------------")

print("\n")


# Q2. Loading Model and Preprocessing Objects
# Load the trained model, scaler and encoded columns.

print("Q2")

model = joblib.load("manga_model.pkl")

scaler = joblib.load("manga_scaler.pkl")

encoded_columns = joblib.load("manga_columns.pkl")

print("Model Loaded Successfully!")
print("Scaler Loaded Successfully!")
print("Encoded Columns Loaded Successfully!")

print("------------------------------------------------------------")

print("\n")


# Q3. Page Configuration
# Configure the Streamlit page.

print("Q3")

# Configure the Streamlit page.
# page_title sets the browser title.
# layout="centered" keeps the page neat and easy to use.

st.set_page_config(
    page_title="Manga Score Predictor",
    layout="centered"
)

print("Page Configured Successfully!")

print("------------------------------------------------------------")

print("\n")

# Q4. Title and Description
# Display the application title and a short description.
print("Q4")

st.title("Manga Score Predictor")

st.write(
    "Enter the manga details below to predict its score using the trained Machine Learning model."
)

print("---------------------------------------------------------------------")
print("\n")

# ==========================================================
# Q5. Numerical Input Fields
# Create number input fields for important numerical features.
# ==========================================================

print("Q5")

chapters = st.number_input(
    "Number of Chapters",
    min_value=1,
    max_value=7000,
    value=10
)

volumes = st.number_input(
    "Number of Volumes",
    min_value=1,
    max_value=250,
    value=1
)

members = st.number_input(
    "Members",
    min_value=0,
    max_value=1000000,
    value=1000
)

favorites = st.number_input(
    "Favorites",
    min_value=0,
    max_value=200000,
    value=10
)

scored_by = st.number_input(
    "Scored By",
    min_value=0,
    max_value=500000,
    value=500
)

rank = st.number_input(
    "Rank",
    min_value=1,
    max_value=60000,
    value=1000
)

popularity = st.number_input(
    "Popularity",
    min_value=1,
    max_value=90000,
    value=1000
)

print("------------------------------------------------------------")

print("\n")

# ==========================================================
# Q6. Categorical Input Fields
# ==========================================================

print("Q6")

type_value = st.selectbox(
    "Type",
    [
        "Manga",
        "Light Novel",
        "Manhwa",
        "Manhua",
        "Novel",
        "One-shot"
    ]
)

status_value = st.selectbox(
    "Status",
    [
        "Finished",
        "Publishing",
        "On Hiatus"
    ]
)

publishing_value = st.selectbox(
    "Publishing",
    [True, False]
)

print("------------------------------------------------------------")

print("\n")

# ==========================================================
# Q7. Predict Button
# ==========================================================

print("Q7")

predict_button = st.button("Predict Manga Score")

print("------------------------------------------------------------")

print("\n")

# ==========================================================
# Q8. Create Input DataFrame & Encode
# ==========================================================

print("Q8")

if predict_button:

    input_data = pd.DataFrame({
        "chapters": [chapters],
        "volumes": [volumes],
        "publishing": [publishing_value],
        "scored_by": [scored_by],
        "rank": [rank],
        "popularity": [popularity],
        "members": [members],
        "favorites": [favorites],
        "type": [type_value],
        "status": [status_value]
    })

    input_encoded = pd.get_dummies(input_data)

    input_encoded = input_encoded.reindex(
        columns=encoded_columns,
        fill_value=0
    )

    st.write("Encoded Input Data")
    st.dataframe(input_encoded.head())
    input_encoded = input_encoded.reindex(
        columns=encoded_columns,
        fill_value=0
    )

    # Display encoded input
    st.write("Encoded Input Data")
    st.dataframe(input_encoded)

    print("------------------------------------------------------------")
    print("\n")

# ==========================================================
# Q9. Feature Scaling and Prediction
# Apply StandardScaler and predict the manga score.
# ==========================================================

    print("Q9")

    # Apply the loaded scaler
    input_scaled = scaler.transform(input_encoded)

    try:

    # Predict manga score
        predicted_score = model.predict(input_scaled)

     # Display prediction
        st.success(
            f"⭐ Predicted Manga Score : {predicted_score[0]:.2f}"
        )

    except Exception as e:

        st.error(f"Error : {e}")

print("------------------------------------------------------------")

print("\n")

# ------------------------------------------------------------
# Q10. Mini Project Summary
#
# This Streamlit application predicts the score of a manga
# using the trained Linear Regression model.
#
# The user enters manga details such as chapters, volumes,
# popularity, rank, members, favorites and other features.
#
# The application preprocesses the input, performs One-Hot
# Encoding, aligns the columns with the training dataset,
# applies Standard Scaling, and finally predicts the manga score.
#
# The predicted score is displayed in a simple and user-friendly
# interface using Streamlit.
# ------------------------------------------------------------


