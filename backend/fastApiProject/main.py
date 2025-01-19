import pandas as pd
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
import pickle

app = FastAPI()

# Define allowed origins for CORS
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define the input schema
class Item(BaseModel):
    OverallQual: str
    GarageCars: str
    ExterQual: str
    GrLivArea: str
    FullBath: str
    KitchenQual: str
    YearBuilt: str
    FirstFlrSF: str
    BsmtQual: str
    Fireplaces: str


# Define mappings for categorical features
EXTER_QUAL_MAP = {
    "Excellent": "Ex",
    "Good": "Gd",
    "Average/Typical": "TA",
    "Fair": "Fa",
    "Poor": "Po"
}

OVERALL_QUAL_MAP = {
    "Very Excellent": 10,
    "Excellent": 9,
    "Very Good": 8,
    "Good": 7,
    "Above Average": 6,
    "Average": 5,
    "Below Average": 4,
    "Fair": 3,
    "Poor": 2,
    "Very Poor": 1
}

KITCHEN_QUAL_MAP = {
    "Excellent": "Ex",
    "Good": "Gd",
    "Typical/Average": "TA",
    "Fair": "Fa",
    "Poor": "Po"
}

BASEMENT_QUAL_MAP = {
    "Excellent": "Ex",
    "Good": "Gd",
    "Typical": "TA",
    "Fair": "Fa",
    "Poor": "Po",
    "No Basement": "NA"
}


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}


@app.post("/predict")
async def prediction(data: Item):
    # Load the trained pipeline
    with open('model.pkl', 'rb') as file:
        model_pipeline = pickle.load(file)

    # Convert input data into a DataFrame with the correct column names
    input_data = pd.DataFrame([{
        "OverallQual": OVERALL_QUAL_MAP.get(data.OverallQual),
        "GarageCars": int(data.GarageCars),
        "ExterQual": EXTER_QUAL_MAP.get(data.ExterQual),
        "GrLivArea": int(data.GrLivArea),
        "FullBath": int(data.FullBath),
        "KitchenQual": KITCHEN_QUAL_MAP.get(data.KitchenQual),
        "YearBuilt": int(data.YearBuilt),
        "1stFlrSF": int(data.FirstFlrSF),
        "BsmtQual": BASEMENT_QUAL_MAP.get(data.BsmtQual),
        "Fireplaces": int(data.Fireplaces)
    }])

    # Predict SalePrice
    prediction = model_pipeline.predict(input_data)

    # Return the prediction
    return {"price": str(prediction[0])}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)