import pandas as pd
import matplotlib.pyplot as plt

#Q1. Load the Heart Disease dataset using pandas and display the first 10 rows.
# Also check the shape and basic information (info()) of the dataset.
print("Q1")

df = pd.read_csv(r"c:\Users\PRASANNA\OneDrive\Desktop\heart.csv")

print("First 10 Rows :- ")
print(df.head(10))

print()
print("Shape of Dataset :- ")
print(df.shape)

print()
print("Dataset Informantion :- ")
df.info()

print("\n")
#Q2. Check for missing values in the dataset. Show the count of null values for
# each column.
print("Q2")

print("Missing Values in each Column :- ")
print(df.isnull().sum())

print("\n")
#Q3. Check for duplicate rows in the dataset. If any duplicates are found, remove
# them and print the new shape of the dataset.
print("Q3")
Duplicates =  df.duplicated().sum()

print("Numbers of Duplicates Rows :- ", Duplicates)

df = df.drop_duplicates()

print("New Shape of Dataset :- ", df.shape)

print("\n")
#Q4. Identify unrealistic/invalid values:
# Count how many rows have Cholesterol = 0.
# Count how many rows have RestingBP  0.
print("Q4")

cholesterol_zero = (df["Cholesterol"] == 0).sum()
print("Rows with Cholesterol = 0 :- ", cholesterol_zero)

restingbp_zero = (df["RestingBP"] == 0).sum()
print("Rows with RestingBP = 0 :- ", restingbp_zero)


print("\n")
#Q5. Clean the invalid values:
# Replace Cholesterol = 0 with the mean cholesterol value (excluding zeros).
# Replace RestingBP  0 with the mean resting blood pressure value (excluding
# zeros).
# Round both columns to 2 decimal places.
# Print the statistical summary (describe()) of these two columns before and after
# cleaning.
print("Q5")

df["Cholesterol"] = df["Cholesterol"].astype(float)
df["RestingBP"] = df["RestingBP"].astype(float)

print("Before Cleaning:")
print()
print(df[["Cholesterol", "RestingBP"]].describe())

cholesterol_mean = df.loc[df["Cholesterol"] != 0, "Cholesterol"].mean()

restingbp_mean = df.loc[df["RestingBP"] != 0, "RestingBP"].mean()

df.loc[df["Cholesterol"] == 0, "Cholesterol"] = cholesterol_mean

df.loc[df["RestingBP"] == 0, "RestingBP"] = restingbp_mean

df["Cholesterol"] = df["Cholesterol"].round(2)

df["RestingBP"] = df["RestingBP"].round(2)

print()
print("After Cleaning:")
print()
print(df[["Cholesterol", "RestingBP"]].describe())


print("\n")
#Q6. Create a function to plot histograms for the following numerical columns:
#Age
#RestingBP
#Cholesterol
#MaxHR
#Plot all four histograms in one figure using subplots 2 2 layout). Use this function
#to visualize the data after cleaning.
print("Q6")

def plot_histograms(data):
    columns = ["Age", "RestingBP", "Cholesterol", "MaxHR"]

    plt.figure(figsize=(12, 8))

    for i, column in enumerate(columns, 1):
        plt.subplot(2, 2, i)
        plt.hist(data[column],bins=15, edgecolor="black")
        plt.title(f"Q6 :- Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()

plot_histograms(df)


print("\n")
#Q7. Identify and print numerical columns and categorical columns separately.
print("Q7")

numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns

categorical_columns = df.select_dtypes(include=["object"]).columns

print("Numerical Columns :- ")
print(list(numerical_columns))

print()

print("Categorical Columns :- ")
print(list(categorical_columns))


print("\n")
#Q8. Perform One-Hot Encoding on all categorical columns using
#pd.get_dummies().
#Store the result in a new dataframe called df_encoded.
#Print the shape and the first 5 rows of the encoded dataframe.
print("Q8")


df_encoded = pd.get_dummies(df, columns=categorical_columns)

print("Shape of Encoded DataFrame:")
print(df_encoded.shape)

print()

print("First 5 Rows of Encoded DataFrame:")
print(df_encoded.head())


print("\n")
#Q9. After cleaning and encoding:
#Print the final shape of df_encoded.
#Show the list of all column names in the final dataframe.
print("Q9")

print("Final Shape of df_encoded :- ")
print(df_encoded.shape)

print()

print("Column Name in df_encoded :- ")
print(df_encoded.columns.tolist())


print("\n")
#Q10. Summary)
#Write a short summary (in comments or markdown) covering:
#What invalid values did you find and how did you fix them?
#Why is it important to handle invalid values like Cholesterol = 0?
#What is the purpose of One-Hot Encoding?
#Any other observations from the cleaning process.

#-------------------------------------------------------------------------------
# Q10 Summary

# 1. We found 172 Cholesterol values and 1 RestingBP value equal to 0.
#    These values were replaced with the mean value of the respective column.

# 2. Invalid values can affect data analysis and machine learning results.
#    Cleaning them improves the quality of the dataset.

# 3. One-Hot Encoding converts categorical columns into numerical columns
#    so that machine learning algorithms can use them.

# 4. The dataset had no missing values and no duplicate rows.
#    After cleaning and encoding, the data became ready for analysis.

#-----------------------------------------------------------------------------------------




