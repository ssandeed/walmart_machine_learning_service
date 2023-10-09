FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./app /app

COPY ./data/processed/unique_item_list.csv /data/processed/unique_item_list.csv

COPY ./models/predictive/lgbm_store_CA_1.joblib /models/predictive/lgbm_store_CA_1.joblib
COPY ./models/predictive/lgbm_store_CA_2.joblib /models/predictive/lgbm_store_CA_2.joblib
COPY ./models/predictive/lgbm_store_CA_3.joblib /models/predictive/lgbm_store_CA_3.joblib
COPY ./models/predictive/lgbm_store_CA_4.joblib /models/predictive/lgbm_store_CA_4.joblib
COPY ./models/predictive/lgbm_store_TX_1.joblib /models/predictive/lgbm_store_TX_1.joblib
COPY ./models/predictive/lgbm_store_TX_2.joblib /models/predictive/lgbm_store_TX_2.joblib
COPY ./models/predictive/lgbm_store_TX_3.joblib /models/predictive/lgbm_store_TX_3.joblib
COPY ./models/predictive/lgbm_store_WI_1.joblib /models/predictive/lgbm_store_WI_1.joblib
COPY ./models/predictive/lgbm_store_WI_2.joblib /models/predictive/lgbm_store_WI_2.joblib
COPY ./models/predictive/lgbm_store_WI_3.joblib /models/predictive/lgbm_store_WI_3.joblib

COPY ./models/forecasting/arima_model.joblib /models/forecasting/arima_model.joblib

COPY Procfile Procfile

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "/gunicorn_conf.py", "main:app"]