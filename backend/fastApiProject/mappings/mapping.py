"""
Mappings module for categorical feature conversion.

This file contains mappings for categorical
values used in the prediction pipeline.
"""

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
