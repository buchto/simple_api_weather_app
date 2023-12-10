import requests

api = '31035865bee0d0fc42a76ee570dc1bd2'

user_input = input('Enter city: ')

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&appid={api}")

if weather_data.json()['cod'] == '404':
    print('City not found')
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

print(f'The weather in {user_input} is {weather}')
print(f'The temperature in {user_input} is {temp}°F')
