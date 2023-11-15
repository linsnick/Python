from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Restaurant Finder")
root.geometry("400x400")

def areacodeLookup():
    acode.get()
    acodeLabel = Label(root, text = acode.get())
    acodeLabel.grid(row = 1, column = 0, columnspan = 2)
    
    try:
        api_request = requests.get("") #insert the api reference
        api = json.loads(api_request.content)
        #Create variables to assign to api info
        location = api[0]['City']
        name = api[0]['Name']
        style = api[0]['Restaurant']['Specialty']
        myLabel = Label(root, text = name + " is a restaurant that specializes in " + style + " in " + location) #Figure out which index of the api you want to use
        myLabel.grid(row = 2, column = 0, columnspan = 2)                                                                                           #Different APIs will have different formats    

    except Exception as e:
        api = "Error..."




acode = Entry(root)
acode.grid(row = 0, column = 0)

acode_btn = Button(root, command = areacodeLookup)
acode_btn.grid(row = 0, column = 1)


root.mainloop()

