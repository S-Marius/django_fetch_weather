from django.shortcuts import render
from django.views import View

import urllib.request
from urllib.parse import quote
import json

# Replace with your actual OpenWeather API key
api_key = "HIDDEN/"



# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        # Extract HTML Form data
        location = request.POST['location']
        country_code = request.POST['country-code']

        # URL parser
        base_url = "https://api.openweathermap.org/data/2.5/weather?q="
        encoded_location = quote(location)  # Encode the location name
        url = f"{base_url}{encoded_location},{country_code}&appid={api_key}"

        try:

            # ACCEPTING Response
            response = urllib.request.urlopen(url)
            json_data = json.loads(response.read())

            # Convert temperature from Kelvin to Celsius
            temperature_celsius = json_data['main']['temp'] - 273.15

            # Retrieve the weather data from the JSON response
            weather_data = {
                "temperature": round(temperature_celsius, 0),
                "weather_name": json_data['weather'][0]['main'],
                "pressure": json_data['main']['pressure'],
                "humidity": json_data['main']['humidity'],
                "wind_speed": round(json_data['wind']['speed'] * 3.6, 0),
                "cloudiness": json_data['clouds']['all'],
                "location": json_data['name'],
                "country_code": json_data['sys']['country'],
                "weather_icon": json_data['weather'][0]['icon'],
            }
            print(weather_data)
            return render(request, 'index.html', {'weather_data': weather_data})
        except:
            return render(request, 'index.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
