# Import Tkinter
from tkinter import *

# Define Variables
info = {
    "name": "Jacob Spar",
    "id": "302903910",
    "DOB": "January 15, 2002",
    "pin": "230927",
    "address": "557 Applegate Street, Saint-Prime, QC G8J 1C1",
    "atdfv": "Two, Four, Infinity, None, Five Hundered"
}

# Define Window
window = Tk()
window.title("Drivers License")
window.geometry("500x300")

# Title
title = Label(
    text="Driving License",
    bg = 'red',
    fg = 'white'
)
title.configure(font=("Times", 24, 'bold italic'))
title.pack(fill=X)

# ID
idFrame = Frame(border=10)
idLabel = Label(
    idFrame,
    text="ID: ",
)
idLabel.configure(font=("Ariel", 14, 'bold'))
idLabel.pack(side=LEFT)
idText = Label(
    idFrame,
    text="",
)
idText.configure(font=("Ariel", 14))
idText.pack(side=LEFT)
idFrame.pack(fill=X, side=TOP)

# Name
nameFrame = Frame(border=1)
nameLabel = Label(
    nameFrame,
    text="Name: ",
)
nameLabel.configure(font=("Ariel", 12, 'bold'))
nameLabel.pack(side=LEFT)
nameText = Label(
    nameFrame,
    text="",
)
nameText.configure(font=("Ariel", 12))
nameText.pack(side=LEFT)
nameFrame.pack(fill=X, side=TOP)

# Date Of Birth
DOBFrame = Frame(border=1)
DOBLabel = Label(
    DOBFrame,
    text="Date Of Birth: ",
)
DOBLabel.configure(font=("Ariel", 12, 'bold'))
DOBLabel.pack(side=LEFT)
DOBText = Label(
    DOBFrame,
    text="",
)
DOBText.configure(font=("Ariel", 12))
DOBText.pack(side=LEFT)
DOBFrame.pack(fill=X, side=TOP)

# Pin No.
pinFrame = Frame(border=1)
pinLabel = Label(
    pinFrame,
    text="Pin Number: ",
)
pinLabel.configure(font=("Ariel", 12, 'bold'))
pinLabel.pack(side=LEFT)
pinText = Label(
    pinFrame,
    text="",
)
pinText.configure(font=("Ariel", 12))
pinText.pack(side=LEFT)
pinFrame.pack(fill=X, side=TOP)

# Address.
addressFrame = Frame(border=1)
addressLabel = Label(
    addressFrame,
    text="Address: ",
)
addressLabel.configure(font=("Ariel", 12, 'bold'))
addressLabel.pack(side=LEFT)
addressText = Label(
    addressFrame,
    text="",
)
addressText.configure(font=("Ariel", 12))
addressText.pack(side=LEFT)
addressFrame.pack(fill=X, side=TOP)

# adtfv.
adtfvFrame = Frame(border=1)
adtfvLabel = Label(
    adtfvFrame,
    text="Authorization to drive the following vehicles: ",
)
adtfvLabel.configure(font=("Ariel", 12, 'bold'))
adtfvLabel.pack(side=LEFT)
adtfvText = Label(
    adtfvFrame,
    text="",
    wraplength=100,
    anchor="nw", 
    font=("Ariel", 12)
)
adtfvText.configure(font=("Ariel", 12))
adtfvText.pack(side=LEFT)
adtfvFrame.pack(fill=X, side=TOP)

# Button
def showInfo():
    idText["text"] = info["id"]
    nameText["text"] = info["name"]
    DOBText["text"] = info["DOB"]
    pinText["text"] = info["pin"]
    addressText["text"] = info["address"]
    adtfvText["text"] = info["atdfv"]
    showInfoButton.configure(command=hideInfo, text="Hide Info")
def hideInfo():
    idText["text"] = ""
    nameText["text"] = ""
    DOBText["text"] = ""
    pinText["text"] = ""
    addressText["text"] = ""
    adtfvText["text"] = ""
    showInfoButton.configure(command=showInfo, text="Show Info")
showInfoButton = Button(window,text="Show Info", command=showInfo)
showInfoButton.pack(side=BOTTOM)

# Pack and Main Loop
window.mainloop()