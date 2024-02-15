import requests

API_KEY = '5ca8870b01b52893554e49bf96d0d2c2'


def get_forecast(city_name):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}&units=metric'
    r = requests.get(url)
    content = r.json()['list']
    with open('data.txt', 'a') as f:
        for dict in content:
            date = dict['dt_txt']
            temp = dict['main']['temp']
            weather = dict['weather'][0]['description']
            f.write(f'{city_name},{date},{temp},{weather}\n')


print(get_forecast('Sofia'))