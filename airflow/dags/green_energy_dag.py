from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import sys
import os

# Add scripts directory to path so we can import functions
sys.path.append('/opt/airflow/scripts')

# Import functions from our scripts
try:
    from fetch_weather import fetch_weather_data
    from process_weather import process_weather_data
    from load_weather_to_bq import load_data_to_bigquery
except ImportError as e:
    print(f"Warning: Could not import scripts: {e}")
    def fetch_weather_data(): pass
    def process_weather_data(): pass
    def load_data_to_bigquery(): pass

# Default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
with DAG(
    'green_energy_pipeline',
    default_args=default_args,
    description='Pipeline Green Energy: API -> Raw -> Clean -> BigQuery -> dbt',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['green_energy', 'dbt', 'bigquery'],
) as dag:

    # 1. Ingestion: Fetch raw data from API
    ingest_task = PythonOperator(
        task_id='ingest_weather_data',
        python_callable=fetch_weather_data,
    )

    # 2. Storage/Preparation: Clean and format data
    prepare_task = PythonOperator(
        task_id='prepare_weather_data',
        python_callable=process_weather_data,
    )

    # 3. Loading: Upload to BigQuery
    load_task = PythonOperator(
        task_id='load_to_bigquery',
        python_callable=load_data_to_bigquery,
    )

    # 4. Transformation: dbt run
    # Using the mounted profile at /opt/dbt/profiles.yml
    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='dbt run --project-dir /opt/dbt --profiles-dir /opt/dbt',
        env={'GOOGLE_APPLICATION_CREDENTIALS': '/opt/airflow/keys/service-account.json'}
    )

    # 5. Testing: dbt test
    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='dbt test --project-dir /opt/dbt --profiles-dir /opt/dbt',
        env={'GOOGLE_APPLICATION_CREDENTIALS': '/opt/airflow/keys/service-account.json'}
    )

    # Define dependencies
    ingest_task >> prepare_task >> load_task >> dbt_run >> dbt_test
