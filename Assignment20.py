import pandas as pd

#Q1. Preparing Features)
# Load your cleaned Ford Car Dataset.
# Separate the dataset into Independent Features X and Dependent Feature
# Y (price).
# Drop the target column from X.
# Print the shape of X and Y.
print("Q1")

df = pd.read_csv(r"c:\Users\PRASANNA\OneDrive\Desktop\ford_car_dataset.csv")

df = df.drop_duplicates()

X = df.drop('price', axis=1)

Y = df['price']

print("Shape of X (Independent Features):", X.shape)
print("Shape of Y (Dependent Feature):", Y.shape)

print()
print("Independent Features:")
print(X.head())

print()
print("Dependent Feature:")
print(Y.head())

# ----------------------------------------------------
# Observations:
# 1. 'price' is selected as the target (dependent) feature.
# 2. All remaining columns are independent features.
# 3. X contains the input variables used for prediction.
# 4. Y contains the output variable (price).
# 5. The printed shapes show the number of samples and features.
# ---------------------------------------------------------------------------

print("\n")

#Q2. One-Hot Encoding)
# Identify all categorical columns in X.
# Perform One-Hot Encoding using pd.get_dummies().
# Convert the encoded data to integer type (astype(int)).
# Show the first 5 rows after encoding.
print("Q2")

categorical_cols = X.select_dtypes(include=['object', 'string']).columns

print("Categorical Columns:")
print(categorical_cols)


X_encoded = pd.get_dummies(X, columns=categorical_cols, drop_first=True)


X_encoded = X_encoded.astype(int)

print()
print("First 5 Rows After One-Hot Encoding:")
print(X_encoded.head())

# ----------------------------------------------------
# Observations:
# 1. Identified all categorical columns in X.
# 2. Applied One-Hot Encoding using pd.get_dummies().
# 3. Converted the encoded data into integer type using astype(int).
# 4. The dataset now contains only numeric values.
# 5. The encoded dataset is suitable for Machine Learning models.
# ------------------------------------------------------------------------------

print("\n")

#Q3. Feature Scaling)
# Apply Standard Scaling on the numerical columns (year, mileage, tax, mpg,
# engineSize).
# Use StandardScaler from sklearn.preprocessing.
# Show the first 5 rows of the scaled features.
print("Q3")


from sklearn.preprocessing import StandardScaler

numeric_cols = ['year', 'mileage', 'tax', 'mpg', 'engineSize']

scaler = StandardScaler()

X_encoded[numeric_cols] = scaler.fit_transform(X_encoded[numeric_cols])

print("First 5 Rows of Scaled Features:")
print(X_encoded[numeric_cols].head())

# ----------------------------------------------------
# Observations:
# 1. StandardScaler transforms numerical features
#    to have a mean of approximately 0 and a
#    standard deviation of 1.
# 2. Only numerical columns were scaled.
# 3. Categorical (One-Hot Encoded) columns were
#    not scaled.
# 4. Feature scaling improves the performance of
#    many Machine Learning algorithms.
# ----------------------------------------------------------------------

print("\n")

#Q4. Train-Test Split)
# Split the preprocessed data into training and testing sets using train_test_split.
# Use test_size=0.33 and random_state=42.
# Print the shape of X_train, X_test, y_train, and y_test.
print("Q4")

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_encoded,
    Y,
    test_size=0.33,
    random_state=42
)

print("Shape of X_train:", X_train.shape)
print("Shape of X_test :", X_test.shape)
print("Shape of y_train:", y_train.shape)
print("Shape of y_test :", y_test.shape)

# ----------------------------------------------------
# Observations:
# 1. The dataset is divided into training and testing sets.
# 2. 67% of the data is used for training and 33% for testing.
# 3. random_state=42 ensures the same split every time the code runs.
# 4. X_train and y_train are used to train the model.
# 5. X_test and y_test are used to evaluate the model.
# --------------------------------------------------------------------------

print("\n")

#Q5. Building Linear Regression Model)
# Train a Linear Regression model using sklearn.
# Fit the model on the training data (X_train, y_train).
# Print the intercept and coefficients of the model.
print("Q5")


from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

print("Intercept:")
print(model.intercept_)

print()

print("Coefficients:")
coef_df = pd.DataFrame({
    "Feature": X_train.columns,
    "Coefficient": model.coef_
})

print(coef_df)

# ----------------------------------------------------
# Observations:
# 1. Linear Regression learns the relationship between
#    input features and the target variable (price).
# 2. The intercept is the predicted price when all
#    feature values are zero.
# 3. Each coefficient shows how much the price changes
#    with a one-unit increase in that feature, while
#    keeping other features constant.
# 4. Positive coefficients increase the predicted price,
#    while negative coefficients decrease it.
# -----------------------------------------------------------------

print("\n")

#Q6. Making Predictions)
# Use the trained model to make predictions on the test data.
# Store predictions in y_pred.
# Print the first 10 predicted values and compare them with the first 10 actual
# values from y_test.
print("Q6")

y_pred = model.predict(X_test)

print("First 10 Predicted Values:")
print(y_pred[:10])

print()

print("First 10 Actual Values:")
print(y_test.head(10).values)

print()

comparison = pd.DataFrame({
    "Actual Price": y_test.values[:10],
    "Predicted Price": y_pred[:10]
})

print("Comparison of Actual and Predicted Values:")
print(comparison)

# ----------------------------------------------------
# Observations:
# 1. The trained Linear Regression model predicts the
#    car prices for the test dataset.
# 2. y_pred stores the predicted prices.
# 3. Comparing actual and predicted values helps
#    evaluate the model's performance.
# 4. Smaller differences between actual and predicted
#    values indicate better prediction accuracy.
# ----------------------------------------------------------------------

print("\n")

#Q7. Model Evaluation using R² Score)
# Calculate the R² score using r2_score(y_test, y_pred).
# Interpret the R² value in your own words.
# Comment on how well the model is performing.
print("Q7")


from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)

print("R² Score :", r2)

# ----------------------------------------------------
# Interpretation:
# 1. R² Score measures how well the Linear Regression
#    model explains the variation in the target variable.
# 2. An R² value closer to 1 indicates better model
#    performance, while a value closer to 0 indicates
#    poor performance.
# 3. A higher R² score means the model predicts car
#    prices more accurately.
#
# Comment:
# If the R² score is high (close to 1), the model is
# performing well. If it is low, the model may need
# more relevant features or a different algorithm to
# improve prediction accuracy.
# ----------------------------------------------------------------------

print("\n")

#Q8. Saving the Model)
# Save your trained model and preprocessing objects using joblib:
# The Linear Regression model → "LR_ford_car.pkl"
# The StandardScaler → "scaler.pkl"
# The list of columns → "columns.pkl"
print("Q8")


import joblib


joblib.dump(model, "LR_ford_car.pkl")

joblib.dump(scaler, "scaler.pkl")

joblib.dump(X_encoded.columns.tolist(), "columns.pkl")

print("Files saved successfully!")
print("1. LR_ford_car.pkl")
print("2. scaler.pkl")
print("3. columns.pkl")

# ----------------------------------------------------
# Observations:
# 1. The trained Linear Regression model is saved as
#    'LR_ford_car.pkl'.
# 2. The StandardScaler is saved as 'scaler.pkl'.
# 3. The feature column names are saved as 'columns.pkl'.
# 4. These files can be loaded later without retraining
#    the model.
# -----------------------------------------------------------------

