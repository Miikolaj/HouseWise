"""
Module: model_training

This module is responsible for training a Random Forest Regressor pipeline.
It includes preprocessing steps for numerical and categorical data, evaluates the model,
and saves the trained pipeline for deployment.
"""

import os
import pickle
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np

# Load the dataset
data = pd.read_csv('../data/cleaned_dataset.csv')

# Separate features and target
X = data.drop(columns=['SalePrice'])
y = data['SalePrice']

# Identify categorical and numerical columns
categorical_cols = X.select_dtypes(include=['object']).columns
numerical_cols = X.select_dtypes(exclude=['object']).columns

# Define pipelines for preprocessing
numerical_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combine preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_pipeline, numerical_cols),
        ('cat', categorical_pipeline, categorical_cols)
    ]
)

# Create a pipeline with the preprocessor and model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', RandomForestRegressor(random_state=42))
])

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the pipeline on training data
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Save the pipeline to a file
OUTPUT_PATH = '../fastApiProject/models/'
os.makedirs(OUTPUT_PATH, exist_ok=True)
model_file = os.path.join(OUTPUT_PATH, 'model.pkl')

with open(model_file, 'wb') as f:
    pickle.dump(model, f)

print("Number of features expected:", model.n_features_in_)

print("Pipeline saved to:", model_file)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Display evaluation metrics
evaluation_results = {
    "MAE": mae,
    "MSE": mse,
    "RMSE": rmse,
    "R2": r2
}

print(evaluation_results)
