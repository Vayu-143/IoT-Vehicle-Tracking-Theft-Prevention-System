import math

SAFE_LAT = 12.9716
SAFE_LON = 77.5946
RADIUS = 1.0  # km


def distance(lat1, lon1, lat2, lon2):
    return math.sqrt(
        (lat1 - lat2) ** 2 +
        (lon1 - lon2) ** 2
    ) * 111


def check_geofence(lat, lon):

    d = distance(
        lat,
        lon,
        SAFE_LAT,
        SAFE_LON
    )

    return d <= RADIUS