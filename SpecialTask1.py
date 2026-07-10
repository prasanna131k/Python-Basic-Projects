# Special Task anime Dataset Analysis


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"c:\Users\PRASANNA\OneDrive\Documents\data_set\anime_dataset.csv")

print("First 5 Rows :-  ")
print(df.head)
print()

print("----------------------------------------------------------------------------------------------------------------------------------------------------")

print()
print("Shape of Dataset :- ")
print(df.shape)
print()

print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")

print()
print("Dataset Information :- ")
print(df.info())
print()

print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print()
print("Statistical Summary :- ")
print(df.describe())
print()

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")

print()
print("Columns :- ")
print(df.columns)
print()

print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print()
print("Missing Values :- ")
print(df.isnull().sum())
print()

print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print()
print("Duplicate Rows :- ")
print(df.duplicated().sum())
print()

print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print()
print("Numerical Columns :- ")
print(df.select_dtypes(include=np.number).columns)
print()

print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print()
print("Categorical Columns :- ")
print(df.select_dtypes(include=["object", "string"]).columns)
print()

print("===========================================================================================================================================================")

print()
print("1 :- Distribution of anime Scores :- ")
plt.figure(figsize=(8,5))
sns.histplot(df["score"].dropna(), bins=20)
plt.title("1 :- Distribution  of Anime Scores ")
plt.xlabel("Type")
plt.ylabel("COunt")
plt.show()
print()

print("==================================================================================================================================================================================")

print()
print("2 :- Top 10 Anime Types ")
plt.figure(figsize=(8,5))
df["type"].value_counts().head(10).plot(kind="bar")
plt.title("2 :- Top Anime Types ")
plt.xlabel("Type")
plt.ylabel("count")
plt.show()
print()

print("=========================================================================================================================================================================")

print()
print("3 :- Correlation Heatmap")
plt.figure(figsize=(10,8))
numeric_df = df.select_dtypes(include=np.number)
sns.heatmap(numeric_df.corr(), cmap=("coolwarm"), annot=True)
plt.title("3 :- Correlation Heatmap")
plt.show()
print()

print("====================================================================================================================================================================================")

print()
print("4 :- Top 10 Geners ")
plt.figure(figsize=(10,5))
df["genres"].value_counts().head(10).plot(kind="bar")
plt.title("4 :- Top 10 Genres ")
plt.xlabel("Genres")
plt.ylabel("count")
plt.xticks(rotation=45)
plt.show()
print()

print("==================================================================================================================================================================================")

print()
print("5 :- Top Rated Studios ")
top_studios = df.groupby("studios")["score"].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_studios.plot(kind="bar")
plt.title("5 :- Top Rated Studios ")
plt.xlabel("Studio")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.show()
print()

print("=============================================================================================================================================================================")

print()
print("6 :- Year-wise Anime Releases ")
plt.figure(figsize=(10,5))
df["year"].value_counts().sort_index().plot()
plt.title("6 :- Year-wise Anime Releases ")
plt.xlabel("Year")
plt.ylabel("Number of Anime ")
plt.show()
print()

print("========================================================================================================================================================================================")

print()
print("7 :- Boxplot of Scores ")
plt.figure(figsize=(6,4))
sns.boxplot(x=df["score"])
plt.title("7 :- Boxplot of Anime Scores ")
plt.show()
print()

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print()

print("================ SUMMARY ================")

print("Purpose:")
print("This dataset contains information about anime such as title, genre, studio, ratings, popularity and release year.")

print()

print("Key Observations:")
print("- Dataset contains 30,075 records.")
print("- Dataset contains 29 columns.")
print("- Includes numerical and categorical features.")
print("- Some missing values are present.")

print()

print("Important Insights:")
print("- TV anime are the most common.")
print("- Popular genres appear frequently.")
print("- Higher scored anime generally have better popularity.")

print()

print("Dataset Information:")
print("Rows :", df.shape[0])
print("Columns :", df.shape[1])

print()

print("Input Features:")
print("type, source, episodes, duration, popularity, members, favorites, season, year, studios, genres, themes")

print()

print("Output / Target Variable:")
print("score")

