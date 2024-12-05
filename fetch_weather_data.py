import requests
import pandas as pd
from datetime import datetime

API_KEY = '16fa4093308c5affe336f91f8df31174'
CITY = 'London'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

def fetch_weather_data():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        records = []
        for entry in data['list']:
            records.append({
                "Temperature": entry['main']['temp'],
                "Humidity": entry['main']['humidity'],
                "Wind Speed": entry['wind']['speed'],
                "Weather Condition": entry['weather'][0]['description'],
                "Date": entry['dt_txt']
            })
        df = pd.DataFrame(records)
        df.to_csv('raw_data.csv', index=False)
        print("Weather data saved to raw_data.csv")
    else:
        print("Error fetching data:", response.status_code)

if __name__ == "__main__":
    fetch_weather_data()