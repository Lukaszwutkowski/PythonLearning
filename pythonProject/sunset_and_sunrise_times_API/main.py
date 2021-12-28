import requests

MY_LAT = "59.516855"
MY_LNG = "370.274504"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"].split("T")

print(sunrise.split("T")[1].split(":")[0])
print(sunset)
print(data)
