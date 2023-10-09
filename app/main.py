# Import necessary libraries
from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse
from datetime import datetime
import joblib
from joblib import load
import pandas as pd

# Create a FastAPI application instance
app = FastAPI()

# Define a list of store names
store_names = ['store_CA_1', 'store_CA_2', 'store_CA_3', 'store_CA_4', 'store_TX_1',
               'store_TX_2', 'store_TX_3', 'store_WI_1', 'store_WI_2', 'store_WI_3']

# Define a list of store IDS
store_ids = ['CA_1', 'CA_2', 'CA_3', 'CA_4', 'TX_1', 'TX_2', 'TX_3', 'WI_1', 'WI_2', 'WI_3']


# Read a list of unique item IDs from a CSV file
list_of_unique_item_ids = pd.read_csv('../data/processed/unique_item_list.csv')['item_id'].tolist()

# Checking leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Checking if date is valid
def validate_date(date_str):
    try:
        # Try to parse the date using the specified format
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        
        # Check if the date is within the desired range
        start_date = datetime(2011, 1, 1)
        end_date = datetime(2015, 12, 31)
        
        # Extract year, month, and day from the date
        year, month, day = date_obj.year, date_obj.month, date_obj.day

        # Check if the year, month, and day are within valid ranges
        if (
            start_date <= date_obj <= end_date
            and 1 <= month <= 12
            and 1 <= day <= 31
        ):
            # Check for February and handle leap year
            if month == 2:
                if is_leap_year(year):
                    return 1 <= day <= 29
                else:
                    return 1 <= day <= 28
            else:
                # Check for months with fewer than 31 days
                if month in [4, 6, 9, 11]:
                    return 1 <= day <= 30
                else:
                    return 1 <= day <= 31
        else:
            return False
    except ValueError:
        # If parsing the date raises a ValueError, it's an invalid date
        return False

    
# Create a dictionary to store the models
lgbm_models = {}


for name in store_names:
    # Load the model using joblib
    import_model = load(f'../models/predictive/lgbm_{name}.joblib')
    
    # Store the model in the dictionary with the store name as the key
    lgbm_models[name] = import_model

# Load the ARIMA model using joblib
arima_model = load(f'../models/forecasting/arima_model.joblib')
    
    
def format_features(
    item_id: str,
    store_id: str,
    date: str
):
    # Convert the date to a datetime object
    date_datetime = pd.to_datetime(date)

    # Extract year, month, day, and day of the week
    year = date_datetime.year
    month = date_datetime.month
    day = date_datetime.day
    day_of_week = date_datetime.strftime('%A')

    return {
        'item_id': [item_id],
        'store_id': [store_id],
        'year': [year],
        'month': [month],
        'day': [day],
        'day_of_week': [day_of_week]
    }


# Next 7 days prediction function:
def predict_7_days(start_date, arima_model):
    # Convert the input date string to a datetime object
    start_date = pd.to_datetime(start_date)

    # Create a date range for the next 7 days
    future_date_index = pd.date_range(start=start_date, periods=7)

    # Make predictions for the next 7 days
    pred = arima_model.predict(start=len(arima_model.fittedvalues), end=len(arima_model.fittedvalues) + 6, typ='levels').rename('ARIMA Predictions')

    # Create a dictionary of predictions in the desired format
    predictions_dict = {date.strftime('%d/%m/%Y'): value for date, value in zip(future_date_index, pred)}

    return predictions_dict


@app.get("/")
def read_root():
    return {"Project": "AT2 - Machine Learning as a Service",
            "Author": "Sareem Sandeed",
            "Task-1": "Predictive model using a Machine Learning algorithm to accurately predict the sales revenue for a given item in a specific store at a given date",
            "Task-2": "Forecasting model using a time-series analysis algorithm that will forecast the total sales revenue across all stores and items for the next 7 days",
            "EndPoint-1: / :": "Brief description of the project",
            "EndPoint-2: /health/ : ": "Returning status code 200 with a string with a welcome message",
            "EndPoint-3: /sales/national/ :": "Returning next 7 days sales volume forecast for an input date",
            "EndPoint-4: /sales/stores/items/ :": "Returning predicted sales revenue for an input item, store and date",
            "Input Date Format": "YYYY-MM-DD",
            "Input Item Format": "Full item id: All in Capital Letters-Case Sensitive(For example: FOODS_3_310)",
            "Input Store Format": "Full store id: All in Capital Letters-Case Sensitive(For example: CA_3)",
            "Output Prediction Format": " JSON: {'prediction':'5.66'} ",
            "Output Forecast Format": "JSON: {'2014-11-21':'1000', '2014-11-22':'1000'....}",
            "GitHub Repo": "https://github.com/ssandeed/adv_mla_at2"}


@app.get('/health/', status_code=200)
def healthcheck():
    return 'Prediction and Forecasting are all ready to go!'


# endpoint-2: sales/national
@app.get("/sales/national/")
def get_sales_forecast(start_date: str):
    # Check if the date is in the correct format
    if not validate_date(start_date):
        raise HTTPException(status_code=400, detail="Invalid Date!!! Date format should be 'YYYY-MM-DD', valid and within the range.")
    predictions = predict_7_days(start_date, arima_model)
    return JSONResponse(predictions)


# endpoint-3: /sales/stores/items
@app.get("/sales/stores/items/")
def predict(item_id: str, store_id: str, date: str):
    # Check if the item_id is in the list of unique item IDs
    if item_id not in list_of_unique_item_ids:
        raise HTTPException(status_code=400, detail="Invalid Item!!! Please give correct item id.")
        
    # Check if the store_id is in the list of valid store_ids
    if store_id not in store_ids:
        raise HTTPException(status_code=400, detail="Invalid Store!!! Please give correct store id.")
    
    # Check if the date is in the correct format
    if not validate_date(date):
        raise HTTPException(status_code=400, detail="Invalid Date!!! Date format should be 'YYYY-MM-DD', valid and within the range.")
        
    # If the item_id, store_id and date are valid, proceed with the rest of the code
    features = format_features(item_id, store_id, date)
    model = lgbm_models[f'store_{store_id}']
    obs = pd.DataFrame(features)
    pred = model.predict(obs)
    
    # Format the prediction result as a dictionary
    prediction_result = {'prediction': pred.tolist()}
    return JSONResponse(prediction_result)