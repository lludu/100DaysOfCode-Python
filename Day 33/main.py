# # -------------------- MODULES -------------------- #
import requests
# API REQUEST DOCUMENTATION  # https://docs.python-requests.org/en/master/user/quickstart/
from datetime import datetime
# DATETIME DOCUMENTATION # https://docs.python.org/3/library/datetime.html
import smtplib
#  Email SMPT Documentation  #  https://docs.python.org/3/library/smtplib.html
import time
from password import *
#  Data file including MY_LAT, MY_LNG, MY_EMAIL, MY_EMAIL_CONNECTION, E_PASS, RECEIVING_EMAIL, and KEY (API Key for DST Website)


# # -------------------- DAYLIGHT SAVINGS TIME Data from the https://app.abstractapi.com/api/timezone/tester -------------------- #
response = requests.get(f"https://timezone.abstractapi.com/v1/current_time/?api_key={KEY}&location={MY_LAT},{MY_LNG}")
DST_CHECKER = response.json()["is_dst"] # Returns boolean true, false if currently daylightsavings
GMT_OFFSET = response.json()["gmt_offset"] # Timezone's offset from Greenwich Mean Time (GMT).
TZONE = response.json()["timezone_abbreviation"] # Current Time Zone
# print(GMT_OFFSET)

def get_position():
    # # -------------------- ISS LOCATION API http://open-notify.org/Open-Notify-API/ISS-Location-Now/ -------------------- #
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # print(response.status_code) # Shows the status code i.e. 200 / 404
    response.raise_for_status()  # Shows raised exception for errors
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f'ISS Position: {iss_latitude}, {iss_longitude}')
    print(f'My Current Location: {MY_LAT}, {MY_LNG}')


    # Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True
    else:
        return False


def email():
    with smtplib.SMTP(MY_EMAIL_CONNECTION) as connection:
        connection.starttls()  # secure the email connection
        connection.login(user=MY_EMAIL, password=E_PASS)
        if get_position() and is_night():
            connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=RECEIVING_EMAIL,
                            msg="Subject:ISS in Visible Range!\n\n"
                                f"Look Up, the ISS is above you, you can see it")
        else:
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=RECEIVING_EMAIL,
                                msg="Subject:ISS Not in Visible Range!\n\n"
                                    f"It is not in range, you cannot view it now")
        print("Msg Sent")

# # -------------------- Sunrise Sunset API https://sunrise-sunset.org/api -------------------- #

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise_utc = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) # Hour of Sunrise in UTC
    if sunrise_utc == 00:
        sunrise_utc = 24
    sunrise = sunrise_utc + GMT_OFFSET # Hour of Sunrise in Local Time
    # print(sunrise)


    sunset_utc = int(data["results"]["sunset"].split("T")[1].split(":")[0]) # Hour of Sunset in UTC
    if sunset_utc == 00:
        sunset_utc = 24
    sunset = sunset_utc + GMT_OFFSET # Hour of Sunset in Local Time
    # print(sunset)


    time_now = datetime.now().hour
    # print(time_now)

    if time_now >=sunset or time_now<=sunrise:
        print("It's Night")
        return True
    else:
        print("It's Day")
        return False



# # -------------------- Run Bot Program -------------------- #
get_position()
is_night()
print("")

while True:
    time.sleep(60)
    if get_position() and is_night():
        email()
        print("Yes, it is above you, you can see it")
    else:
        print("No, You cannot see it")
