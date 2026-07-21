import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#Q1. Data Loading & Preprocessing
print("Q1")

df = pd.read_csv(r"c:\Users\PRASANNA\OneDrive\Desktop\heart.csv")

df = df.drop_duplicates()

df["Cholesterol"] = df["Cholesterol"].astype(float)
df["RestingBP"] = df["RestingBP"].astype(float)

cholesterol_mean = df.loc[df["Cholesterol"] != 0, "Cholesterol"].mean()
restingbp_mean = df.loc[df["RestingBP"] != 0, "RestingBP"].mean()

df.loc[df["Cholesterol"] == 0, "Cholesterol"] = cholesterol_mean
df.loc[df["RestingBP"] == 0, "RestingBP"] = restingbp_mean

X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

X = pd.get_dummies(X, drop_first=True)

columns = X.columns.tolist()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Shape of X :-", X.shape)
print("Shape of y :-", y.shape)

print("\n")

#Q2. Train-Test Split
print("Q2")

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.20,
    random_state=42
)

print("Shape of X_train :-", X_train.shape)
print("Shape of X_test :-", X_test.shape)
print("Shape of y_train :-", y_train.shape)
print("Shape of y_test :-", y_test.shape)

print("\n")


#Q3. Building Logistic Regression Model
#Train a Logistic Regression model.

print("Q3")

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(random_state=42)

model.fit(X_train, y_train)

print("Logistic Regression Model Trained Successfully!")

print("\n")

#Q4. Making Predictions
#Use the trained model to predict on the test data.
#Store predictions in y_pred.
#Print the first 10 actual values (y_test) and predicted values (y_pred).

print("Q4")

y_pred = model.predict(X_test)

print("First 10 Actual Values :-")
print(y_test.iloc[:10].values)

print()

print("First 10 Predicted Values :-")
print(y_pred[:10])

print("\n")

#Q5. Confusion Matrix
#Create a Confusion Matrix using confusion_matrix(y_test, y_pred).
#Display the matrix.
#Label TN, FP, FN, and TP in the output.

print("Q5")

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix :-")
print(cm)

print()

print("TN (True Negative)  :-", cm[0][0])
print("FP (False Positive) :-", cm[0][1])
print("FN (False Negative) :-", cm[1][0])
print("TP (True Positive)  :-", cm[1][1])

print("\n")

#Q6. Model Evaluation Metrics
#Calculate Accuracy, Precision, Recall, F1 Score
#Print the Classification Report

print("Q6")

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy :-", accuracy)
print("Precision :-", precision)
print("Recall :-", recall)
print("F1 Score :-", f1)

print()

print("Classification Report :-")
print(classification_report(y_test, y_pred))

print("\n")

#Q7. Saving the Model
#Save the trained model and preprocessing objects using joblib.


print("Q7")

import joblib

joblib.dump(model, "heart_model.pkl")

joblib.dump(scaler, "heart_scaler.pkl")

joblib.dump(columns, "heart_columns.pkl")

print("Heart Disease Model Saved Successfully!")
print("Heart Disease Scaler Saved Successfully!")
print("Heart Disease Columns Saved Successfully!")

print("\n")

#Q8. Loading & Testing Saved Model
#Load the saved model and objects.
#Create sample input data (one patient record).
#Preprocess the input (encoding + scaling).
#Make a prediction using the loaded model and print the result.

print("Q8")

import joblib
import pandas as pd

loaded_model = joblib.load("heart_model.pkl")
loaded_scaler = joblib.load("heart_scaler.pkl")
loaded_columns = joblib.load("heart_columns.pkl")

sample_data = pd.DataFrame({
    "Age": [45],
    "RestingBP": [130],
    "Cholesterol": [230],
    "FastingBS": [0],
    "MaxHR": [150],
    "Oldpeak": [1.0],
    "Sex": ["M"],
    "ChestPainType": ["ATA"],
    "RestingECG": ["Normal"],
    "ExerciseAngina": ["N"],
    "ST_Slope": ["Up"]
})

sample_encoded = pd.get_dummies(sample_data)

sample_encoded = sample_encoded.reindex(columns=loaded_columns, fill_value=0)

sample_scaled = loaded_scaler.transform(sample_encoded)

prediction = loaded_model.predict(sample_scaled)

print("Prediction Result :-")

if prediction[0] == 1:
    print("Heart Disease : Yes")
else:
    print("Heart Disease : No")

print("\n")

