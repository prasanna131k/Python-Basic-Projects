import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

#Q1. Data Loading & Initial Analysis)
#Load the Ford Car Dataset using pandas.
#Display the first 10 rows and last 5 rows.
#Check the shape (number of rows and columns) and data types of all
#columns.
#Write observations about the dataset structure in comments
print("Q1")


df = pd.read_csv(r"c:\Users\PRASANNA\OneDrive\Desktop\ford_car_dataset.csv")

print("First 10 Rows :- ")
print(df.head(10))

print()

print("Last 5 Rows :- ")
print(df.tail(5))

print()

print("Data Shape :- ")
print(df.shape)

print()

print("Data Types :- ")
print(df.dtypes)

print()

print("Dataset Info :- ")
print(df.info())

#---------------------------------------------------------------------------------
### Observations :- 
# 1. The dataset contains rows (records) and columns (features).
# 2. Each row represents one Ford car.
# 3. Numerical columns are stored as int64 and float64.
# 4. The 'model' column is categorical (object data type).
# 5. Shape shows the totale number of rows and columns in the dataset.
#------------------------------------------------------------------------------------------

print("\n")
print("======================================================================================")

print()
#Q2. Missing & Duplicate Values)
#Perform a detailed check on the dataset:
#Find the total number of missing values in each column.
#Identify and remove duplicate rows if any.
#Write a summary of your findings and how you handled them in comments.
print("Q2")

print("Missing Values in Each Column :- ")
print(df.isnull().sum())

print()

print("Totle Missing Values :- ")
print(df.isnull().sum().sum())

print()

print("Duplicate Rows :- ")
print(df.duplicated().sum())

print()

df = df.drop_duplicates()

print("Duplicate Rows After Removal :- ")
print(df.duplicated().sum())

print()

print("Dataset Shape After Removing Duplicates :- ")
print(df.shape)

#-----------------------------------------------------------------------------

# Summary :
# 1. Chacked all columns for missing  (null) values using isnull().sum() .
# 2. Calculated the totale number of missing values in the dataset.
# 3. Checked for duplicate records using duplicated().sum() .
# 4. Removed duplicate rows using drop_duplicated() .
# 5. Verified that no duplicate rows remain in the dataset.

#-------------------------------------------------------------------------------------

print("\n")
print("=============================================================================================")

print()
#Q3. Statistical Summary)
#Generate the statistical summary of all numeric columns using describe().
#Identify minimum, maximum, mean, and median values for key columns like
#price, mileage, and year.
print("Q3")

print("Statistical Summary :- ")
print(df.describe())

print()

print("Price Statistics :- ")
print("Minimum Price :- ", df['price'].min())
print("Maximum Price :- ", df["price"].max())
print("Mean Price    :- ", df["price"].mean())
print("Median Price :- ", df["price"].median())

print()

print("Mileage Statistics :- ")
print("Minimum Mileage :- ", df['mileage'].min())
print("Maximum Mileage :-", df["mileage"].max())
print("Mean Mileage :- ", df["mileage"].mean())
print("Median Mileage :- ", df["mileage"].median())

print()

print("Year Statistics :- ")
print("Minimum Year :- ", df['year'].min())
print("Maximum year :- ", df["year"].max())
print("Mean Year    :- ", df['year'].mean())
print("Median year  :- ", df["year"].median())

#---------------------------------------------------------------------------------
# Observations :- 
# 1. desccribe() provides count, mean, standard deviation, minimum, maximum and quartile values(25%, 50%, 75%) .
# 2. The minimum and maximum values show the data range.
# 3. The mean represents the average value.
# 4. The median (50th percentile) represents the middle value and is less affected by outliners.
# 5. These statistics help understand the overall distribution of price, mileage, and year in the Ford car dataset.
#---------------------------------------------------------------------------------------------

print("\n")
print("=======================================================================================")

print()
#Q4. Histogram of Numeric Features)
#Plot histograms for all important numeric columns (price, mileage, year,
#engineSize, mpg).
#Analyze the distribution for each feature and note your findings in comments.
print("Q4")

columns = ['price', 'mileage', 'year', 'engineSize', 'mpg']

for col in columns :
    plt.figure(figsize=(6,4))
    plt.hist(df[col], bins=20, edgecolor='black')
    plt.title(f"4 :- Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.grid(alpha=0.3)
    plt.show()

#---------------------------------------------------------------------------------------------------
# Findings :- 
# 1. Price :- Shows how car price are distrinuted.
#            Most cars are usually concentrated in a particular price range.
# 2. Mileage :- Indicates the distance travelled by cars.
#               Higher mileage cars may appear less frequwntly.
# 3. Year :- Displays the manufacturing year distribution.
#            More recent models are generally more commen.
# 4. Engine Size :- Most cars typically have small to madium engine size. 
#                   Large engine sizes are comparatively fewer.
# 5. MPG (Miles Per Gskkon) :- Shows fuel efficiency distribution.
#                              Most vrhicles are clustered around the average MPG vslues. 
# 
# Histograms help understand the distribution, spread, skewness, and possible outliers in numerical data.
#-----------------------------------------------------------------------------------------------------------------

print("\n")
print("============================================================================================")

print()
#Q5. Count Plots of Categorical Features)
#Create count plots for all categorical columns (fuelType, transmission, model, etc.)
#using seaborn.
#Analyze which categories are most common.
#Write insights about market trends based on these plots in comments.
print("Q5")

cat_col = df.select_dtypes(include=['object','string']).columns

print("Categorical Columns :- ")
print(cat_col)

for col in cat_col :
    plt.figure(figsize=(10,5))
    sns.countplot(data=df, x=col, order=df[col].value_counts().index)
    plt.title(f"5 :- Count Plot of {col}")
    plt.xlabel(col)
    plt.ylabel("count")
    plt.xticks(rotation=45)
    plt.show()

#-----------------------------------------------------------------------------------------------------------
# Insights :
# 1. Fule type :- The fule type with the highest count is the most popular among Ford cars in the dataset.
# 2. Transmission :- The transmission type with the highest frequency indicates costomer preference(e.g., Manual or automatic).
# 3. Model :- Some Ford models appear much more frequently then others, showing their popularity in the market.
# 4. Other categorical columns :- Catagories with very low counts represent less common vehicle variants.
# 5. Overall Market Trend :- The market is dominated by a few popular models, fule types, and transmission types, while the remaining
#                            categories have comparatively fewer vehicles.
#-----------------------------------------------------------------------------------------------------------------------------

print("\n")
print("============================================================================================================")

print()
#Q6. Correlation Heatmap)
#Create a heatmap of the correlation matrix for numeric features.
#Use seaborn with proper annotations.
#Identify which features are highly correlated with the target variable (price).
#Write your observations in comment.
print("Q6")
numeric_df = df.select_dtypes(include=['int64','float64'])

corr_matrix = numeric_df.corr()

plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("6 :- Correlation Heatmap of Numeric Feature")
plt.show()

print("Correlation with Price :- ")
print(corr_matrix['price'].sort_values(ascending=False))

#--------------------------------------------------------------------------------------------
# Observation :-
# 1. The heatmap shows the correlation between all numerical features.
# 2. Correlation values range from -1 to +1.
#  -  +1  :- Strong positive correlation 
#  -  -1  :- Strong negative correlation
#  -   0  :- No correlation
# 3. features having correlation values close to +1 to -1 with 'price' have a strong relationship with price.
# 4. Features with correlation values close to 0 have little or no impact on price.
# 5. The printed correlation values help identify witch numeric features are most strongly related to the target variable (price).


print("\n")
print("===============================================================================================")

print()
#Q7. Feature Identification)
#Clearly identify and list:
#Independent Features Input Features)
#Dependent Feature Output/Target Feature)
#Justify your choice with reasoning.
print("Q7")

x = df.drop('price', axis=1)

y = df["price"]

print("Indepenadent Features (x) :- ")
print(x.columns .tolist())

print()

print("Independent Features (y) :- ")
print(y.name)

# ---------------------------------------------------------------------------------------
# Justification:
#
# Independent Features (X):
# These are the input variables used to predict the
# price of a Ford car. They include:
# - model
# - year
# - transmission
# - mileage
# - fuelType
# - tax
# - mpg
# - engineSize
#
# Dependent Feature (y):
# - price
#
# Reason:
# The 'price' column is the target/output variable
# because it is the value we want to predict.
# All remaining columns provide information about
# the car and are therefore used as input features
# for prediction.
# ------------------------------------------------------------------------------------------------------------

print("\n")
print("===============================================================================================")

print()
#Q8. Encoding Categorical Variables)
#Convert all categorical columns into numeric form using appropriate encoding
#techniques:
#Use One Hot Encoding.
#Show before and after transformation for at least 2 columns.
print("Q8")
print("Befor One-Hot Encodeing :- ")
print(df[['model', 'transmission']].head())

categorical_col = df.select_dtypes(include=['object', 'string']).columns

df_encoded = pd.get_dummies(df, columns=categorical_col, drop_first=True)

print()
print("After One-Hot Ecoding :- ")
print(df_encoded.head())

print("Shape Before Encoding :- ", df.shape)
print()
print("Shape After Ecoding :- ", df_encoded.shape)

#------------------------------------------------------------------------------------------------------------
# Observations :-
# 1. Befor encodeing, columns like 'model'and 'transmission' contained text value.
# 2. One-Hot Ecoding coverted text these categorical values into numeric (0 and 1) columns.
# 3. 'drop_first = True' removes one dummy column from each category to avoid the dummy variable trap.
# 4. After encoding, the dataset contains only numerical values, making it suitable for Machine Learning algorithms.
#-----------------------------------------------------------------------------------------------------------------------------------

print("\n")
print("==================================================================================================")

print()
#Q9. Feature Scaling)
#Apply Standard Scaling (using StandardScaler from sklearn) on the numeric
#independent features.
#Show the first 5 rows of scaled data.
print("Q9")
x = df_encoded.drop('price', axis=1)

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_scaled = pd.DataFrame(x_scaled, columns=x.columns)

print("First 5 Rows of Scaled Data :- ")
print(x_scaled.head())

#--------------------------------------------------------------------------------------------------------
# Observations :- 
# 1. StandardScaler transforms numerical features so that they have a mean of approximately 0 and a standard deviatoin of 1.
# 2. Feature scaling helps improve the performance of many Machine Learning algorithms.
# 3. The target variable (price) is not scaled because only input features require scaling.
#----------------------------------------------------------------------------------------------------------------------

print("\n")
print("======================================================================================================")

print()
#Q10. Mini Project - Complete Preprocessing Pipeline)
#Create a complete preprocessing pipeline for the Ford Car Dataset:
#Load and clean the data (handle missing & duplicate values).
#Perform EDA (histograms + count plots + heatmap).
#Identify input and output features.
#Encode categorical variables.
#Scale the numeric features.
print("Q10")

print("1 :- Load and Clean Data")
print("Missing Values :- ")
print(df.isnull().sum())

df = df.drop_duplicates()

print()
print("Dataset Shape :- ", df.shape)

print("2:- Exploratory Data Analysis (EDA)")

#Histograms

numeric_cols = ['price', 'mileage', 'year', 'engineSize', 'mpg']

for col in numeric_cols :
    plt.figure(figsize=(6,4))
    plt.hist(df[col], bins=20, edgecolor='black')
    plt.title(f"10 :- Histogram of {col}")
    plt.xticks(rotation=45)
    plt.show()

# count plots

cat_cols = df.select_dtypes(include=['object', 'string']).columns

for col in cat_cols :
    plt.figure(figsize=(10,5))
    sns.countplot(data = df, x = col, order=df[col].value_counts().index)
    plt.title(f"10.2 :- Count Plot of {col}")
    plt.xticks(rotation=45)
    plt.show()

#correlation Heatmap
plt.figure(figsize=(10,8))
corr = df.select_dtypes(include=["int64", "float64"]).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("10.3 :- Correlation Heatmap ")
plt.show()

print("3 :- Identify Input and Output Features")

x = df.drop('price', axis=1)
y = df["price"]

print()
print("Input Features :- ")
print(x.columns.tolist())

print()
print("Target Feature :- ")
print(y.name)


print("4 :- One-Hot Encoding ")

df_encoded = pd.get_dummies(df,columns=cat_cols, drop_first=True)

print()
print("Encoded Dataset Shape :- ")
print(df_encoded.shape)

print("5 :- Feature Scaling")

x = df_encoded.drop('price', axis=1)

scaler = StandardScaler()

x_scaled = scaler.fit_transform(x)

x_scaled = pd.DataFrame(x_scaled, columns = x.columns)

print()
print("First 10 Rows of SCaled Data :- ")
print(x_scaled.head())

#---------------------------------------------------------------------------------------------------
# Mini Project Summary
#
# 1. Loaded the Ford Car dataset. 
# 2. Checked missing values and removed duplicate rows.
# 3. Performed Exploratory Data Analysis using :-
# - Histograms
# - Count Plots
# - Correlation Heatmap
# 4. Identified independent features (x) and depended feature (price).
# 5. Converted categorical variables into numeric using One-Hot Encoding.
# 6. Applied StandardScaler to scale all input features.
# 7. The final dataset is now ready for Machine Learning.

