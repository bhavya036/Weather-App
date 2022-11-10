#LIVE WEATHER APP WITH TKINTER GUI

from tkinter import *
from tkinter import ttk #for combo box(For shawing Multiple option in a 1 click)
import requests
import json

with open('state_district.json', 'r') as fp:
    statesDis = json.loads(fp.read())  #Data is converted into python format

cities = []
for i in statesDis:
    [cities.append(j) for j in i['districts']]

cities.sort()

def data_get():
    City = City_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+City+"&appid=3a01b4a65701defe543f80ea3f213f21").json()
    w_label1.config(text = data["weather"][0]["main"])
    wb_label1.config(text = data["main"]["humidity"])
    temp_label1.config(text = str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text = data["main"]["pressure"])


win = Tk()
win.title("Tech Bjpatel")
win.config(bg="pale green")
win.geometry("500x500")

name_label = Label(win,text="Accurate Weather App",fg = "darkblue",bg="lightpink",font=("Tmes New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

City_name = StringVar()


com = ttk.Combobox(win,font=("Times New Roman",15,"bold"),values = cities,textvariable=City_name)
com.place(x=25,y=120,height=50,width=450)

w_label = Label(win,text="Weather Climate",fg = "darkblue",bg="lightpink",font=("Tmes New Roman",15))
w_label.place(x=25,y=250,height=30,width=160)
w_label1 = Label(win,text=" ",fg = "darkblue",bg="lightpink",font=("Tmes New Roman",15))
w_label1.place(x=250,y=250,height=30,width=160)

wb_label = Label(win,text="Weather Humidity",fg = "darkblue",bg="lightpink",font=("Tmes New Roman",13))
wb_label.place(x=25,y=300,height=30,width=160)
wb_label1 = Label(win,text=" ",fg = "darkblue",bg="lightpink",font=("Tmes New Roman",13))
wb_label1.place(x=250,y=300,height=30,width=160)

temp_label = Label(win,text="Temperature",fg = "darkblue",bg="lightpink",font=("Tmes New Roman",13))
temp_label.place(x=25,y=350,height=30,width=160)
temp_label1 = Label(win,text=" ",fg = "darkblue",bg="lightpink",font=("Tmes New Roman",13))
temp_label1.place(x=250,y=350,height=30,width=160)

per_label = Label(win,text="perssure",fg = "darkblue",bg="lightpink",font=("Tmes New Roman",13))
per_label.place(x=25,y=400,height=30,width=160)
per_label1 = Label(win,text=" ",fg = "darkblue",bg="lightpink",font=("Tmes New Roman",13))
per_label1.place(x=250,y=400,height=30,width=160)


done_button = Button(win,text="DONE",fg = "darkblue",bg="lightpink",font=("Tmes New Roman",20,"bold"),command = data_get)
done_button.place(x=200,y=190,height=50,width=100)

win.mainloop()
