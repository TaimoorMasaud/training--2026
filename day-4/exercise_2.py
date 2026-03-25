import requests
import sys

def get_weather(city):
    # Step 1: Geocoding
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_data = requests.get(geo_url).json()

    if "results" not in geo_data:
        print("City not found")
        return

    location = geo_data["results"][0]
    lat = location["latitude"]
    lon = location["longitude"]
    city_name = location["name"]

    # Step 2: Weather
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather_data = requests.get(weather_url).json()

    current = weather_data["current_weather"]

    temp_c = current["temperature"]
    temp_f = (temp_c * 9/5) + 32
    wind = current["windspeed"]
    code = current["weathercode"]

    # Weather code mapping
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast"
    }

    description = weather_codes.get(code, "Unknown")

    print(f"City: {city_name}")
    print(f"Temperature: {temp_c}°C / {temp_f:.1f}°F")
    print(f"Wind Speed: {wind} km/h")
    print(f"Weather: {description}")



if __name__ == "__main__":
    # take city name from command line
    if len(sys.argv) > 1:
        city_name = sys.argv[1]
    else:
        city_name = input("Enter City name: ")

    get_weather(city_name)