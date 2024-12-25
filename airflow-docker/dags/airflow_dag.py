import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import pandas as pd

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': dt.datetime(2024, 12, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Create the DAG
with DAG(
    'example_dag',
    default_args=default_args,
    description='An example DAG',
    schedule='@daily',  # Replacing schedule_interval with schedule
) as dag:

    # Define tasks
    bash_task = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    def greet():
        print("Hello, Airflow!")

    python_task = PythonOperator(
        task_id='say_hello',
        python_callable=greet,
    )

    # Task dependencies
    bash_task >> python_task

