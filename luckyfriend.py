# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:51:57 2024

@author: mcode
"""

from tkinter import Tk, Label, Button, Frame, LEFT, RIGHT, TOP, X, Entry
from random import choice

# Global Variables
friends = []

# Window
window = Tk()
window.title('Lucky Friend')
window.geometry('400x400')

# Title
titleFrame = Frame(border=5, bg='black')
title = Label(
    titleFrame,
    text="Welcome to Luchy Friend",
    bg = 'black',
    fg = 'white',
    font=("Arial", 15)
)
title.pack(side=LEFT)
exitB=Button(titleFrame, text='X', bg='black', fg='white', font=("Arial", 15), command=window.destroy).pack(side=RIGHT)
titleFrame.pack(fill=X, side=TOP)

# Items Display

display=Label(text='Posible Friends: ', wraplength=300)

# Input
inputF=Frame(border=5)
Label(inputF, text='Freind Name: ').pack(side=LEFT)
friendName=Entry(inputF, width=15)
friendName.pack(side=LEFT)
def getFriends():
    string = ''
    for friend in friends:
        string = f'{string}{friend}, '
    display['text']=f'Posible Friends: {string}'
def submit():
    friends.append(friendName.get())
    getFriends()
Button(inputF, text='Add Friend', command=submit).pack(side=LEFT, padx=(5,0))
inputF.pack(side=TOP, fill=X)
display.pack(side=TOP)

# Output
output = Label(text="Lucky Friend: ")
def selectFriend():
    try:
        friend = choice(friends)
        output['text']=f'Lucky Friend: {friend}'
        friends.remove(friend)
        getFriends()
    except IndexError:
        output['text']='No Friends Left!'
Button(text='Select Friend', command=selectFriend).pack(side=TOP)
output.pack(side=TOP)

# Window.mainloop and Pack
window.mainloop()
