import requests

from flask import Flask
app = Flask(__name__)

api_key = "0fae9832d5533b6bd57d6b312dfe61a0"

@app.route('/')
def show_weather():
    city = "Boston"
    r = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}".format(city, api_key))
    return r.json()
