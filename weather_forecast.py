# src/weather_forecast.py
# pip install requests

import requests
from tkinter import Tk, Label

# OpenWeatherMap API key (replace with your actual key)
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

# Function to get weather data
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

# GUI for weather forecast
def weather_forecast_gui():
    root = Tk()
    root.title("Weather Forecast")

    city = "New York"
    weather_data = get_weather(city)

    label = Label(root, text=f"City: {weather_data['name']}\n"
                             f"Temperature: {weather_data['main']['temp']}°C\n"
                             f"Weather: {weather_data['weather'][0]['description']}")
    label.pack()

    root.mainloop()

# Test the weather forecast GUI
if __name__ == "__main__":
    weather_forecast_gui()
