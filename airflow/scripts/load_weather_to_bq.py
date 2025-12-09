import pandas as pd
from google.cloud import bigquery
import os

# Configuration
PROJECT_ID = "effidic-stage-2026"
DATASET_ID = "raw_energy"
TABLE_ID = "daily_weather"
CSV_PATH = "/opt/airflow/dags/data/weather_data.csv"

def load_data_to_bigquery():
    print(f"🚀 Starting ingestion from {CSV_PATH} to BigQuery...")

    if not os.path.exists(CSV_PATH):
        print(f"❌ File not found: {CSV_PATH}")
        return

    # 1. Read CSV
    try:
        df = pd.read_csv(CSV_PATH)
        print(f"✅ File read successfully: {len(df)} rows found.")
    except Exception as e:
        print(f"❌ CSV read error: {e}")
        return

    # 2. Connect to BigQuery
    try:
        client = bigquery.Client(project=PROJECT_ID)
        table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

        # Job configuration
        job_config = bigquery.LoadJobConfig(
            write_disposition="WRITE_TRUNCATE", # Overwrite daily for simplicity in this demo
            autodetect=True,
        )

        # 3. Upload data
        print("⏳ Uploading to BigQuery...")
        job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
        job.result()  # Wait for job to complete
        
        print(f"🎉 Success! Data loaded into {table_ref}")
        
        # Verification
        table = client.get_table(table_ref)
        print(f"📊 Table now contains {table.num_rows} rows.")
        
    except Exception as e:
        print(f"❌ BigQuery upload error: {e}")
        raise e

if __name__ == "__main__":
    load_data_to_bigquery()
