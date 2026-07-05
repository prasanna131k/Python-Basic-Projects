# Assignment 16 
# whatever i do in that Assignment program...!


import pandas as pd
# Manga Dataset - data reading. Loading. exploring and Understanding the data.


# Load The Manga Dataset
df = pd.read_csv(r"c:\Users\PRASANNA\OneDrive\Documents\data_set\manga_dataset.csv")

# Display the first 5 rows of the dataset.
print("Display the first 5 rows of the dataset.  ")
print(df.head())

# Display the last 5 rows of the dataset.
print()
print("Display the last 5 rows of the dataset.  ")
print(df.tail())

# Display the number of rows and columns.
print()
print("Number of rows and columns:")
print(df.shape)

# Display all the column names in the dataset.
print()
print("Column Names:-")
print(df.columns.tolist())

# Display the dataset information.
print()
print("Dataset Information:")
print(df.info())

# Generate summary statistics for numerical columns.
print()
print("Summary statistics for numerical columns:")
print(df.describe())

# Display the data type of all columns in the dataset.
print()
print("Data types of all columns:")
print(df.dtypes)

# Count the number of missing values in each column.
print()
print("Count of missing values in each column:")
print(df.isnull().sum())

# Count the number of unique values in each column.
print()
print("Count of unique values in each column:")
print(df.nunique())

# Display 5 random rows from the dataset.
print()
print("Display 5 random rows from the dataset:")
print(df.sample(5))

# Display value counts for the 'title_english' column.
print()
print("Value counts for the 'title_english' column:")
print(df['title_english'].value_counts())

# Display value counts for the 'title_japanese' column.
print()
print("Value counts for the 'title_japanese' column:")
print(df['title_japanese'].value_counts())


# Display value counts for the 'chapters' column.
print()
print("Value counts for the 'chapters' column:")
print(df['chapters'].value_counts())
