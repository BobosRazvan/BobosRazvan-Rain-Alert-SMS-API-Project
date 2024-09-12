import requests
import os
from twilio.rest import Client

account_sid = ""
auth_token = ""





def get_weather_forecast(lat, lon, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "cnt": 4,
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()


# Use the function
lat = 51.0
lon = 16.0
api_key = ""

forecast = get_weather_forecast(lat, lon, api_key)


bring_an_umbrela = 0
for i in range(0, 3):
    if forecast['list'][i]['weather'][0]['id'] < 700:
        bring_an_umbrela = 1

if bring_an_umbrela == 0:
    print("It is not raining today you won t need an umbrella")
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Astazi va ploua. Nu uita sa iti iei o umbrela cu tine!",
        from_="",
        to="",
    )

    print(message.status)
