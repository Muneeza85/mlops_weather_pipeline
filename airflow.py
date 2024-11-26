from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def collect_data():
    # Call the data collection script here
    exec(open("collect_data.py").read())

def preprocess_data():
    # Call the preprocessing script here
    exec(open("preprocess_data.py").read())

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "weather_pipeline",
    default_args=default_args,
    description="A simple weather data pipeline",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:
    task1 = PythonOperator(task_id="collect_data", python_callable=collect_data)
    task2 = PythonOperator(task_id="preprocess_data", python_callable=preprocess_data)

    task1 >> task2
