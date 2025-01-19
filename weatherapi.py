import requests
import json

# API URL
url = "https://archive-api.open-meteo.com/v1/archive?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure"

# Fetch data
response = requests.get(url)
weather_data = response.json()

# Save JSON data
with open("data/json/weather_data.json", "w") as file:
    json.dump(weather_data, file, indent=4)  # Pretty-printing for readability


import json
import pandas as pd

# Load JSON data
with open('data/json/weather_data.json', 'r') as file:
    data = json.load(file)

# Extract the relevant data from 'hourly'
hourly_data = data['hourly']
time = hourly_data['time']
temperature_2m = hourly_data['temperature_2m']
relative_humidity_2m = hourly_data['relative_humidity_2m']
precipitation = hourly_data['precipitation']
surface_pressure = hourly_data['surface_pressure']

# Create a list of dictionaries containing only the data of interest
filtered_data = []
for i in range(len(time)):
    filtered_data.append({
        "time": time[i],
        "temperature_2m": temperature_2m[i],
        "relative_humidity_2m": relative_humidity_2m[i],
        "precipitation": precipitation[i],
        "surface_pressure": surface_pressure[i]
    })

# Convert to a DataFrame
df = pd.DataFrame(filtered_data)

# Save the DataFrame to CSV
df.to_csv('data/CSV/weather_data.csv', index=False)
