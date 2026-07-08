import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Q1. Load the Anime dataset and display the first 10 rows
print("Q1")


df = pd.read_csv(r"c:\Users\PRASANNA\OneDrive\Documents\data_set\anime_dataset.csv")

print(df.head(10))


print("\n")
# Q2. Get basic information about the Anime dataset
print("Q2")

print("Shape of the dataset:")
print(df.shape)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())


print("\n")
# Q3. Check for missing values
print("Q3")

print("Missing Values:")
print(df.isnull().sum())


print("\n")
# Q4. Identify numerical and categorical columns
print("Q4")

numerical_columns = df.select_dtypes(include=["int64","float64"]).columns

categorical_columns = df.select_dtypes(include=["object","string"]).columns

print("Numerical Columns:")
print(list(numerical_columns))

print("\nCategorical Columns:")
print(list(categorical_columns))


print("\n")
# Q5. Distribution plots for numerical columns
print("Q5")

columns = ["score","rank","popularity","members"]

for col in columns:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], kde=True)
    plt.title(f"Q5: Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()


print("\n")
# Q6. Count plots for categorical columns
print("Q6")


columns = ["type","status","season"]

for col in columns:
    plt.figure(figsize=(6,4))
    sns.countplot(x=col, data=df)
    plt.title(f"Q6: Count Plot of {col}")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.xticks(rotation=30)
    plt.show()


print("\n")
# Q7. Correlation Heatmap
print("Q7")

correlation = df.corr(numeric_only=True)

plt.figure(figsize=(10,8))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Q7: Correlation Heatmap")
plt.show()


print("\n")
# Q8. Top 10 Highest Rated Anime
print("Q8")

top_anime = df.sort_values(by="score", ascending=False)

print(top_anime[["title","score"]].head(10))


print("\n")
# Q9. Most Popular Genres
print("Q9")

print(df["genres"].value_counts().head(10))


print("\n")
# Q10. Highest Rated Studios
print("Q10")

studio_rating = df.groupby("studios")["score"].mean().sort_values(ascending=False)

print(studio_rating.head(10))



#### i try to this Optional task make to same for our dealy Assignment type
