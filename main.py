from datetime import datetime
import time

from python_simulation.gps_simulator import get_location
from python_simulation.geofence import check_geofence
from python_simulation.logger import log_data
from python_simulation.pdf_report import generate_pdf
from python_simulation.thingspeak_sender import update_thingspeak

# ==================================
# CONFIGURATION
# ==================================

VEHICLE_LOCKED = True
TOTAL_ITERATIONS = 20

# ==================================
# MAIN PROGRAM
# ==================================

try:

    print("\n====================================")
    print(" Vehicle Tracking System Started ")
    print("====================================\n")

    for i in range(TOTAL_ITERATIONS):

        # Get GPS Coordinates
        lat, lon = get_location()

        # Check Geofence
        safe = check_geofence(lat, lon)

        # Simulated Speed
        speed = 35

        # Vehicle Status
        if speed == 0:
            status = "PARKED"
        else:
            status = "MOVING"

        # Alert Logic
        if not safe and VEHICLE_LOCKED:

            alert = "THEFT ALERT"

        elif not safe:

            alert = "GEOFENCE ALERT"

        else:

            alert = "NONE"

        # Google Maps URL
        maps_url = f"https://maps.google.com/?q={lat},{lon}"

        print("\n==============================")
        print(f"Iteration : {i + 1}")
        print("==============================")
        print("Latitude  :", lat)
        print("Longitude :", lon)
        print("Status    :", status)
        print("Alert     :", alert)
        print("Speed     :", speed, "km/h")
        print("Maps URL  :", maps_url)

        # Save to CSV
        log_data([
            datetime.now(),
            lat,
            lon,
            status,
            alert
        ])

        # Upload to ThingSpeak
        update_thingspeak(
            lat,
            lon,
            status,
            alert,
            speed
        )

        print("ThingSpeak Updated")

        # ThingSpeak Free Plan Limit
        time.sleep(15)

except KeyboardInterrupt:

    print("\nProgram Stopped By User")

except Exception as e:

    print("\nError:", e)

finally:

    try:

        generate_pdf()

        print("\nPDF Report Generated Successfully")

    except Exception as e:

        print("\nPDF Generation Error:", e)

    print("\nSystem Shutdown Complete")