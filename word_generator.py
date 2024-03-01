from tkinter import *
from random import choice
window = Tk()
window.title("Word Gen")
window.geometry("200x200")

# Title
title = Label(
    text="Word Gen",
    bg = 'blue',
    fg = 'orange'
)
title.configure(font=("Arial", 24))
title.pack(fill=X)

# Entry and Its Label and its Frame
row1 = Frame(border=10)
Label(
      master=row1,
      text = 'Letters: ',
      font=('Ariel', 14),
      border=5
).pack(side=LEFT)
toFind = Entry(master=row1)
toFind.pack(side=LEFT, fill=X)
row1.pack(side=TOP)
# Results
row2 = Frame(border=10)
Label(row2,text='Word: ',font=('Ariel', 12, 'bold')).pack(side=LEFT)
result = Label(row2, font=('Ariel', 10), wraplength=300)
result.pack(side=LEFT, fill=X)
row2.pack(side=TOP)


def generate():
    try:
        # Validate input and raise custom exception for clarity
        total = int(toFind.get())
        letters = 'abcdefghijklmnopqrstuvwxyz'
        word = ''
        for i in range(total):
            word += choice(letters)
        result['text'] = word

    except ValueError:
        result['text'] = "Invalid input: Please enter a positive number."
    except Exception as e:
        result['text'] = f"An unexpected error occurred: {e}"
Button(text='Generate', command=generate).pack(side=BOTTOM)
    

# Main Loop
window.mainloop()