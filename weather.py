import datetime as dt
import requests

#Go to the read me to learn about the API key.
file_path = 'API.txt'
with open(file_path,'r') as file:
    API_KEY = file.read().strip()

BASE_URL = "https://api.openweathermap.org//data/2.5/weather?"


#The API returns the weather in Kelvin so this converts it to Fahrenheit 
def KelvinToFahrenheit(kelvin):
    fahrenheit = (kelvin-273.15) * (9/5) + 32
    return fahrenheit

#The API returns the wind speed in meters per second so this converts it to miles per hour 
def MPStoMPH(MPS):
    MPH = MPS * 2.23694
    roundedMPH = round(MPH,2)
    return roundedMPH

#Only use is to take the city from another file 
def Get_City(cit): 
    return cit

#Uses the Get_City function to make a url so it can find the info about the city
def Make_Url(city):
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city
    return url

#Uses the Make_Url function to make a request so it can get the info about the city
def generate_response(url):
    response = requests.get(url).json()
    return response


#The functions below correspond to one button in the GUI file and they take info from the functions above
def temp(response,city):
    Tempkelvin = response['main']['temp']
    Tempfahrenheit = KelvinToFahrenheit(Tempkelvin)
    PrintTemp = f"Temperature in {city} is: {Tempfahrenheit:.2f} °F"
    return PrintTemp

def FL(response,city):
    FeelsLikeKelvin = response['main']['feels_like']
    FeelsLikeFahrenheit = KelvinToFahrenheit(FeelsLikeKelvin)
    PrintFeelsLike = f"Temperature in {city} feels like: {FeelsLikeFahrenheit:.2f} °F"
    return PrintFeelsLike

def WindSpeed(response,city):
    WindSpeed = response['wind']['speed']
    MPSWindSpeed = MPStoMPH(WindSpeed)
    PrintWindSpeed = f"Wind speed in {city} is: {MPSWindSpeed} mi/h"
    return PrintWindSpeed

def Humidity(response,city):
    Humidity = response['main']['humidity']
    PrintHumidity = f"Humidity in {city} is: {Humidity}%"
    return PrintHumidity

def Desc(response,city):
    Description = response['weather'][0]['description']
    PrintGeneralWeather = f"Sky Conditions in {city} is: {Description}"
    return PrintGeneralWeather

def sunrise(response,city):
    SunriseTime = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    PrintSunRise = f"Sun rises in {city} at: {SunriseTime} local time"
    return PrintSunRise

def sunset(response,city):
    SunsetTime = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
    PrintSunSet = f"Sun set in {city} at: {SunsetTime} local time"
    return PrintSunSet









