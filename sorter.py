# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 07:59:14 2024

@author: mcode
"""

from tkinter import Tk, Label, Button, Frame, LEFT, RIGHT, TOP, X
from random import sample
window = Tk()
window.title('list Sorter')
window.geometry('400x400')

# Title
titleFrame = Frame(border=5, bg='black')
title = Label(
    titleFrame,
    text="Welcome to List Sorter",
    bg = 'black',
    fg = 'white',
    font=("Arial", 15)
)
title.pack(side=LEFT)
exitB=Button(titleFrame, text='X', bg='black', fg='white', font=("Arial", 15), command=window.destroy).pack(side=RIGHT)
titleFrame.pack(fill=X, side=TOP)

# Labels
original = Label()
sortedL = Label()
# Functions
def generate():
    numbers = sample(range(1,99), 75)
    print(numbers)
    original['text']=f'Original Order: {numbers}'
    numbers.sort()
    print(numbers)
    sortedL['text']=f'Sorted Order: {numbers}'
# Button
Button(text='Generate', command=generate).pack(side=TOP, pady=(5,0))

# Pack and Main Loop
original.pack(side=TOP, pady=(10,3))
sortedL.pack(side=TOP)
window.mainloop()