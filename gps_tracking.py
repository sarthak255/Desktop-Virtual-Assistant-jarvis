# src/gps_tracking.py
# pip install geopy folium googlemaps

import geopy
from geopy.geocoders import Nominatim
import folium
import googlemaps

# Google Maps API key (replace with your actual key)
gmaps = googlemaps.Client(key="YOUR_GOOGLE_MAPS_API_KEY")

# Function to get current location
def get_current_location():
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode("Your address")
    return (location.latitude, location.longitude)

# Function to create a map
def create_map(latitude, longitude):
    my_map = folium.Map(location=[latitude, longitude], zoom_start=15)
    folium.Marker([latitude, longitude], popup="Current Location").add_to(my_map)
    my_map.save("current_location_map.html")

# Function to get directions
def get_directions(origin, destination):
    directions = gmaps.directions(origin, destination, mode="driving")
    return directions

# Test the functions
if __name__ == "__main__":
    current_location = get_current_location()
    print(f"Current location: {current_location}")
    create_map(current_location[0], current_location[1])
    origin = "New York, NY"
    destination = "Los Angeles, CA"
    directions = get_directions(origin, destination)
    print(directions)
