# Walmart Sales: Machine Learning as a Service

This project is to develop a Machine Learning Solution for an American retailer-Walmart, that has 10 stores across 3 different states: California (CA), Texas (TX) and Wisconsin (WI). Each shop sells items from 3 different categories: hobbies, foods and household. The datasets used are from the [M5 Kaggle Competition.](https://www.kaggle.com/competitions/m5-forecasting-accuracy)

![image](https://github.com/ssandeed/walmart_machine_learning_service/assets/46265728/14e0e080-5754-455f-884b-6f157d2a835d)

## Part A:
A predictive model using a Machine Learning algorithm to accurately predict the sales revenue for a given item in a specific store at a given date.
Model - LightGBM

## Part B
A forecasting model using a time-series analysis algorithm that will forecast the total sales revenue across all stores and items for the next 7 days.
Model - ARIMA

## Project Overview

This project aimed to develop two critical models for sales forecasting and revenue optimization in the retail industry. The objectives were to create a Predictive Sales Revenue Model and a Sales Revenue Forecasting Model using machine learning and time-series analysis techniques. These models are pivotal in enhancing decision-making processes at the retail sector's tactical and strategic levels.

## Objective

The main objective of this project is to develop a predictive and forecasting model and deploy it on Heroku.

## Methodology

- Data Collection: The test and train data are already available from the M5 Kaggle Competition.

- Data Preprocessing: The collected data was preprocessed, including handling missing values and feature engineering to extract relevant information.

- Feature Engineering: On date, feature engineering was done on it.

- Model Development: Trained a LightGBM Regression model to predict the sales revenue for a given item in a specific store at a given date. ARIMA was used for forecasting the total sales revenue across all stores and items for the next 7 days.

- Evaluation: The model's performance was assessed using the RSME score, suitable for regression problems.

## Deployment

- The app was deployed using FASTAPI, GitHub, Docker and Heroku.

- Here is the list of expected accessible FAST API endpoints:

**‘/’ (GET):** Displaying a brief description of the project objectives, list of endpoints, expected input parameters and model output format.

**‘/health/’ (GET):** Returning status code 200 with a string with a welcome message.

**‘/sales/national/’ (GET):** Returning next 7 days' sales volume forecast for an input date.

**‘/sales/stores/items/’ (GET):** Returning predicted sales volume for an input item, store and date.

- The model is deployed on Heroku and can be accessed on https://murmuring-savannah-38202-293cb3467416.herokuapp.com/docs



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train.`
    ├── README.md          <- The top-level README for developers using this project.
    ├── app                <- FAST API script
    ├── data
    │   ├── external       <- Data from third-party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final canonical data sets for modelling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. The naming convention is a number (for ordering),
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
    │   ├── features       <- Scripts to turn raw data into features for modelling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results-oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
