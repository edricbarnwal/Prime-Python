from tkinter import *
import pyshorteners

def Shorten_URL():
    short = pyshorteners.Shortener()
    User_Link = URL_Entry.get()
    Short_URL = short.tinyurl.short(User_Link)
    Short_URL_Label.configure(text=Short_URL)

def copy_to_clipboard():
    Copy_URL = Short_URL_Label.cget("text")
    window.clipboard_clear()
    window.clipboard_append(Copy_URL)
    window.update()

window = Tk()
window.title("URL Shortner")
window.geometry("500x400")

Enter_Text = Label(text="Enter Your URL", font=("arial", 20))
Enter_Text.pack(pady=20)

URL_Entry = Entry(font=("arial", 20))
URL_Entry.pack()

Shorten_Button = Button(text="Shorten URL", font=("arial", 18), command=Shorten_URL)
Shorten_Button.pack(pady=20)

Short_URL_Label = Label(text="", font=("arial", 20))
Short_URL_Label.pack(pady=20)

Copy_Button = Button(text="Copy to Clipboard", font=("arial", 16), command=copy_to_clipboard)
Copy_Button.pack()

window.mainloop()
