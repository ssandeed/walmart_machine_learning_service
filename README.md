adv_mla_at2
==============================

# Advance Machine Learning Algorithms Assignment-2: Machine Learning as a Service


## Part A:
A predictive model using a Machine Learning algorithm to accurately predict the sales revenue for a given item in a specific store at a given date.
Model - LightGBM

## Part B
A forecasting model using a time-series analysis algorithm that will forecast the total sales revenue across all stores and items for the next 7 days.
Model - ARIMA

## Project Overview

This project aimed to develop two critical models for sales forecasting and revenue optimization in the retail industry. The objectives were to create a Predictive Sales Revenue Model and a Sales Revenue Forecasting Model using machine learning and time-series analysis techniques, respectively. These models play a pivotal role in enhancing decision-making processes at both the tactical and strategic levels within the retail sector.

## Objective

The main objective of this project is to develop a predictive and forecasting model and deploy on Heroku.

## Methodology

- Data Collection: We have the test and train data already provided for this part of assessment.

- Data Preprocessing: The collected data was preprocessed, including handling missing values and feature engineering to extract relevant information.

- Feature Engineering: On date, feature engineering was done on it.

- Model Development: We trained a LightGBM Regression model to predict predict the sales revenue for a given item in a specific store at a given date. ARIMA was used for forecasting the total sales revenue across all stores and items for the next 7 days.

- Evaluation: The model's performance was assessed using RSME score, which is suitable for regression problems.

## Deployment

- App was deployed using FASTAPI, GitHub, Docker and Heroku.

- Here are the list of expected accessible FAST API endpoints:

‘/’ (GET): Displaying a brief description of the project objectives, list of endpoints, expected input parameters and output format of the model.
‘/health/’ (GET): Returning status code 200 with a string with a welcome message.
‘/sales/national/’ (GET): Returning next 7 days sales volume forecast for an input date.
‘/sales/stores/items/’ (GET): Returning predicted sales volume for an input item, store and date.

- Model is deployed on Heroku: https://murmuring-savannah-38202-293cb3467416.herokuapp.com/docs



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── app                <- FAST API script
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
