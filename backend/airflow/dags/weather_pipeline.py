from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

# Define functions to execute your scripts
def fetch_weather():
    subprocess.run(["python", "fetch_weather_data.py"], check=True)

def preprocess_weather():
    subprocess.run(["python", "preprocess_data.py"], check=True)

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
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

    # Define task dependencies
    fetch_task.set_downstream(preprocess_task)

