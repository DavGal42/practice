import requests

api_key = '4ce14ec96659e7a0d805d06e96444648'
city_name = 'London,uk'

url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

response = requests.get(url)
data = response.json()

print(data)
