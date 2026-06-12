import random

MODE = "NORMAL"

# NORMAL
# GEOFENCE
# THEFT


def get_location():

    if MODE == "NORMAL":

        lat = 12.9716 + random.uniform(-0.003, 0.003)
        lon = 77.5946 + random.uniform(-0.003, 0.003)

    elif MODE == "GEOFENCE":

        lat = 13.5000
        lon = 78.0000

    elif MODE == "THEFT":

        lat = 13.7000
        lon = 78.3000

    return lat, lon