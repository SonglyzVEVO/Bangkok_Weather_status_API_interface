#need install module before follow this command : pip install requests
import requests
from datetime import datetime
import time

#API call : https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
API_KEY = '3eea872d8a092a6988b16f4470d17c3e'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
city = 'Bangkok'
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

def request_data_n_show():
    while True:
        response = requests.get(request_url)

        # status_code 2xx = Success ,200 = OK
        if response.status_code == 200:

            data = response.json()

            now = datetime.now()
            date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
            print("Area :", city, 'DateTime String:', date_time_str)

            weather = data['weather'][0]['description']
            # f"" is string format all in "------" just like a = 5 ; print(f"A : {a}")
            print(f"Current Weather : {weather}")

            temperature = data["main"]["temp"]
            temp_celcius = round(temperature - 273)
            pressure = data["main"]["pressure"]
            humidity = data["main"]["humidity"]
            print(f'T : {temp_celcius} celcius, P : {pressure} hPa, H : {humidity} %')

            wind_speed = data["wind"]["speed"]
            wind_deg = data["wind"]["deg"]
            print(f'Wind Speed : {wind_speed}, Wind Degree : {wind_deg}')
            print("---------------------------------------------------")

        elif response.status_code == 404:
            print("Error 404 page not found")
        elif response.status_code == 502:
            print("Bad Gate Way")
        elif response.status_code == 407:
            print("Proxy Authentication Required")
        else:
            print("An error occurred.")

        time.sleep(10)

if __name__ == "__main__":
   request_data_n_show()
