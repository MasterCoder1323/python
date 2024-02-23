# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 07:13:51 2024

@author: mcode
"""

# Imports
from tkinter import *

# Window
window = Tk()
window.title("Accii Encrypter")
window.geometry("300x400")

# Title
titleFrame = Frame(border=5, bg='black')
title = Label(
    titleFrame,
    text="Welcome to Accii encrypter",
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
encryptedText = Text(font=('Ariel', 10, 'bold'), width=40, height=1)
def convert():
    inputVal = inputText.get()
    accii = []
    encrypted = ''
    output1 = ''
    for letter in inputVal:
        accii.append(ord(letter))
        output1 = str(accii)
    for num in accii:
        encrypted = f'{encrypted}{chr(num-13)}'
    outputText["text"] = output1
    encryptedText.delete('1.0',END)
    encryptedText.insert('1.0',encrypted)
def decrypt():
    inputVal = inputText.get()
    accii = []
    encrypted = ''
    output1 = ''
    for letter in inputVal:
        accii.append(ord(letter))
        output1 = str(accii)
    for num in accii:
        encrypted = f'{encrypted}{chr(num+13)}'
    outputText["text"] = output1
    encryptedText.delete('1.0',END)
    encryptedText.insert('1.0',encrypted)
Button(text='Encrypt', bg='yellow', command=convert).place(relx=0.4, rely=0.5, anchor=CENTER)
Button(text='Decrypt', bg='yellow', command=decrypt).place(relx=0.6, rely=0.5, anchor=CENTER)
outputText.place(relx=0.5, rely=0.6, anchor=CENTER)
encryptedText.place(relx=0.5, rely=0.7, anchor=CENTER)
# Main Loop
window.mainloop()
