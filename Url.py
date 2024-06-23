import pyperclip
import pyshorteners
from tkinter import Tk, Entry, Label, StringVar,Button 

root = Tk()
root.geometry("450x250")
root.title("Urls Shortener")
root.configure(bg="Light Blue")
url = StringVar()
url_address = StringVar()

def urlshortener():
    urladdress= url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(root, text="Url Shortener", font="Times 16").pack(pady=9)
Entry(root, textvariable=url, font="Times 14").pack(pady=14)
Button(root, text="Generate the Short Url",command=urlshortener, font="Times 14").pack(pady=9)
Entry(root, textvariable=url_address,font="Times 14").pack(pady=9)
Button(root, text="Copy the Url", command=copyurl, font="Times 12").pack(pady=7)

root.mainloop()


