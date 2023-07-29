# django_fetch_weather
Just a simple DJANGO project to FETCH weather data from OpenWeatherMap

The reason a low quality ICON is being displayed on the card is due to how OpenWeatherMap displays them! Not my fault >.<

<img src="https://i.imgur.com/cbVeXUk.png" alt="Before Fetching"> 

<img src="https://i.imgur.com/qWgfnaT.png" alt="After Fetching"> 

<h1>How to Run:</h1>
<hr>
1. Install all the necessary folders along with django..
2. cd "weather_webapp", go into main/views and ADD your own OpenWeatherMAP API key.
3. python manage.py runserver (FINISHED!)
4. IF you get an error after STEP 3, try to run these commands: 
- python manage.py makemigrations 
- python manage.py migrate
- python manage.py runserver
