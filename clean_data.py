from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
import pandas as pd

file_path = 'data/train.csv'
data = pd.read_csv(file_path)

data.head(), data.info()

target = 'SalePrice'
X = data.drop(columns=[target])
y = data[target]

imputer = SimpleImputer(strategy='most_frequent')
X_imputed = imputer.fit_transform(X)

X_encoded = pd.DataFrame(X_imputed, columns=X.columns)
for col in X_encoded.select_dtypes(include='object').columns:
    le = LabelEncoder()
    X_encoded[col] = le.fit_transform(X_encoded[col].astype(str))

model = RandomForestRegressor(random_state=42)
model.fit(X_encoded, y)

importances = pd.Series(model.feature_importances_, index=X.columns)
top_10_features = importances.nlargest(10).index

cleaned_data = data[top_10_features.tolist() + [target]]

cleaned_data.to_csv("cleaned_dataset.csv", index=False)

print("Dataset cleaned")
