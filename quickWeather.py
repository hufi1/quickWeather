#! python3
# -- quickWeather.py -- takes a command line argument and pulls the weather from
# openweathermap.com with the requests-module

### Hufi
### 27.07.2020

import json, requests, sys

# Compute location from command line arguments
if len(sys.argv) < 2 :
   print('Usage: quickWeather location[example: Angern an der March, AT]')
   sys.exit()
location = ''.join(sys.argv[1:])

APPID = 'YOUR OPENWEATHERMAP API KEY'

# Download the JSON data from openweathermap.org's API
url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s&units=metric&lang=de' % (location, APPID)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# print weather descriptions
w = weatherData['list']

print ('Derzeitiges Wetter in %s:' %(location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print('min. Temperatur: ', round(w[0]['main']['temp_min']))
print('max. Temperatur: ', round(w[0]['main']['temp_max']))
print('Luftfeuchtigkeit: ',w[0]['main']['humidity'] , '%')
print()
print ('Morgiges Wetter:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print('min. Temperatur: ', round(w[1]['main']['temp_min']))
print('max. Temperatur: ', round(w[1]['main']['temp_max']))
print('Luftfeuchtigkeit: ',w[1]['main']['humidity'] , '%')
print()
print ('Übermorgen:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
print('min. Temperatur: ', round(w[2]['main']['temp_min']))
print('max. Temperatur: ', round(w[2]['main']['temp_max']))
print('Luftfeuchtigkeit: ',w[2]['main']['humidity'] , '%')
