import pickle

from fastapi import FastAPI
from pickle import dump, load
from pydantic import BaseModel
from pyexpat import features
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/")
async def root():
    return {"message": "dsadsa"}


@app.post("/predict")
async def prediction(data: Item):
    with open('my_model.pkl', 'rb') as file:
        model = pickle.load(file)

    OverallQual = int(data.OverallQual)
    GarageCars = int(data.OverallQual)
    GrLivArea = int(data.OverallQual)
    FullBath = int(data.OverallQual)
    YearBuilt = int(data.OverallQual)
    FirstFlrSF = int(data.OverallQual)
    Fireplaces = int(data.OverallQual)

    ExterQual = data.ExterQual
    KitchenQual = data.KitchenQual
    BsmtQual = data.BsmtQual

    to_predict = [
        OverallQual,
        GarageCars,
        ExterQual,
        GrLivArea,
        FullBath,
        KitchenQual,
        YearBuilt,
        FirstFlrSF,
        BsmtQual,
        Fireplaces,
    ]

    prediction = model.predict([to_predict])

    return {"price": str(prediction[0])}

