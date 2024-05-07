# api key = d39f180958284aa688c111745242301
#  endpoint = https://api.weatherapi.com/v1/current.json?key=

import requests
import json
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")

city = input("enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=d39f180958284aa688c111745242301&q={city}" 

r = requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
text = f"the current weather in {city} is {w} degrees !"
speak.Speak(text)