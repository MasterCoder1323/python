# -*- coding: utf-8 -*-
"""
@author: mcode
"""

from tkinter import *
# Make Window
window = Tk()
window.title("MC1323 Calculator V1.0.2")
window.geometry("400x500")
# Title
title = Label(
    text="Welcome to MC1323 Calculator",
    bg = 'black',
    fg = 'white'
)
title.configure(font=("Arial", 15))
title.pack(fill=X)
# Num Entry In Its Frame
numFrame = Frame(height=50)
num1 = Entry(
    width = 15,
    master=numFrame
)
num2 = Entry(
    width = 15,
    master=numFrame
)
Label(
    text='First Number:',
    master=numFrame
).pack(side=LEFT)
num1.pack(side=LEFT)
num2.pack(side=RIGHT)
Label(
    text='Second Number:',
    master=numFrame
).pack(side=RIGHT)
numFrame.pack(fill=X)

# Result
result = Text(wrap=WORD)

# Buttons & Their Functions & Their Frame
btnFrame = Frame(borderwidth=10)
def add():
    try:
        n1=float(num1.get())
        n2=float(num2.get())
        resultN=n1+n2
        result.insert(END, f'\n{n1} + {n2} = {str(resultN)}')
        result.see(END)
    except ValueError:
        result.insert(END, '\nError: Invalid input detected!')
addButton = Button(
    master=btnFrame,
    text='Add',
    command=add
).pack(side=LEFT, expand=True)
def subtract():
    try:
        n1=float(num1.get())
        n2=float(num2.get())
        resultN=n1-n2
        result.insert(END,  f'\n{n1} - {n2} = {str(resultN)}')
        result.see(END)
    except ValueError:
        result.insert(END, '\nError: Invalid input detected!')
subtractButton = Button(
    master=btnFrame,
    text='Subtract',
    command=subtract
).pack(side=LEFT, expand=True)
def multiply():
    try:
        n1=float(num1.get())
        n2=float(num2.get())
        resultN=n1*n2
        result.insert(END,  f'\n{n1} X {n2} = {str(resultN)}')
        result.see(END)
    except ValueError:
        result.insert(END, '\nError: Invalid input detected!')
multiplicationButton = Button(
    master=btnFrame,
    text='Multiply',
    command=multiply
).pack(side=LEFT, expand=True)
def divide():
    try:
        n1 = float(num1.get())
        n2 = float(num2.get())
        resultN = n1 / n2
        result.insert(END, f'\n{n1}/{n2} = {str(resultN)}')
        result.see(END)
    except ZeroDivisionError:
        result.insert(END, f'\nError: Division by zero!')
    except ValueError:
        result.insert(END, '\nError: Invalid input detected!')
divideButton = Button(
    master=btnFrame,
    text='Divide',
    command=divide
).pack(side=LEFT, expand=True)
def power():
    try:
        n1=float(num1.get())
        n2=float(num2.get())
        resultN=n1**n2
        result.insert(END,  f'\n{n1} ^ {n2} = {str(resultN)}')
        result.see(END)
    except ValueError:
        result.insert(END, '\nError: Invalid input detected!')
    except OverflowError:
        result.insert(END, '\nError: Numbers too big!')
powerButton = Button(
    master=btnFrame,
    text='Exponent',
    command=power
).pack(side=LEFT, expand=True)
def root():
    try:
        n1=float(num1.get())
        n2=float(num2.get())
        resultN=n1**(1/n2)
        result.insert(END,  f'\n{n1} ^ (1/{n2}) = {str(resultN)}')
        result.see(END)
    except ValueError:
        result.insert(END, '\nError: Invalid input detected!')
rootButton = Button(
    master=btnFrame,
    text='Root',
    command=root
).pack(side=LEFT, expand=True)
btnFrame.pack(side=TOP, fill=X)
result.pack(fill=X, side=TOP)
window.mainloop()
