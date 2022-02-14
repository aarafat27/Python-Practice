# Weather Information
import tkinter
import tkinter as tk
# from tkinter.constants import *
import requests

# from pprint import pprint
API_Key = '2d3bfa3a7b559ee80c6ce1811f0994bd'
# city = input('Enter a city: ')
# base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city
# weather_data = requests.get(base_url).json()
# pprint(weather_data)
import json

frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x400')

city = ''


def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    global city
    city = inp
    # lbl.config(text="Provided Input: " + inp)
    return city


print(city)


def showData():
    c = printInput()
    base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + c
    weather_data = requests.get(base_url).json()
    y = json.dumps(weather_data)
    # lbl.config(text="Weather Data: " + y)
    Output.config(END +' ' +y)


# TextBox Creation
inputtxt = tk.Text(frame,
                   height=2,
                   width=20)

inputtxt.pack()

# Button Creation
printButton = tk.Button(frame,
                        text="Print",
                        command=showData)
printButton.pack()

# Label Creation
# lbl = tk.Label(frame, text="")
# lbl.pack()
Output = tk.Text(frame, height=5,
                 width=25,
                 bg="light cyan")

Output.pack()
frame.mainloop()
