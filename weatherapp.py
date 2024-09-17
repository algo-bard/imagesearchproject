from tokenize import endpats

import requests
import json

api_key = "ae7e7979bc3ad586c03607697ad5733a"

clouds = "Cloudy"
thunderstorm = "Thunderstorms"
rain = "Rainy"
atmosphere = "Foggy"
clear = "Clear skies"

while True:
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city = input("Enter city: ")

    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")

    print(res.json())

    weather = (res.json())['weather'][0]['main']
    temp = (res.json())['main']['temp']

    print(weather)

    if weather == "Clouds":
        print(clouds, "at", city)

    elif weather == "Thunderstorms":
        print(thunderstorm, "at", city)


    elif weather == "Rain":
        print(rain, "at", city)


    elif weather == "Atmosphere":
        print(atmosphere, "at", city)


    elif weather == "Clear":
        print(clear, "at", city)

    else:
        print("Incorrect input. Please try again")




