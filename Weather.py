import requests


def return_weather(place):
    words = place.split(" ")
    r = data = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=' + words[1] + '&APPID=5305e66d631b9da248c2112c5f48c600')
    if data.json()['cod'] == 200:
        weather = data.json()['weather'][0]['description']
        loc = data.json()['name']
        msg = "The weather forecast for " + loc + " is: " + weather
        return msg
    else:
        msg = "The Location provided is incorrect"
        return msg


