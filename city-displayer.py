from tkinter import Tk, Label, Button, Frame, LEFT, RIGHT, TOP, X, Entry
from random import choice
from extra import jstr

# Global Variables
locations = []

# Window
window = Tk()
window.title('Lucky Friend')
window.geometry('400x400')

# Title
titleFrame = Frame(border=5, bg='black')
title = Label(
    titleFrame,
    text="Welcome to City Selector",
    bg = 'black',
    fg = 'white',
    font=("Arial", 15)
)
title.pack(side=LEFT)
exitB=Button(titleFrame, text='X', bg='black', fg='white', font=("Arial", 15), command=window.destroy).pack(side=RIGHT)
titleFrame.pack(fill=X, side=TOP)


# Display
display=Label(text='Countries & Cities: ', wraplength=300)
def dispayLocations():
    string = ''
    for location in locations:
        string += jstr(location)
    display['text']=f'Countries & Cities:\n\n{string}'


# Input
inputF=Frame(border=5)
Label(inputF, text='Country: ').pack(side=LEFT)
country=Entry(inputF, width=15)
country.pack(side=LEFT)
city=Entry(inputF, width=15)
city.pack(side=RIGHT)
Label(inputF, text='City: ').pack(side=RIGHT)
inputF.pack(side=TOP, fill=X)
def submit():
    print('Submiting')
    locations.append({f'{country.get()}': city.get()})
    for location in locations:
        print(jstr(location))
    dispayLocations()
Button(window, text='Submit', command=submit).pack(side=TOP, padx=(5,0))
display.pack(side=TOP)

# Random Selector
result=Label(wraplength=300)
def select():
    result['text']=jstr(choice(locations))
Button(window, text='Select Random Location', command=select).pack(side=TOP)
result.pack(side=TOP)

# Window.mainloop and Pack
window.mainloop()
