import  requests
import json
# Start by importing the win32com package
import win32com.client as wincom

city = input(" Enter the name of the City\n")

url = f"http://api.weatherapi.com/v1/current.json?key=4adbce37700146d7b3f133836232306&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])
speak = wincom.Dispatch("SAPI.SpVoice")
text = f"Say 'The Current Whether in {city} is {r} degrees' "
speak.Speak(text)
