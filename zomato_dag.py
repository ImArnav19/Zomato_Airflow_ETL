from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from zomato_etl import zomato_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 11, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'zomato.dag',
    default_args=default_args,
    description='First ETL',
    schedule_interval=timedelta(days=1),

)

run_etl = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=zomato_etl,
    dag=dag,
)

run_etl

