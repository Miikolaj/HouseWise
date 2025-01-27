"""
Schemas module for input data validation.

This file contains schema definitions for input data
used in the prediction pipeline.
"""

from pydantic import BaseModel

class Item(BaseModel):
    """
    Schema for input data sent to the prediction endpoint.

    Attributes:
        OverallQual (str): Overall quality rating.
        GarageCars (str): Number of cars in the garage.
        ExterQual (str): Exterior quality rating.
        GrLivArea (str): Above ground living area size.
        FullBath (str): Number of full bathrooms.
        KitchenQual (str): Kitchen quality rating.
        YearBuilt (str): Year the house was built.
        FirstFlrSF (str): Size of the first floor.
        BsmtQual (str): Basement quality rating.
        Fireplaces (str): Number of fireplaces.
    """
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
