import requests
from tkinter import *
from tkinter import messagebox


KEY_API = '79b6eb596c50dd2b8c9ff241ee824ed9'
URL_BASE = "http://api.openweathermap.org/data/2.5/weather?"

def the_weather(your_city):
    url = f"{URL_BASE}appid={KEY_API}&q={your_city}"
    res = requests.get(url)
    return res.json()

def search_it():
    your_city = city_text_is.get()
    weather_is = the_weather(your_city)
    if weather_is and weather_is.get('cod') != '404':
        location['text'] = f"{weather_is['name']}, {weather_is['sys']['country']}"
        temp_cel = weather_is['main']['temp'] - 273.15
        temp_label['text'] = f"{temp_cel:.2f} °C"
        weather_lable['text'] = weather_is['weather'][0]['description'].capitalize()
    else:
        messagebox.showerror('Error:', f"unable to find city '{your_city}'")

application = Tk()
application.title("The Weather App")
application.geometry("350x210")

city_text_is = StringVar()
entry_city = Entry(application, textvar=city_text_is)
entry_city.pack()

btn_search = Button(application, text="Search to know Weather", command=search_it)
btn_search.pack()

location = Label(application, text="Your Location", font=('bold', 18))
location.pack()

temp_label = Label(application, text="")
temp_label.pack()

weather_lable = Label(application, text="")
weather_lable.pack()

application.mainloop()