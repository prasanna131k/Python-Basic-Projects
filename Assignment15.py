

import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv(r"C:\Users\PRASANNA\OneDrive\Desktop\Countries.csv")

# First 5 rows
print("Display the first 5 rows of the dataset. ")
print(df.head())

print()
# Last 5 rows
print("Display the last 5 rows of the dataset. ")
print(df.tail())

print()
# Shape
print("Show the number of rows and columns. ")
print(df.shape)

print()
# Column names
print("Column Names:")
print(df.columns)

print()
# Dataset information
print("Dataset Information:")
df.info()

print()
# Summary statistics
print("Generate summary statistics for numerical columns. ")
print(df.describe())

print()
# Data types
print("Display the data type of each column. ")
print(df.dtypes)

print()
# Missing values
print("Count missing values in each column. ")
print(df.isnull().sum())

print()
# Unique values
print("Count unique values in each column. ")
print(df.nunique())

print()
# Random 5 rows
print("Display 5 random rows from the dataset. ")
print(df.sample(5))

print()
# Count countries in each region
print("Count countries in each region. ")
print(df["region"].value_counts())


