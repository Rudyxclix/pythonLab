import json

with open("weather.json", "r", encoding="utf-8") as file:
    weather_data = json.load(file)

cities = weather_data["cities"]
print("City        Temperature (°C)   Humidity (%)")
print("-------------------------------------------")

temperature_total = 0
for city_data in cities:
    city = city_data["city"]
    temperature = city_data["temperature"]
    humidity = city_data["humidity"]
    temperature_total = temperature_total + temperature
    print(f"{city:<12}{temperature:<20}{humidity}")

if cities:
    average_temperature = temperature_total / len(cities)
    print("Average temperature:", format(average_temperature, ".1f") + "°C")
    print(
        "Summary: Data for",
        len(cities),
        "cities shows an average temperature of",
        format(average_temperature, ".1f") + "°C.",
    )
else:
    print("No city weather data is available.")
