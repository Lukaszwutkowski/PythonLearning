import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "WEATHERAPI"
account_sid = "TWILIOSID"
auth_token = "TWILIOTOKEN"

auth_phone = "AUTHPHONE"

weather_params = {
    "lat": 59.490269,
    "lon": 10.314810,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
will_snow = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 600:
        will_rain = True
    elif 600 <= int(condition_code) < 700:
        will_snow = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today :)",
        from_=auth_phone,
        to="Your verified number"
    )
    print(message.sid)
elif will_snow:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to snow today :)",
        from_=auth_phone,
        to="Your verified number"
    )
    print(message.sid)
else:
    print("Not necessary to take an umbrella.")


