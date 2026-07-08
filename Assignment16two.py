#Q1. Load the insurance dataset using pandas and display the first 10 rows of the data.
print("Q1")

import pandas as pd

df = pd.read_csv(r"c:\Users\PRASANNA\OneDrive\Desktop\insurance.csv")
print(df.head(10))  

print("\n")
#Q2. Use pandas functions to get basic information about the dataset:
# Shape of the data (shape) Column names and data types (info()) 
# Statistical summary of numerical columns (describe())

print("Q2")

print("Shape of the dataset :")
print(df.shape)

print()

print("Column names and data types :")
print(df.info())

print()

print("Statistical summary of numerical columns :")
print(df.describe())

print("\n")
#Q3. Check if the dataset contains any null/missing values. Show the count of null
# values for each column.
print("Q3")

print("Count of null values for each column :")
print(df.isnull().sum())

print("\n")
#Q4. Identify numerical and categorical columns in the dataset. Print them
# separately.

numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

categorical_columns = df.select_dtypes(include=['object', 'string']).columns

print("Numerical Columns:")
print(list(numerical_columns))

print()

print("Categorical Columns:")
print(list(categorical_columns))


print("\n")
#Q5. Create distribution plots for all numerical columns (age, bmi, children, expenses):
# Use sns.histplot() or sns.distplot()
# Create one plot per column (total 4 plots)
# Add meaningful titles and labels

import matplotlib.pyplot as plt
import seaborn as sns

# Distribution plot for 'age'   
plt.figure(figsize=(6, 4))
sns.histplot(df['age'], kde=True)
plt.title('Q5: Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Distribution plot for 'bmi'
plt.figure(figsize=(6, 4))
sns.histplot(df['bmi'], kde=True)
plt.title('Q5: Distribution of BMI')
plt.xlabel('BMI')
plt.ylabel('Frequency')
plt.show()

# Distribution plot for 'children'
plt.figure(figsize=(6, 4))
sns.histplot(df['children'], kde=True)
plt.title('Q5: Distribution of Children')
plt.xlabel('Number of Children')
plt.ylabel('Frequency')
plt.show()

# Distribution plot for 'expenses'
plt.figure(figsize=(6, 4))
sns.histplot(df['expenses'], kde=True)
plt.title('Q5: Distribution of Expenses')
plt.xlabel('Expenses')
plt.ylabel('Frequency')
plt.show()


print("\n")
#Q6. Create count plots for all categorical columns (sex, smoker, region):
# Use sns.countplot() for each column
# Add titles and labels for clarity
print("Q6")

# Count plot for 'sex'
plt.figure(figsize=(6, 4))
sns.countplot(x='sex', data=df)
plt.title('Q6: Count of Sex')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.show()

# Count plot for 'smoker'
plt.figure(figsize=(6, 4))
sns.countplot(x='smoker', data=df)
plt.title('Q6: Count of Smoker')
plt.xlabel('Smoker')
plt.ylabel('Count')
plt.show()

# Count plot for 'region'
plt.figure(figsize=(6, 4))
sns.countplot(x='region', data=df)
plt.title('Q6: Count of Region')
plt.xlabel('Region')
plt.ylabel('Count')
plt.show()


print("\n")
#Q7. Create a heatmap to show the correlation between numerical variables.
# Use sns.heatmap()
# Annotate the values and use a suitable color palette
print("Q7")

correlation = df.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Q7: Correlation Heatmap of Numerical Variables')
plt.show()


print("\n")
#Q8. Perform the following analysis on the expenses column:
# Find the average insurance expenses
#Find the maximum and minimum expenses
# Group by smoker and compare the average expenses for smokers vs non
# smokers
print("Q8")

print("Average insurance expenses :")
print(df['expenses'].mean())

print()

print("Maximum insurance expenses :")
print(df['expenses'].max())

print()

print("Minimum insurance expenses :")
print(df['expenses'].min())

print()

print("Average expenses for smokers vs non-smokers :")
average_charges_by_smoker = df.groupby('smoker')['expenses'].mean()
print(average_charges_by_smoker)


print("\n")
#Q9. Create a boxplot to show the distribution of expenses with respect to smoker
# and sex.
# You can create two separate boxplots or use hue parameter)
print("Q9")

plt.figure(figsize=(6, 4))
sns.boxplot(x='smoker', y='expenses', data=df)
plt.title('Q9: Insurance Expenses Distribution by Smoker Status')
plt.xlabel('Smoker')
plt.ylabel('Expenses')
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(x='sex', y='expenses', data=df)
plt.title('Q9: Insurance Expenses Distribution by Sex')
plt.xlabel('Sex')
plt.ylabel('Expenses')
plt.show()


print("\n")
# Q10. Mini Project / Analysis Summary
print("Q10")

# Calculate required values
avg_age = df["age"].mean()
avg_bmi = df["bmi"].mean()
avg_charges_smoker = df.groupby("smoker")["expenses"].mean()
highest_region = df["region"].value_counts().idxmax()

# ---------------------- Summary ----------------------

# 1. Average age and BMI of customers
print("Average Age:", avg_age)
print("Average BMI:", avg_bmi)

print()
# 2. Smoking effect on insurance expenses
print("Average Expenses by Smoker Status:")
print(avg_charges_smoker)

print()
# 3. Region with the highest number of customers
print("Region with Highest Number of Customers:")
print(highest_region)

# 4. Observations
# - The average age and BMI are shown above.
# - Smokers have significantly higher insurance expenses than non-smokers.
# - The region printed above has the highest number of customers.
# - The distribution plots show that expenses are right-skewed, and the boxplots
#   indicate smokers generally pay much higher expenses than non-smokers.
# - The correlation heatmap shows that age and smoking have a stronger
#   relationship with expenses compared to other numerical variables.

############### sorry for little change in the code, i chnaged an word that word is "charges" to "expenses" in the code, because in the dataset the column name is "expenses" not "charges".
### thats all for the analysis of the insurance dataset.


