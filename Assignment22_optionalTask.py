import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#Q1. Data Loading & Preprocessing
#Load the Loan Approval dataset.
#Separate features into X and y.
#Perform necessary preprocessing.

print("Q1")

df = pd.read_csv(r"c:\Users\PRASANNA\Downloads\loan_approval_dataset_1.csv")

df.columns = df.columns.str.strip()

df = df.drop_duplicates()

print("Missing Values :-")
print(df.isnull().sum())

print()

X = df.drop(["loan_id", "loan_status"], axis=1)
y = df["loan_status"]

X = pd.get_dummies(X, drop_first=True)

columns = X.columns.tolist()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Shape of X :-", X.shape)
print("Shape of y :-", y.shape)

print()
print("First 5 Rows of Encoded Features :-")
print(X.head())

print("\n")


#Q2. Train-Test Split
#Split the preprocessed data into training and testing sets.

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
#Print the first 10 actual values and predicted values.

print("Q4")

y_pred = model.predict(X_test)

print("First 10 Actual Values :-")
print(y_train.iloc[:10].values)

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

TN = cm[0][0]
FP = cm[0][1]
FN = cm[1][0]
TP = cm[1][1]

print("True Negative (TN)  :-", TN)
print("False Positive (FP) :-", FP)
print("False Negative (FN) :-", FN)
print("True Positive (TP)  :-", TP)

print("\n")

#Q6. Model Evaluation Metrics
#Calculate Accuracy, Precision, Recall, F1 Score.
#Print the Classification Report.

print("Q6")

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label=" Approved")
recall = recall_score(y_test, y_pred, pos_label=" Approved")
f1 = f1_score(y_test, y_pred, pos_label=" Approved")

print("Accuracy  :-", accuracy)
print("Precision :-", precision)
print("Recall    :-", recall)
print("F1 Score  :-", f1)

print()

print("Classification Report :-")
print(classification_report(y_test, y_pred))

print("\n")


#Q7. Saving the Model
#Save the trained model and preprocessing objects.

print("Q7")

import joblib

joblib.dump(model, "loan_model.pkl")

joblib.dump(scaler, "loan_scaler.pkl")

joblib.dump(columns, "loan_columns.pkl")

print("Model Saved Successfully! (loan_model.pkl)")
print("Scaler Saved Successfully! (loan_scaler.pkl)")
print("Columns Saved Successfully! (loan_columns.pkl)")

print("\n")


#Q8. Loading & Testing Saved Model
#Load the saved model and preprocessing objects.
#Create sample input data.
#Preprocess the input.
#Make a prediction.

print("Q8")

loaded_model = joblib.load("loan_model.pkl")
loaded_scaler = joblib.load("loan_scaler.pkl")
loaded_columns = joblib.load("loan_columns.pkl")

print("Model Loaded Successfully!")
print("Scaler Loaded Successfully!")
print("Columns Loaded Successfully!")

print()

sample_data = pd.DataFrame({
    "no_of_dependents": [2],
    "education": [" Graduate"],
    "self_employed": [" No"],
    "income_annum": [6000000],
    "loan_amount": [15000000],
    "loan_term": [15],
    "cibil_score": [750],
    "residential_assets_value": [5000000],
    "commercial_assets_value": [3000000],
    "luxury_assets_value": [4000000],
    "bank_asset_value": [2000000]
})

sample_encoded = pd.get_dummies(sample_data)

sample_encoded = sample_encoded.reindex(columns=loaded_columns, fill_value=0)

sample_scaled = loaded_scaler.transform(sample_encoded)

prediction = loaded_model.predict(sample_scaled)

print()
print("Prediction Result :-", prediction[0])

if prediction[0] == " Approved":
    print("Loan Status : Approved")
else:
    print("Loan Status : Rejected")

print("\n")


