import random
import time
from datetime import datetime

from python_simulation.thingspeak_sender import update_thingspeak

# ==================================
# MODES
# ==================================

MODE = "NORMAL"

# NORMAL
# GEOFENCE
# THEFT

while True:

    if MODE == "NORMAL":

        latitude = (
            12.9716 +
            random.uniform(-0.003, 0.003)
        )

        longitude = (
            77.5946 +
            random.uniform(-0.003, 0.003)
        )

        status = "MOVING"
        alert = "NONE"
        speed = random.randint(25, 60)

    elif MODE == "GEOFENCE":

        latitude = 13.5000
        longitude = 78.0000

        status = "MOVING"
        alert = "GEOFENCE ALERT"
        speed = random.randint(40, 70)

    elif MODE == "THEFT":

        latitude = 13.7000
        longitude = 78.3000

        status = "THEFT"
        alert = "THEFT ALERT"
        speed = random.randint(60, 90)

    print(
        datetime.now(),
        latitude,
        longitude,
        status,
        alert
    )

    update_thingspeak(
        latitude,
        longitude,
        status,
        alert,
        speed
    )

    # ThingSpeak Free Limit
    time.sleep(15)