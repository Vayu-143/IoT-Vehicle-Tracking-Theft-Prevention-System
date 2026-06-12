import requests

WRITE_API_KEY = "0IU6P7UH51NO8EHU"


def update_thingspeak(
    latitude,
    longitude,
    status,
    alert,
    speed
):
    url = "https://api.thingspeak.com/update"

    payload = {
        "api_key": WRITE_API_KEY,
        "field1": latitude,
        "field2": longitude,
        "field3": status,
        "field4": alert,
        "field5": speed
    }

    try:
        response = requests.post(
            url,
            data=payload,
            timeout=10
        )

        print(
            f"ThingSpeak Updated: {response.text}"
        )

    except Exception as e:
        print(
            f"ThingSpeak Error: {e}"
        )