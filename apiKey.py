import requests
baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID': '8e726de64b04b2ec692093a59564c36c'
 ,'q' : 'New Delhi,India'}
response = requests.get(baseUrl, params=parameters)
print(response.content)
