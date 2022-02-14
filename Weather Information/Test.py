import json
import requests
from tkinter import *

API_Key = '2d3bfa3a7b559ee80c6ce1811f0994bd'
city = ''
root = Tk()
root.geometry("600x300")
root.title("Weather Information")


def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    if (INPUT != ""):
        global city
        city = INPUT
        base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city
        weather_data = requests.get(base_url).json()

        Output.insert(END, weather_data)
    else:
        Output.insert(END, "Please write a valid city name!")


l = Label(text="Enter City Name :")
inputtxt = Text(root, height=2,
                width=25,
                bg="light yellow")

Output = Text(root, height=20,
              width=44,
              bg="light cyan")

Display = Button(root, height=2,
                 width=20,
                 text="Show",
                 command=lambda: Take_input())

l.pack()
inputtxt.pack()
Display.pack()
Output.pack()

mainloop()
