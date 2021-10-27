#WeatherApp.py
#Name: Noah Busack
#Date: 10/26/2021
#Assignment: Weather Assignment

import WeatherInfo

#Set your key

WeatherInfo.setKey("6b04b92feb317046e6d27d2261c3e291")

#Ask the user for their city

Str city = raw_input("")

#Update the weather with the given city

success = WeatherInfo.updateWeather()

if(success == True):
  print("It worked")
else:
  print("Invalid City")
  
#Request any data you need from the WeatherInfo API

des = getDescription()
temp = getTemp()
fl = getFeelsLike()
hum = getHumidity()
pres = getPressure()
ws = getWindSpeed()

#Process the data



#convert temperature to fahrenheit,

 temp = (getTemp() -273.15) * 9/5 + 32

#determine wind speed in words

print("the wind speed is " + (getWindSpeed) + " mph."

#decide jacket and umbrella status
      
      if hum == 100:
      print("you should carry an umbrella")
      if temp < 40:
      print("you should wear a jacket")
      
#Report to the user the weather of their city
      
      print(des + "the tempurature is " + temp + " the humidity is " + humidity + " the wind speed is " + ws + " 

#Ask user if they would like another weather report
#If yes, loop to the top of your program where they are asked for a city.
#If no, end with a goodbye statement of some sort.
