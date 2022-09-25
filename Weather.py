import requests
API_KEY = "148235d26d4539e83d10e874d9c98642"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    # print(data)
    country = data['sys']['country']
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)
    feels_like = round(data["main"]["feels_like"] - 273.15, 2)
    temp_min = round(data["main"]["temp_min"] - 273.15, 2)
    temp_max = round(data["main"]["temp_max"] - 273.15, 2)
    humidity = round(data["main"]["humidity"] , 2)
    print("Country: ", country)
    print("Weather: ", weather)
    print("Temperature: ", temperature, "celsius")
    print ("Feels Like: ", feels_like,"celcious")
    print("Minimum Temperature: ", temp_min,"celcious" )
    print("Maximum Temperature: ", temp_max,"celcious" )
    print("Humidity: ", humidity)
    
else:
    print("An Error Occured.")