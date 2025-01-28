import pandas as pd
from tpot import TPOTRegressor
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np

data = pd.read_csv('../data/cleaned_dataset.csv')

X = data.drop(columns=['SalePrice'])
y = data['SalePrice']

categorical_cols = X.select_dtypes(include=['object', 'category', 'string']).columns
numerical_cols = X.select_dtypes(include=[np.number]).columns

numerical_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_pipeline, numerical_cols),
        ('cat', categorical_pipeline, categorical_cols)
    ]
)

tpot_regressor = TPOTRegressor(
    generations=5,
    population_size=50,
    verbosity=2,
    random_state=42,
    n_jobs=-1
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)

preprocessor.fit(X_train)

X_train_prepared = preprocessor.transform(X_train)
X_test_prepared = preprocessor.transform(X_test)

tpot_regressor.fit(X_train_prepared, y_train)

best_pipeline = tpot_regressor.fitted_pipeline_
