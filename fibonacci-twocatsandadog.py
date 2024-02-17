# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 08:01:38 2024

@author: mcode
"""

from tkinter import *
window = Tk()
window.title("Fibonacci (Two Cats and an Ice Cream)")
window.geometry("400x600")

# Title
title = Label(
    text="Fibonacci Series Generator",
    bg = 'blue',
    fg = 'orange'
)
title.configure(font=("Arial", 24))
title.pack(fill=X)

# Entry and Its Label and its Frame
row1 = Frame(border=10)
Label(
      master=row1,
      text = 'Numbers To Generate: ',
      font=('Ariel', 14),
      border=5
).pack(side=LEFT)
toFind = Entry(master=row1)
toFind.pack(side=LEFT, fill=X)
row1.pack(side=TOP)
# Results
row2 = Frame(border=10)
Label(row2,text='Fibonacci Series: ',font=('Ariel', 12, 'bold')).pack(side=LEFT)
result = Label(row2, font=('Ariel', 10), wraplength=300)
result.pack(side=LEFT, fill=X)
row2.pack(side=TOP)

# Button and Function
class overLoad(Exception):
    pass

def generate():
    try:
        # Validate input and raise custom exception for clarity
        total = float(toFind.get())
        if total > 50:
            raise overLoad("Number too large (maximum 50)")

        # Initialize nums efficiently using list comprehension
        nums = [0, 1]

        # Calculate Fibonacci sequence using explicit and clear iteration
        for _ in range(2, int(total - 3) + 1):
            next_num = nums[-1] + nums[-2]
            nums.append(next_num)

        # Set result text, considering feedback on formatting
        result['text'] = nums

    except ValueError:
        result['text'] = "Invalid input: Please enter a positive number."
    except overLoad as e:
        result['text'] = f"Error: {e}"
    except Exception as e:
        result['text'] = f"An unexpected error occurred: {e}"
Button(text='Generate', command=generate).pack(side=BOTTOM)
    

# Main Loop
window.mainloop()