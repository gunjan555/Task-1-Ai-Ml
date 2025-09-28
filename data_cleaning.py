import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Step 1: Load dataset
df = pd.read_csv("titanic.csv")
print("Initial Shape:", df.shape)
print(df.info())
print(df.isnull().sum())

# Step 2: Handle Missing Values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Step 3: Encode Categorical Variables
df = pd.get_dummies(df, columns=['Sex','Embarked'], drop_first=True)

# Step 4: Standardize Numerical Columns
scaler = StandardScaler()
df[['Age','Fare']] = scaler.fit_transform(df[['Age','Fare']])

# Step 5: Outlier Removal (IQR method on Age)
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1
df = df[~((df['Age'] < (Q1 - 1.5*IQR)) | (df['Age'] > (Q3 + 1.5*IQR)))]

print("Final Shape after Cleaning:", df.shape)

# Save cleaned data
df.to_csv("titanic_cleaned.csv", index=False)
print("✅ Cleaned dataset saved as titanic_cleaned.csv")