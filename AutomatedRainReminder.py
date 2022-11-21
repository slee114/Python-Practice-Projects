import smtplib

import requests
OWM_Endpoint = "api endpoint for openweathermap.org"
api_key = "your api key from openweathermap.org"

parameters = {
    "lat": 47.606209,
    "lon": -122.332069,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}

response = requests.get(OWM_Endpoint,params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]
print(weather_slice)


will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain == True:
    with smtplib.SMTP("smtp.gmail.com") as email_response:
        email_response.starttls()
        email_response.login(user="your email", password="your password")
        email_response.sendmail(from_addr="your email", to_addrs="recipients email", msg="Subject:It's going to Rain!\n\nBring an Umbrella!")
    print("Bring an Umbrella")
