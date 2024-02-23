# Imports
from tkinter import *

# Window
window = Tk()
window.title("Text to Accii")
window.geometry("300x400")

# Title
titleFrame = Frame(border=5, bg='black')
title = Label(
    titleFrame,
    text="Welcome to Text to Accii",
    bg = 'black',
    fg = 'white',
    font=("Arial", 15)
)
title.pack(side=LEFT)
exitB=Button(titleFrame, text='X', bg='black', fg='white', font=("Arial", 15), command=window.destroy).pack(side=RIGHT)
titleFrame.pack(fill=X, side=TOP)

# Input
Label(text='Input Text:').place(relx=0.5, rely=0.3, anchor=CENTER)
inputText=Entry(width=20)
inputText.place(relx=0.5, rely=0.4, anchor=CENTER)

# Button Function And Output
outputText = Label(text='', font=('Ariel', 10, 'bold'), wraplength=200)
def convert():
    inputVal = inputText.get()
    output = ''
    for letter in inputVal:
        output += str(ord(letter)) + ', '
    outputText["text"] = output
Button(text='Convert', bg='yellow', command=convert).place(relx=0.5, rely=0.5, anchor=CENTER)
outputText.place(relx=0.5, rely=0.6, anchor=CENTER)
# Main Loop
window.mainloop()
