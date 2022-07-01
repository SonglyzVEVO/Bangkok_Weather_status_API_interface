import requests
from datetime import datetime
import time
import logging


class WeatherStatus:

    def __init__(self, city):
        # API call : https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
        self.API_KEY = '3eea872d8a092a6988b16f4470d17c3e'
        self.BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

        # default city
        self.city = city
        self.request_url = f"{self.BASE_URL}?appid={self.API_KEY}&q={self.city}"

        # data storage json file
        self.current_data_weather = self.request_data()

    @staticmethod
    def get_time():
        now = datetime.now()
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        return date_time_str

    def change_city(self, new_city):
        self.city = new_city


    def request_data(self):
        response = requests.get(self.request_url)
        # status_code 2xx = Success ,200 = OK
        if response.status_code == 200:
            data = response.json()
            return data
        elif response.status_code == 404:
            print("Error 404 page not found")
        elif response.status_code == 502:
            print("Bad Gate Way")
        elif response.status_code == 407:
            print("Proxy Authentication Required")
        else:
            print("An error occurred.")

    def show_current_data_weather(self):

        # Current_Time
        print("Area :", self.city, 'DateTime String:', self.get_time())

        # Weather
        weather = self.current_data_weather['weather'][0]['description']
        # f"" is string format all in "------" just like a = 5 ; print(f"A : {a}")
        print(f"Current Weather : {weather}")

        # Temp, Pressure, Humidity
        temperature = self.current_data_weather["main"]["temp"]
        temp_celcius = round(temperature - 273)
        pressure = self.current_data_weather["main"]["pressure"]
        humidity = self.current_data_weather["main"]["humidity"]
        print(f'T : {temp_celcius} celcius, P : {pressure} hPa, H : {humidity} %')

        # Wind Speed, Wing Degree
        wind_speed = self.current_data_weather["wind"]["speed"]
        wind_deg = self.current_data_weather["wind"]["deg"]
        print(f'Wind Speed : {wind_speed}, Wind Degree : {wind_deg}')
        print("---------------------------------------------------")




if __name__ == "__main__":
    x = WeatherStatus("New york")
    while True:
        x.request_data()
        x.show_current_data_weather()
        time.sleep(5)

