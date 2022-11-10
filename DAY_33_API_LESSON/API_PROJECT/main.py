import requests
from datetime import datetime
import smtplib
from time import sleep
MY_EMAIL = "sideprojectpython@gmail.com"
PASSWORD = "crghykxyzuoorofn"

# TO-DO: If the ISS is over my position, send an email

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=MY_EMAIL, password=PASSWORD)


LOCAL_UTC_OFFSET = -3


def utc_to_local(utc_hour):
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour


MY_LAT = -8.055190  # Your latitude
MY_LONG = -34.871181  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
print(iss_latitude)
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_longitude)

# Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
lt_sunrise = utc_to_local(sunrise)
print(lt_sunrise)

sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
lt_sunset = utc_to_local(sunset)
print(lt_sunset)

time_now = datetime.now()
time_now = time_now.hour
print(time_now)
while True:
    if time_now >= lt_sunset or time_now < lt_sunrise:
        print("time True")
        if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg="Subject: Look up \n\n The ISS is in the sky.")
            print("send it")
            break
        # else:
        #     connection.sendmail(from_addr=MY_EMAIL,
        #                         to_addrs=MY_EMAIL,
        #                         msg="Subject: Look up \n\n The ISS is NOT in the sky.")
        #     print("send it")
    sleep(60)


## Se for entre lat = -3 or -13 and long = -29 or -39, and time_now => lt_sunset or time_now < lt_sunrise:
## Send email


# If the ISS is close to my current position
# And it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
