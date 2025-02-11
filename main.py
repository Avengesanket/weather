from tkinter import *
from tkinter import ttk
import requests

def get_data():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=0673b4ef4c13abfe93ca79600b9f7cec").json()
    print(data)
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    hum_label1.config(text=data["main"]["humidity"])

win = Tk()
win.title("Weather App")
win.config(bg="cyan")
win.geometry("500x570")

name_label = Label(win, text="Weather App", font=("Comic Sans MS", 30, "bold"))
name_label.place(x=25, y=25, height=50, width=450)
city_name = StringVar()
list_name = [
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Kolkata",
    "Chennai",
    "Hyderabad",
    "Pune",
    "Ahmedabad",
    "Jaipur",
    "Surat",
    "Lucknow",
    "Kanpur",
    "Nagpur",
    "Patna",
    "Indore",
    "Thane",
    "Bhopal",
    "Visakhapatnam",
    "Vadodara",
    "Firozabad",
    "Ludhiana",
    "Rajkot",
    "Agra",
    "Nashik",
    "Faridabad",
    "Meerut",
    "Kalyan-Dombivali",
    "Vasai-Virar",
    "Varanasi",
    "Srinagar",
    "Aurangabad",
    "Dhanbad",
    "Amritsar",
    "Navi Mumbai",
    "Allahabad",
    "Ranchi",
    "Haora",
    "Coimbatore",
    "Jabalpur",
    "Gwalior",
    "Vijayawada",
    "Jodhpur",
    "Madurai",
    "Raipur",
    "Kota",
    "Chandrapur",
    "Guwahati",
]
com = ttk.Combobox(win, text="Weather App", values=list_name, font=("Times New Roman", 20), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

w_label = Label(win, text="Weather Climate", font=("Times New Roman", 15,))
w_label.place(x=25, y=260, height=50, width=220)
w_label1 = Label(win, text="", font=("Times New Roman", 15,))
w_label1.place(x=250, y=260, height=50, width=220)

wd_label = Label(win, text="Weather Description", font=("Times New Roman", 15,))
wd_label.place(x=25, y=330, height=50, width=220)
wd_label1 = Label(win, text="", font=("Times New Roman", 15,))
wd_label1.place(x=250, y=330, height=50, width=220)

temp_label = Label(win, text="Temperature", font=("Times New Roman", 15,))
temp_label.place(x=25, y=400, height=50, width=220)
temp_label1 = Label(win, text="", font=("Times New Roman", 15,))
temp_label1.place(x=250, y=400, height=50, width=220)

hum_label = Label(win, text="Humidity", font=("Times New Roman", 15,))
hum_label.place(x=25, y=470, height=50, width=220)
hum_label1 = Label(win, text="", font=("Times New Roman", 15,))
hum_label1.place(x=250, y=470, height=50, width=220)

done_button = Button(win, text="Done", font=("Times New Roman", 20, "bold"), command=get_data)
done_button.place(x=200, y=190, height=50, width=100)

win.mainloop()