# HouseWise Estimator

HouseWise Estimator is a web application that predicts house prices using a machine learning model trained on property data. The model utilizes the `RandomForestRegressor` algorithm to provide reliable estimates of house values, helping users make informed decisions in the real estate market.

## Features

- Predict house prices based on various property features
- User-friendly interface for inputting property details
- Real-time predictions using a FastAPI backend
- Responsive design for different screen sizes

## Technologies Used

- Python
- FastAPI
- Scikit-learn
- Pandas
- Svelte
- TypeScript
- SCSS

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/Miikolaj/HouseWise.git
    ```

## Start the Project

To start the entire project, run the following command in your terminal:

```sh
./start-project.ps1
```



## Usage

1. Open your browser and navigate to `http://localhost:5173`.
2. Input the details of the house you want to estimate the price for.
3. Click the "Predict" button to get the estimated price.

## Input Data Format

The input data should include the following features:

- `OverallQual`: Overall material and finish quality (e.g., "Very Excellent", "Excellent", "Very Good", etc.)
- `GarageCars`: Number of cars that can fit in the garage
- `ExterQual`: Exterior quality (e.g., "Excellent", "Good", "Average/Typical", etc.)
- `GrLivArea`: Above ground living area in square feet
- `FullBath`: Number of full bathrooms
- `KitchenQual`: Kitchen quality (e.g., "Excellent", "Good", "Typical/Average", etc.)
- `YearBuilt`: Year the house was built
- `FirstFlrSF`: First floor square feet
- `BsmtQual`: Basement quality (e.g., "Excellent", "Good", "Typical", etc.)
- `Fireplaces`: Number of fireplaces

## API Endpoints

### `POST /predict`

Predicts the house price based on the input data.

#### Request Body

```json
{
  "OverallQual": "Very Good",
  "GarageCars": "2",
  "ExterQual": "Good",
  "GrLivArea": "1500",
  "FullBath": "2",
  "KitchenQual": "Good",
  "YearBuilt": "2000",
  "FirstFlrSF": "1000",
  "BsmtQual": "Good",
  "Fireplaces": "1"
}