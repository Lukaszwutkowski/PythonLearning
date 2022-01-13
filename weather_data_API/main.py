import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "2b9b523c035deabd32599358929037a7"
account_sid = "AC9b1ee39e932dbc3ed528a21d8ee1dcd9"
auth_token = "8295aa955eb294d01e5ccf17c9f6769d"

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
        from_="+17166870572",
        to="Your verified number"
    )
    print(message.sid)
elif will_snow:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to snow today :)",
        from_="+17166870572",
        to="Your verified number"
    )
    print(message.sid)
else:
    print("Not necessary to take an umbrella.")


