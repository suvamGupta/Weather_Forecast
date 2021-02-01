import os
import requests
import json
from datetime import datetime

api_key = os.environ['open_weather']
city_name = input('\nEnter the city name : ').strip()

# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

complete_api_link = 'https://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key

api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print(api_data['message'].capitalize())
    a = input()
else:
    weather_desc = api_data['weather'][0]['description']
    temp_city = float(api_data['main']['temp']) - 273.15
    humid = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    city_name = api_data['name']
    city_id = api_data['id']
    date_time = datetime.now().strftime("%d-%b-%Y | %I:%M:%S %p")

    print('\n------------------------------------------------------------------------------------')
    print('Weather stats for -> {} | City-id : {} | [{}]'.format(city_name, city_id, date_time))
    print('------------------------------------------------------------------------------------\n')

    print('Current Temperature   :  {:.2f} deg Celcius'.format(temp_city))
    print('Weather Discription   :  {}'.format(weather_desc))
    print('Wind Speed            :  {} kmph'.format(wind_spd))
    print('Humidity              :  {} %\n'.format(humid))
    b = input()

# def main():
#     pass

# if __name__ == '__main__':
#     main()