from time import strftime
import requests
from django.shortcuts import render, redirect
import datetime
import timezonefinder
import pytz
import json
from django.contrib import messages


def index(request):

    if request.method == 'POST':

        user_api = "8ccf65d9d8d8eae4bd584def104aac1b"
        city = request.POST.get("city")
        complete_api_link = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={user_api}'
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()

        try:
            city_name = api_data['name']
            temperature = api_data['main']['temp'] - 273.15
            weather = (api_data['weather'][0]['description']).title()
            wind = api_data['wind']['speed']
            humidity = api_data['main']['humidity']
            pressure = api_data['main']['pressure']
            icon = api_data['weather'][0]['icon']

            # Time

            tf = timezonefinder.TimezoneFinder()

            timezone_str = tf.certain_timezone_at(
                lat=api_data['coord']['lat'], lng=api_data['coord']['lon'])

            if timezone_str is None:
                print("Could not determine the time zone")
            else:
                # Display the current time in that time zone
                timezone = pytz.timezone(timezone_str)
                dt = datetime.datetime.utcnow()
                time = (dt + timezone.utcoffset(dt)).strftime("%H:%M")

            params = {
                'city_name': city_name,
                'temperature': round(temperature),
                'weather': weather,
                'wind': wind,
                'humidity': humidity,
                'pressure': pressure,
                'icon': icon,
                'time': time,
            }
            return render(request, 'index.html', params)
            
        except KeyError:
            messages.error(request, 'City not found!')
            return redirect('index')

        
            

        
    else:

        # current_location = requests.get('http://ipinfo.io/json')
        # place = current_location.json()

        user_api = "8ccf65d9d8d8eae4bd584def104aac1b"
        city = 'Ahmedabad'
        complete_api_link = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={user_api}'
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()
        city_name = api_data['name']
        temperature = api_data['main']['temp'] - 273.15
        weather = (api_data['weather'][0]['description']).title()
        wind = api_data['wind']['speed']
        humidity = api_data['main']['humidity']
        pressure = api_data['main']['pressure']
        icon = api_data['weather'][0]['icon']

        # Time

        tf = timezonefinder.TimezoneFinder()

        timezone_str = tf.certain_timezone_at(
            lat=api_data['coord']['lat'], lng=api_data['coord']['lon'])

        if timezone_str is None:
            print("Could not determine the time zone")
        else:
            # Display the current time in that time zone
            timezone = pytz.timezone(timezone_str)
            dt = datetime.datetime.utcnow()
            time = (dt + timezone.utcoffset(dt)).strftime("%H:%M")

        params = {
            'city_name': city_name,
            'temperature': round(temperature),
            'weather': weather,
            'wind': wind,
            'humidity': humidity,
            'pressure': pressure,
            'icon': icon,
            'time': time
        }

        return render(request, 'index.html', params)
