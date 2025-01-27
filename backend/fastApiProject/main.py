"""
Main application file for the HouseWise backend.

This module defines the FastAPI application,
handles API endpoints, and integrates the trained model.
"""

import pickle
import pandas as pd
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from schemas.schema import Item
from mappings.mapping import (
    EXTER_QUAL_MAP,
    OVERALL_QUAL_MAP,
    KITCHEN_QUAL_MAP,
    BASEMENT_QUAL_MAP)

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

@app.post("/predict")
async def prediction(data: Item):
    """
    Predict the house price based on input data.

    Parameters:
        data (Item): Input data conforming to the Item schema.

    Returns:
        dict: Predicted house price or error message.
    """
    # Load the trained pipeline
    try:
        with open("models/model.pkl", "rb") as file:
            model_pipeline = pickle.load(file)
    except FileNotFoundError:
        return {"error": "Model file not found. Ensure 'model.pkl' is available."}
    except pickle.UnpicklingError:
        return {"error": "Failed to load the model. Check the file format."}

    # Convert input data into a DataFrame with the correct column names
    try:
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
    except ValueError as e:
        return {"error": f"Invalid input data: {e}"}

    # Predict SalePrice
    try:
        result = model_pipeline.predict(input_data)
        return {"price": str(result[0])}
    except Exception as e:
        return {"error": f"Prediction failed: {e}"}
