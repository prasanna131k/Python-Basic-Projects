# Q1.  Find a dataset that has at least one continuous target variable (e.g., Price,
# Salary, Sales, Temperature, House Price, Car Mileage, etc.).
import warnings
warnings.filterwarnings("ignore")

print("Q1")
print()

print("Answer :-")
print("Dataset Name : Manga Dataset")
print("Target Variable : score")
print("Type of Target Variable : Continuous")
print("Problem Type : Regression")

print("Explanation :- The Manga Dataset Contains information about manga such as title, genres, chapters, volumes, members,\nfavorites, and score. The score column is a continuous numerical variable (for ex :- 7.82, 8.45, 9.13), so it can be\nused as the target variable in a regression model.")


print("\n")

#Q2. Dataset Selection & Initial Exploration)
# Load the dataset and show first 10 rows.
# Write 56 lines explaining why you chose this dataset and what continuous
# value you want to predict.
print("Q2")

import pandas as pd

df = pd.read_csv(r"c:\Users\PRASANNA\OneDrive\Documents\data_set\manga_dataset.csv")

print("First 10 Rows of the Dataset :-")
print(df.head(10))

print()
print("Explaination :-")
print("The Manga Dataset was selected because it contains detailed information about different manga,\nincluding ratings, genres, popularity, and other useful features.\nThis dataset is suitable for regression analysis because it includes a continuous target variable called score.\nThe  goal is to predict the manga score based on various characteristics such as\nchapter, volumes, members, favorites genres, and demographics.")
print("Predicting the score can help understand which factors influence manga ratings. \nThis dataset also provides a good mix of numerical and categorical features, making it suitable for machine learning tasks.")

print("\n")

#Q3. Missing & Duplicate Values Analysis)
# Check for missing values in each column and calculate their percentage.
# Handle missing values appropriately (drop or fill).
# Check and remove duplicate rows if any.
# Write your observations and steps taken.
print("Q3")
print()

print("Missing Values :- ")
missing = df.isnull().sum()
print(missing)
print()

missing_percent = (missing / len(df)) * 100

missing_data = pd.DataFrame({
    "Missing Values" : missing,
    "Percentange" : missing_percent
})

print(missing_data)

numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

categorical_col = df.select_dtypes(include=['object', 'string']).columns

for col in categorical_col :
    df[col] = df[col].fillna(df[col].mode()[0])

duplicates = df.duplicated().sum()
print()
print("Dataset Shape After Cleaning :- ", df.shape)

print("\n")

#Q4. Statistical Summary) 
# Use describe() to generate statistical summary of numeric columns.
# Identify min, max, mean, and median of the target variable.
# Write at least 4 meaningful observations about the data distribution.
print("Q4")

print("Statistical Summary :- ")
print(df.describe())

target = "score"

print()
print("Target Variable Statistics :-")
print("Minimum :- ", df[target].min())
print("Maximum :- ", df[target].max())
print("Mean :- ", df[target].mean())
print("Median :- ", df[target].median())

print()
print("1. The score values range from the minimum to the maximum, showing the overall rating range of manga.")
print("2. The mean and median of the score are close to each other, indicating that the ratings are fairly balanced with limited skewness.")
print("3. The dataset contains a wide range of values for features like members and favorites, indicating differences in manga popularity.")
print("4. Some numerical features have high variation, suggesting that certain manga are significantly more popular or have more chapters than others.")

print("\n")

#Q5. Histogram Analysis of Numeric Features) 
# Plot histograms for all important numeric columns (including the target
# variable).
# Write detailed insights for each plot.
print("Q5")

import matplotlib.pyplot as plt

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_cols :
    plt.figure(figsize=(6,4))
    df[col].hist(bins=20, edgecolor = 'black')
    plt.title(f"Q5 :- Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.grid(False)
    plt.show()

print("Detailed Insights")
print("1. score (Target Variable)")
print("The scores are concentrated between 7 and 9.")
print("Very few manga have extremely low or extremely high scores.")
print("The distribution is close to normal with slight skewness.")
print("This indicates that most manga receive good ratings.")
print()

print("2. members")
print("The distribution is highly right-skewed.")
print("Most manga have a small number of members.")
print("A few very popular manga have extremely high member counts.")
print("These are considered outliers.")
print()

print("3. favorites")
print("Most manga have low favorite counts.")
print("Only a small number of manga are marked as favorites by many users.")
print("The distribution is positively skewed.")
print("Popular manga create a long right tail.")
print()

print("4. scored_by")
print("Most manga are rated by relatively few users.")
print("A few manga receive ratings from a very large audience.")
print("The histogram shows a right-skewed distribution.")
print("This indicates unequal user engagement.")
print()

print("5. chapters")
print("Most manga contain a moderate number of chapters.")
print("Some manga have hundreds of chapters, producing outliers.")
print("The distribution is positively skewed.")
print("Long-running manga are much less common.")
print()

print("6. volumes")
print("Most manga have a small number of volumes.")
print("A few series contain many volumes.")
print("The histogram shows a right-skewed distribution.")
print("This reflects differences between short and long series.")
print()

print("7. popularity")
print("Popularity values are spread across a wide range.")
print("Many manga have lower popularity rankings.")
print("The distribution is not symmetric.")
print("This suggests large variation in popularity among manga.")
print()

print("\n")

#Q6. Count Plots of Categorical Features) 
# Identify categorical columns in your dataset.
# Create count plots for all categorical features using seaborn.
# Analyze the distribution and write business/domain-related insights.
print("Q6")

import seaborn as sns

categorical_cols = df.select_dtypes(include=['object', 'string']).columns

print("Categorical Columns :-")
print(categorical_cols)

for col in categorical_cols :
    plt.figure(figsize=(10,5))

    if df[col].nunique() > 10 :
        sns.countplot(y = df[col], order=df[col].value_counts().head(10).index)
        plt.title(f"Q6 :- Top 10 Categories of {col}")
    else :
        sns.countplot(x=df[col])
        plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

print("Business / Domain-Related Insights")
print("1. Type")
print("Most entries belong to one or two manga types.")
print("This indicates that readers prefer standard manga formats.")
print("Publishers can focus more on these popular types.")
print()

print("2. Status")
print("Most manga are Finished or Publishing.")
print("Ongoing manga help maintain reader engagement.")
print("Completed manga attract readers who prefer binge reading.")
print()

print("3. Genres")
print("Action, Fantasy, Romance, Comedy, and Adventure appear frequently.")
print("These genres have high audience demand.")
print("Publishers can prioritize these genres for future releases.")
print()

print("4. Demographics")
print("Most manga target Shounen and Seinen readers.")
print("This suggests these audience groups dominate the market.")
print("Marketing strategies can focus on these demographics.")
print()


print("5. Authors")
print("Some authors have published many manga, while most have only a few.")
print("Popular authors contribute significantly to reader interest.")
print("Publishers may collaborate more with well-known authors.")
print()

print("6. Serialization (Magazine)")
print("A few magazines publish a large number of manga.")
print("This shows that leading magazines dominate the manga industry.")
print("Publishing in these magazines can increase a manga's visibility.")
print()


print("\n")

#Q7. Correlation Heatmap) 
# Create a correlation heatmap for all numeric features.
# Highlight which features are strongly correlated with the target variable.
# Write your observations regarding feature relationships.
print("Q7")

numeric_df = df.select_dtypes(include=['int64', 'float64'])
corr_matrix = numeric_df.corr()

plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

plt.title("Q7 :- Correlation Heatmap Of Numeric Feature")
plt.show()
target = "score"
print()
print("Correlation with Target Variable (score) :-")
print(corr_matrix[target].sort_values(ascending=False))
print()



print("Observasions :")
print("1. The correlation heatmap shows the relationship between all numerical features in the dataset.")
print("2. Features with correlation values close to +1 have a strong positive relationship with the target variable (score), while values close to -1 indicate a strong negative relationship.")
print("3. Features such as members, favorites, and scored_by are usually positively correlated with score, indicating that highly rated manga tend to have more members, favorites, and user ratings.")
print("4. Features with correlation values close to 0 have little or no linear relationship with the target variable.")
print("5. Highly correlated features can be useful predictors for building an accurate regression model, while weakly correlated features may contribute less to prediction performance.")
print()

print("\n")

#Q8. Feature Identification) Clearly define:
# Independent Features X — input features
# Dependent Feature (y) — continuous target variable you want to predict
# Justify your selection with reasoning.
print("Q8")


X = df.drop(columns=["score", "mal_id", "title", "title_english",
                     "title_japanese", "synopsis", "image_url"],
            errors="ignore")

y = df["score"]

print()
print("Independent Features (X):")
print(X.columns.tolist())

print()
print("Dependent Feature (y):")
print(y.name)

print()
print("Justification:")
print("1. The target variable 'score' is a continuous numerical value.")
print("2. It is suitable for a regression problem.")
print("3. The selected independent features describe different characteristics of a manga.")
print("4. Features like members, favorites, scored_by, genres, and popularity may influence the manga score.")
print("5. Predicting the manga score helps understand which factors contribute to highly rated manga.")

print("\n")

#Q9. Encoding Categorical Variables) Convert all categorical columns to numeric
# form using suitable encoding techniques One-Hot Encoding).
# Show before and after transformation for at least two columns.
# Explain your encoding choices.
print("Q9")

categorical_cols = [
    "type",
    "status",
    "genres",
    "themes",
    "demographics"
]

print("Categorical Columns:")
print(categorical_cols)

print()
print("Before Encoding:")
print(df[["type", "status"]].head())

df_encoded = pd.get_dummies(
    df,
    columns=categorical_cols,
    drop_first=True
)

print()
print("After Encoding:")
encoded_cols = [col for col in df_encoded.columns
                if col.startswith("type_") or col.startswith("status_")]

print(df_encoded[encoded_cols].head())

print()
print("Shape Before Encoding:", df.shape)
print("Shape After Encoding :", df_encoded.shape)
print()
print("Explanation:")
print("1. The dataset contains several categorical columns such as type, status, genres, themes, demographics, authors, and serializations.")
print("2. These columns cannot be used directly in machine learning models because they contain text values.")
print("3. One-Hot Encoding was applied using pd.get_dummies() to convert each category into binary (0/1) columns.")
print("4. The parameter drop_first=True was used to avoid the dummy variable trap and reduce redundant features.")
print("5. Before encoding, columns like 'type' and 'status' contained text values. After encoding, they were converted into numeric columns such as 'type_One-shot', 'type_Doujinshi', 'status_Finished', etc.")
print("6. The encoded dataset is now suitable for training regression models.")

print("\n")

#Q10. Feature Scaling) Apply Standard Scaling on the independent features using
# StandardScaler.
# Show the first 5 rows of the scaled features.
print("Q10")

from sklearn.preprocessing import StandardScaler

X = df_encoded.drop(columns=[
    "score",
    "mal_id",
    "title",
    "title_english",
    "title_japanese",
    "synopsis",
    "image_url",
    "authors",
    "serializations",
    "published_from",
    "published_to"
], errors="ignore")

y = df_encoded["score"]

X = X.fillna(0)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

print("First 5 Rows of Scaled Features:")
print(X_scaled.head())


print()
print("Observation:")
print("1. StandardScaler standardizes all independent features so that they have a mean of 0 and a standard deviation of 1.")
print("2. Feature scaling ensures that variables with larger values do not dominate those with smaller values.")
print("3. Scaling improves the performance of many machine learning algorithms such as Linear Regression, KNN, SVM, and Neural Networks.")
print("4. The first five rows of the scaled features confirm that all independent variables have been transformed into standardized numeric values.")

#=============================================================================================================================================================

print("\nOptional Task : Machine Learning Model")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Features and Target
X = X_scaled          # Use the scaled features created in Q10
y = df["score"]       # Target variable

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("\nModel Evaluation")
print("MAE :", mean_absolute_error(y_test, y_pred))
print("MSE :", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R² Score:", r2_score(y_test, y_pred))

