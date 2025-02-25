import tkinter as tk
from geopy.geocoders import Nominatim

def change_adress():
    latitude = latitude_Entry.get()
    longitude = longitude_Entry.get()
    geolocator = Nominatim(user_agent="geo_locator")
    location = geolocator.reverse((latitude, longitude))
    adress_label.config(text=f"Address: {location}")

project_font = ("Arial", 15)

windows = tk.Tk()
windows.title("Location Finder With Longitude and Latitude")
windows.geometry("600x500")

latitude_text = tk.Label(windows, text="Enter Latitude: ", font=project_font)
latitude_text.grid(row=0, column=0, padx=40, pady=25)

latitude_Entry = tk.Entry(windows, width=30, font=project_font)
latitude_Entry.grid(row=0, column=1)

longitude_text = tk.Label(windows, text="Enter Longitude: ", font=project_font)
longitude_text.grid(row=1, column=0, padx=40, pady=25)

longitude_Entry = tk.Entry(windows, width=30, font=project_font)
longitude_Entry.grid(row=1, column=1)

find_button = tk.Button(windows, text="Find Location", font=project_font, command=change_adress)
find_button.grid(row=2, column=0, columnspan=2, pady=25)

adress_label = tk.Label(windows, text="", font=project_font, wraplength=500, justify="left")
adress_label.grid(row=3, column=0,columnspan=2 ,sticky="w", padx=50, pady=10)

windows.mainloop()
