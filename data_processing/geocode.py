import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import time

# Replace 'your_csv_file.csv' with your CSV file path
csv_file = 'geocoded_testimonies-en.csv'

# Load CSV file
df = pd.read_csv(csv_file, sep=",")

# Initialize Nominatim Geocoder
geolocator = Nominatim(user_agent="geoapiExercises")

# Define a rate limiter to avoid overloading the API service
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Function to get latitude and longitude
def get_geolocation(place):
    try:
        location = geocode(place)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except:
        return None, None

# Assuming the column with place names is named 'Place_Name'
# Replace 'Place_Name' with the actual column name
df['residence_Latitude'], df['residence_Longitude'] = zip(*df['Place_of_residence'].apply(get_geolocation))

# Save the DataFrame with geocoded data to a new CSV file
# Replace 'output_csv_file.csv' with your desired output file name
df.to_csv('new_geocoded_testimonies-en.csv', index=False)