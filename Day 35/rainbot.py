import requests
from password import *

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN


weather_parameters = {
        "lat": LAT,
        "lon": LON,
        "appid": API_KEY,
        "exclude": "current,minutely,daily"
    }

response = requests.get(OWM_Endpoint, params=weather_parameters)
# print(response.status_code)
response.raise_for_status()
weather_data = response.json()


# -----Andrew Version------#
rain_codes = []
for hour_data in range(12):
    hour_code = weather_data["hourly"][hour_data]["weather"][0]["id"]
    if hour_code < 700:
        rain_codes.append(hour_code)

if len(rain_codes) != 0:
    print("Bring a raincoat")
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="There is a high probability that it's going to rain today, Bring a raincoat ☔",
        from_='+14439125051',
        to='+17178917297'
    )


    print(message.sid)
    print(message.status)
else:
    print("All Clear!")
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It shouldn't rain today! Good Luck!",
        from_='+14439125051',
        to='+17178917297'
    )

    print(message.sid)
    print(message.status)


print(rain_codes)
















# Angela Code
# hour_code = weather_data["hourly"][0]["weather"][0]["id"] # First hourly weather code id
# # print(hour_code) # First hourly weather code id
#
# weather_slice = (weather_data["hourly"])[:12] # First 12 Hourly Data
#
# will_rain = False
#
# for hour_data in weather_slice:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) > 700:
#         will_rain = True
#
# if will_rain:
#     print("Bring a raincoat")
#     client = Client(account_sid, auth_token)
#
#     message = client.messages \
#         .create(
#         body="There is a high probability that it's going to rain today, Bring a raincoat ☔",
#         from_='+14439125051',
#         to='+17178917297'
#     )
#
#
#     print(message.sid)
#     print(message.status)











