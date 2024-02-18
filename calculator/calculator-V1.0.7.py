# -*- coding: utf-8 -*-
"""
@author: mcode
"""

from tkinter import *
# Make Window
window = Tk()
window.title("MC1323 Calculator V1.0.7")
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

# Options
options = Frame()
Label(options,text='Options:', font=('Ariel', 12, 'bold')).pack(side=TOP)
accumulate = IntVar()
checkbox1 = Checkbutton(
    options,
    text="Accumulate",  # Label displayed near the checkbox
    variable=accumulate,  # Link the checkbox to the variable
    onvalue=1,  # Set value to 1 when checked
    offvalue=0,  # Set value to 0 when unchecked
)
checkbox1.pack(side=LEFT)

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
        if accumulate.get():
            num1.delete(0, END)
            num1.insert(0, resultN)
    except ValueError:
        result.insert(END, '\nError: Invalid input detected!')
        result.see(END)
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
        if accumulate.get():
            num1.delete(0, END)
            num1.insert(0, resultN)
    except ValueError:
        result.insert(END, '\nError: Invalid input detected!')
        result.see(END)
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
        if accumulate.get():
            num1.delete(0, END)
            num1.insert(0, resultN)
    except ValueError:
        result.insert(END, '\nError: Invalid input detected!')
        result.see(END)
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
        if accumulate.get():
            num1.delete(0, END)
            num1.insert(0, resultN)
    except ZeroDivisionError:
        result.insert(END, f'\nError: Division by zero!')
        result.see(END)
    except ValueError:
        result.insert(END, '\nError: Invalid input detected!')
        result.see(END)
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
        if accumulate.get():
            num1.delete(0, END)
            num1.insert(0, resultN)
    except ValueError:
        result.insert(END, '\nError: Invalid input detected!')
        result.see(END)
    except OverflowError:
        result.insert(END, '\nError: Numbers too big!')
        result.see(END)
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
        if accumulate.get():
            num1.delete(0, END)
            num1.insert(0, resultN)
    except ValueError:
        result.insert(END, '\nError: Invalid input detected!')
        result.see(END)
rootButton = Button(
    master=btnFrame,
    text='Root',
    command=root
).pack(side=LEFT, expand=True)
btnFrame.pack(side=TOP, fill=X)
options.pack(side = TOP)
result.pack(fill=X, side=TOP)
window.mainloop()
