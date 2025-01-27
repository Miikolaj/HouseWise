"""
Module: clean_data.py

This module handles data cleaning for the HouseWise project,
including feature selection and dataset preparation.
"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# File path to the training dataset
FILE_PATH = '../data/train.csv'
data = pd.read_csv(FILE_PATH)

# Display data overview
data.head()
data.info()

# Define target variable and features
TARGET = 'SalePrice'
X = data.drop(columns=[TARGET])
y = data[TARGET]

# Handle missing values using the most frequent strategy
imputer = SimpleImputer(strategy='most_frequent')
X_imputed = imputer.fit_transform(X)

# Encode categorical variables
X_encoded = pd.DataFrame(X_imputed, columns=X.columns)
for col in X_encoded.select_dtypes(include='object').columns:
    le = LabelEncoder()
    X_encoded[col] = le.fit_transform(X_encoded[col].astype(str))

# Train a Random Forest Regressor
model = RandomForestRegressor(random_state=42)
model.fit(X_encoded, y)

# Identify the top 10 most important features
features_importance = pd.Series(model.feature_importances_, index=X.columns)
top_10_features = features_importance.nlargest(10)
top_10_features = pd.Series(top_10_features)

# Create a cleaned dataset with top features and target variable
cleaned_data = data[top_10_features.index.tolist() + [TARGET]]

# Save the cleaned dataset to a new file
cleaned_data.to_csv("../data/cleaned_dataset.csv", index=False)

print("Dataset cleaned")
