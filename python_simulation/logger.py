import csv
import os

FILE = "data/vehicle_log.csv"


def log_data(data):

    file_exists = os.path.isfile(FILE)

    with open(FILE, "a", newline="") as f:

        writer = csv.writer(f)

        if not file_exists:

            writer.writerow([
                "timestamp",
                "latitude",
                "longitude",
                "status",
                "alert"
            ])

        writer.writerow(data)