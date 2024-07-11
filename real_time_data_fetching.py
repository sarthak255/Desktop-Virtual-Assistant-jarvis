import requests

# Function to fetch real-time weather data
def fetch_weather_data(location):
    api_key = "your_openweathermap_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    return response.json()

# Test the real-time data fetching function
if __name__ == "__main__":
    location = "London"
    weather_data = fetch_weather_data(location)
    print(f"Weather Data: {weather_data}")
