import requests
from datetime import datetime, timezone
import time

MY_LAT = 30.475663
MY_LNG = 74.556521

def is_iss_overhead():
    """Check if ISS is near your location."""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LNG - 5) <= iss_longitude <= (MY_LNG + 5):
        return True
    return False


def is_night():
    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LNG,
        "formatted" : 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour   # <-- FIXED LINE ✅

    if time_now >= sunset or time_now <= sunrise:
        return True



while True:
    time.sleep(60)
    try:
        if is_iss_overhead() and is_night():
            print("🌌 ISS Overhead! Look up!")
        else:
            print(f"{datetime.now()}: Not Overhead.")
    except Exception as e:
        print(f"⚠️ Error: {e}")
