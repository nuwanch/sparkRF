# import pandas as pd
# from math import radians, sin, cos, sqrt, atan2

# def calculate_distance(lat1, lon1, lat2, lon2):
#     # Convert latitude and longitude from degrees to radians
#     lat1_rad = radians(lat1)
#     lon1_rad = radians(lon1)
#     lat2_rad = radians(lat2)
#     lon2_rad = radians(lon2)

#     # Radius of the Earth in kilometers
#     earth_radius = 6371.0

#     # Differences in coordinates
#     dlon = lon2_rad - lon1_rad
#     dlat = lat2_rad - lat1_rad

#     # Haversine formula to calculate distance
#     a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1 - a))
#     distance = earth_radius * c

#     return distance  # Distance in kilometers

# # Example usage
# latitude1 = 40.7128  # Latitude of location 1 (e.g., New York City)
# longitude1 = -74.0060  # Longitude of location 1
# latitude2 = 34.0522  # Latitude of location 2 (e.g., Los Angeles)
# longitude2 = -118.2437  # Longitude of location 2

# result = calculate_distance(latitude1, longitude1, latitude2, longitude2)
# print(f"The distance between the locations is approximately {result:.2f} kilometers.")

from geopy.distance import geodesic
newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(geodesic(newport_ri, cleveland_oh).kilometers)

