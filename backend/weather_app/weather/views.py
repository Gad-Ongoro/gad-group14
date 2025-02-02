from django.shortcuts import render
import requests

def get_weather(request):
    city = request.GET.get('city', 'Nairobi')
    api_key = 'WEATHER_API_KEY'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        weather_data = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
        }
    else:
        weather_data = {'error': 'City not found'}

    return render(request, 'weather/weather.html', {'weather_data': weather_data})
