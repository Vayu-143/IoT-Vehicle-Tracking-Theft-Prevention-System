import requests

API_KEY = "YOUR_API_KEY_HERE"


def update_thingspeak(
        latitude,
        longitude,
        status,
        alert,
        speed):

    url = "https://api.thingspeak.com/update"

    payload = {
        "api_key": API_KEY,
        "field1": latitude,
        "field2": longitude,
        "field3": status,
        "field4": alert,
        "field5": speed
    }

    try:

        response = requests.get(
            url,
            params=payload,
            timeout=10
        )

        print(
            "ThingSpeak Response:",
            response.text
        )

    except Exception as e:

        print(
            "ThingSpeak Error:",
            e
        )