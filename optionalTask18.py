import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(r"c:\Users\PRASANNA\OneDrive\Desktop\anime123.csv")

print("Q1")
print("Data Loading and Initial Analysis")
print()

print("First 10 rows :- ")
print(df.head(10))

print()
print("Last 5 Rows :- ")
print(df.tail())

print()
print("Shape :- ")
print(df.shape)

print()
print("Data Types :- ")
print(df.dtypes)

print()
print("Info :- ")
print(df.info())

#---------------------------------------------------------------
# Observation :- 
# Dataset contains Anime information with numerical and categorical features.
#-------------------------------------------------------------------------------

print("\n")
print("===============================================================================")

print()
print("Q2")
print("Missing & Duplicate Values")

print("Missing Values :- ")
print(df.isnull().sum())

print()
print("Duplicate Rows :- ")
print(df.duplicated().sum())

print()
df = df.drop_duplicates()

print("Shape After Removing Duplicates :- ")
print(df.shape)

#---------------------------------------------------------------------
# Observation :-
# Removed Duplicate rows and Chacked missing values.
#------------------------------------------------------------------------------

print("\n")
print("=================================================================================")

print()
print("Q3")
print("Statistical Summary :- ")

print(df.describe())

print()
print("Minimum Score :- ", df["score"].min())
print("Maximum Score :- ", df["score"].max())
print("Mean Score :- ", df["score"].mean())
print("Median Score :- ", df["score"].median())

print()
print("Minimum Members :- ", df["members"].min())
print("Maximum Members :- ", df["members"].max())
print("Mean Members :- ", df["members"].mean())
print("Median Members :- ", df["members"].median())

print()
print("Minimum Favorites :- ", df["favorites"].min())
print("Maximum Favorites :- ", df["favorites"].max())
print("Mean Favorites :- ", df["favorites"].mean())
print("Median Favorites :- ", df["favorites"].median())

print("\n")
print("==================================================================================")

print()
print("Q4")
print("Histograms")

cols = ['score', 'members', 'favorites', 'episodes']

for col in cols :
    plt.figure(figsize=(6,4))
    plt.hist(df[col].dropna(), bins=20, edgecolor='black')
    plt.title(col)
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()

print("\n")
print("==================================================================================")

print()
print("Q5")
print("Count Plots")

cat_cols = ['type', 'status', 'rating', 'source']

for col in cat_cols :
    plt.figure(figsize=(10,5))
    sns.countplot(data=df, x=col, order=df[col].value_counts().index)
    plt.title("Q5 :- Count Ploats")
    plt.xticks(rotation=45)
    plt.show()

print("\n")
print("================================================================================")

print()
print("Q6")
print("Correlation Heatmap")

numeric_df = df.select_dtypes(include=['int64', 'float64'])
corr = numeric_df.corr()

plt.figure(figsize=(12,8))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Q6 :- Heatmap ")
plt.show()

print(corr['score'].sort_values(ascending=False))

print("\n")
print("==================================================================================")

print()
print("Q7")
print("Feature Identification")

x = df.drop("score", axis=1)

y = df["score"]

print("Input Features")
print(x.columns.tolist())

print()
print("Target Feature")
print(y.name)

print("\n")
print("==================================================================================")
print()

print("Q8")
print("One-Hot Encoding")

categorical = ['type', 'status', 'rating', 'source']

df_encoded = pd.get_dummies(df, columns=categorical, drop_first=True)

print(df_encoded.head())

print("\n")
print("===================================================================================")
print()

print("Q9")
print("Standard Scaling")

x = df_encoded.drop('score', axis=1)

x = x.select_dtypes(include=['int64', 'float64', 'bool'])

x = x.fillna(x.mean())

scaler = StandardScaler()

x_scaled = scaler.fit_transform(x)

x_scaled = pd.DataFrame(x_scaled, columns=x.columns)

print(x_scaled.head())

print("\n")
print("===================================================================================")
print()

print("Q10")
print("Mini Project Summary")
print()

print("1. Loaded the Anime dataset successfully.")
print("2. Checked missing values and duplicate records.")
print("3. Performed Exploratory Data Analysis (EDA) using:")
print("   - Histograms")
print("   - Count Plots")
print("   - Correlation Heatmap")
print("4. Identified Independent (Input) and Dependent (Target) features.")
print("5. Applied One-Hot Encoding on categorical columns.")
print("6. Applied Standard Scaling on numeric input features.")
print("7. The dataset is now preprocessed and ready for Machine Learning models.")

# -------------------------------------------------------------------------
# Summary:
# 1. The dataset was loaded and explored successfully.
# 2. Missing values and duplicate records were analyzed.
# 3. Histograms, Count Plots, and Correlation Heatmap were used for EDA.
# 4. 'score' was selected as the target variable.
# 5. Categorical variables were converted into numeric form using One-Hot Encoding.
# 6. Numeric input features were standardized using StandardScaler.
# 7. The final dataset is suitable for further Machine Learning tasks such as
#    classification, regression, or recommendation systems.
# ---------------------------------------------------------------------------------------


