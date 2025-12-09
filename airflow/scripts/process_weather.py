import json
import pandas as pd
import os

# Configuration
INPUT_PATH = "/opt/airflow/dags/data/raw_weather.json"
OUTPUT_PATH = "/opt/airflow/dags/data/weather_data.csv"

def process_weather_data():
    print(f"Reading raw data from {INPUT_PATH}...")
    
    if not os.path.exists(INPUT_PATH):
        print(f"❌ File not found: {INPUT_PATH}")
        return

    with open(INPUT_PATH, 'r') as f:
        data = json.load(f)

    # Process daily data
    daily_data = data['daily']
    df = pd.DataFrame(daily_data)
    
    # Rename columns for clarity
    df.rename(columns={
        'time': 'date',
        'temperature_2m_max': 'max_temp_c',
        'temperature_2m_min': 'min_temp_c',
        'shortwave_radiation_sum': 'solar_radiation_mj_m2',
        'wind_speed_10m_max': 'max_wind_speed_kmh'
    }, inplace=True)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    # Save to CSV
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Processed data saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    process_weather_data()
