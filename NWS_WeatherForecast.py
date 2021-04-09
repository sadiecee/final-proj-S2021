'''
Sadie Murray
Python 3 
4/8/2021
This is a webscrapping code that takes a lat/long value input by the user and outputs a five day weather forecast for that lat/long value 
from forecast.weather.gov. 
'''

# import required libraries
import requests
from bs4 import BeautifulSoup

# Create an empty list to store response
forecast = []

## Provide the latitude and longitude for the location you would like to check the forecast for
## Lat/lon in decimal degrees provided for Worcester, MA
lat = str(round(float(input("Please input your latitude in decimal degrees: ")),4))
lon = str(round(float(input("Please input your longitude in decimal degrees: ")),4))
#lat = '42.2634'
#lon = '-71.8022'

# Create url for the requested location through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon

# Check if the URL exists
# print url
request = requests.get(url)
if request.status_code == 200:
    print(url)
else: 
  print("Error. No data for that location.")


# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate elements on page to be scraped
# findAll() locates all occurrences of div tag with the given class name
# stores it in the BeautifulSoup object
weather_forecast = soup.findAll("li", {"class": "forecast-tombstone"})

# Loop through the BeautifulSoup object to extract text text from every class instance using .text
# Store results in a list
for i in weather_forecast:
    i = i.text
    forecast.append(i)

# Print list to remove unicode characters
for day in forecast:
    day = day.replace('A',' A')
    day = day.replace('L',', L')
    day = day.replace('H',', H')
    day = day.replace('N',' N')
    print(day.upper())
