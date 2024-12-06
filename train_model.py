from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

def fetch_weather():
    subprocess.run(["python", "fetch_weather_data.py"])

def preprocess_weather():
    subprocess.run(["python", "preprocess_data.py"])

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'weather_pipeline',
    default_args=default_args,
    description='A simple weather data pipeline',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    fetch_task = PythonOperator(
        task_id='fetch_weather_data',
        python_callable=fetch_weather
    )

    preprocess_task = PythonOperator(
        task_id='preprocess_data',
        python_callable=preprocess_weather
    )

    fetch_task >> preprocess_task