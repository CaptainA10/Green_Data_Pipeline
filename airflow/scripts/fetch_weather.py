import requests
import pandas as pd
import os
from datetime import datetime

# Configuration
LATITUDE = 48.8566  # Paris
LONGITUDE = 2.3522
START_DATE = "2023-01-01"
END_DATE = datetime.today().strftime('%Y-%m-%d')
OUTPUT_PATH = "/opt/airflow/dags/data/raw_weather.json"

def fetch_weather_data():
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "start_date": START_DATE,
        "end_date": END_DATE,
        "daily": ["temperature_2m_max", "temperature_2m_min", "shortwave_radiation_sum", "wind_speed_10m_max"],
        "timezone": "Europe/Paris"
    }

    print(f"Fetching data from {url}...")
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    # Ensure output directory exists
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    # Save to JSON
    import json
    with open(OUTPUT_PATH, 'w') as f:
        json.dump(data, f)
    print(f"Raw data saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    fetch_weather_data()
