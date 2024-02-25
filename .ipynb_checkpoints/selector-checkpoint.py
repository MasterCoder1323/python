# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:51:57 2024

@author: mcode
"""

from tkinter import Tk, Label, Button, Frame, LEFT, RIGHT, TOP, X, Entry
from random import choice

# Global Variables
items = []

# Window
window = Tk()
window.title('Item Selector')
window.geometry('400x400')

# Title
titleFrame = Frame(border=5, bg='black')
title = Label(
    titleFrame,
    text="Welcome to Item Selector",
    bg = 'black',
    fg = 'white',
    font=("Arial", 15)
)
title.pack(side=LEFT)
exitB=Button(titleFrame, text='X', bg='black', fg='white', font=("Arial", 15), command=window.destroy).pack(side=RIGHT)
titleFrame.pack(fill=X, side=TOP)

# Items Display

display=Label(text='Unpacked Items: ', wraplength=300)

# Input
inputF=Frame(border=5)
Label(inputF, text='Item To Add: ').pack(side=LEFT)
itemName=Entry(inputF, width=15)
itemName.pack(side=LEFT)
def getItems():
    string = ''
    for item in items:
        string = f'{string}{item}, '
    display['text']=f'Unpacked Items: {string}'
def submit():
    items.append(itemName.get())
    getItems()
Button(inputF, text='Add To Items', command=submit).pack(side=LEFT, padx=(5,0))
inputF.pack(side=TOP, fill=X)
display.pack(side=TOP)

# Output
output = Label(text="Pack: ")
def packItem():
    try:
        item = choice(items)
        output['text']=f'Pack: {item}'
        items.remove(item)
        getItems()
    except IndexError:
        output['text']='All Done!'
Button(text='Pack Item', command=packItem).pack(side=TOP)
output.pack(side=TOP)

# Window.mainloop and Pack
window.mainloop()
