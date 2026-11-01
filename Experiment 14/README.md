# Experiment 14: Weather Information Using JSON

## Aim
To read weather data for multiple cities from a JSON file and summarize the temperatures.

## Algorithm
1. Open `weather.json` and parse it with Python's `json` module.
2. Display each city's name, temperature, and humidity.
3. Calculate and display the average temperature and a short summary.

## Sample output
```text
City        Temperature (°C)   Humidity (%)
-------------------------------------------
Bengaluru   28                  70
Kochi       30                  80
Delhi       35                  45
Average temperature: 31.0°C
Summary: Data for 3 cities shows an average temperature of 31.0°C.
```

## Explanation
The program reads the sample dataset from the relative path `weather.json`, so no API key or internet connection is needed.
