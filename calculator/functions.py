# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 17:53:16 2024

@author: mcode
"""
import math

def roundToFive(value):
  formatted_string = f"{value:.5f}"
  return float(formatted_string)
def addition(n1,n2):
    try:
        resultN = float(n1.get()) + float(n2.get())
        returnValue = [f'\n{n1.get()} + {n2.get()} = {str(resultN)}', resultN]
        return returnValue
    except ValueError:
        return ['\n Error: This is Addition! Do It Yourself!', n1.get()]
    
def subtraction(n1,n2):
    try:
        resultN = float(n1.get()) - float(n2.get())
        returnValue = [f'\n{n1.get()} - {n2.get()} = {str(resultN)}', resultN]
        return returnValue
    except ValueError:
        return ['\n Error: You get an F for breaking subtraction, how do you even break subtraction!', n1.get()]
    
def multiplication(n1,n2):
    try:
        resultN = float(n1.get()) * float(n2.get())
        returnValue = [f'\n{n1.get()} X {n2.get()} = {str(resultN)}', resultN]
        return returnValue
    except ValueError:
        return ['\n Error: Are you multipliing "Me" X "You"!', n1.get()]
    
def division(n1,n2):
    try:
        resultN = float(n1.get()) / float(n2.get())
        returnValue = [f'\n{n1.get()} / {n2.get()} = {str(resultN)}', resultN]
        return returnValue
    except ValueError:
        return ['\n Error: Try dividing "this" by "that" and then use numbers, with no letters!', n1.get()]
    except ZeroDivisionError:
        return ['\nError: Uh oh, dividing by zero is like trying to use the Force on an empty fridge. It just doesn\'t work! May the odds be ever in your favor for future calculations.']

def exponent(n1,n2):
    try:
        resultN = float(n1.get()) ** float(n2.get())
        returnValue = [f'\n{n1.get()} ^ {n2.get()} = {str(resultN)}', resultN]
        return returnValue
    except ValueError:
        return ['\n Error: What did you put in? Tell Me NOW!', n1.get()]
    except OverflowError:
        return ['\nError: Whoa there, seems your numbers are bigger than the universe can handle! Try using smaller numbers or a more powerful calculator (like the one in your head, not me).', n1.get()]
    
def rooting(n1,n2):
    try:
        resultN = float(n1.get()) ** (1/float(n2.get()))
        returnValue = [f'\n{n1.get()} ^ (1/{n2.get()}) = {str(resultN)}', resultN]
        return returnValue
    except ValueError:
        return ['\n Error: Are you (root)ing for somone?!', n1.get()]
    
def sine(n1, n2, inverse):
    try:
        if inverse.get():
            resultN = roundToFive(math.asin(float(n1.get())))
            return [f'\nsin-1({n1.get()}) = {resultN}',resultN]
        else:
            resultN = roundToFive(math.sin(float(n1.get())))
            return [f'\nsin({n1.get()}) = {resultN}',resultN]
    except ValueError:
        return ['\n Error: Seriusely, sine-1 only accepts numbers between -1, and 1! Oh, and if your using sine, ITS RADIANS', n1.get()]
    
def cosine(n1, n2, inverse):
    try:
        if inverse.get():
            resultN = roundToFive(math.acos(float(n1.get())))
            return [f'\ncos-1({n1.get()}) = {resultN}',resultN]
        else:
            resultN = roundToFive(math.cos(float(n1.get())))
            return [f'\ncos({n1.get()}) = {resultN}',resultN]
    except ValueError:
        return ['\n Error: What do you even use cosine for, its like a messed up sine!', n1.get()]

def tangent(n1, n2, inverse):
    try:
        if inverse.get():
            resultN = roundToFive(math.atan(float(n1.get())))
            return [f'\ntan-1({n1.get()}) = {resultN}',resultN]
        else:
            resultN = roundToFive(math.cos(float(n1.get())))
            return [f'\ntan({n1.get()}) = {resultN}',resultN]
    except ValueError:
        return ['\n Error: Are you even triing to get the tangent of a number?!', n1.get()]
    
def logarithem(n1,n2,inverse):
    try:
        if inverse.get():
            if n2.get():
                resultN = roundToFive(10**float(n1.get()))
                return [ f'\nlog-1({n1.get()}) = {str(resultN)}', resultN]
            else:
                resultN = roundToFive(math.exp(float(n1.get())))
                return [ f'\nln-1({n1.get()}) = {str(resultN)}', resultN]
        else:
            if n2.get():
                resultN = roundToFive(math.log10(float(n1.get())))
                return [ f'\nlog({n1.get()}) = {str(resultN)}', resultN]
            else:
                resultN = roundToFive(math.log(float(n1.get())))
                return [ f'\nln({n1.get()}) = {str(resultN)}', resultN]
    except ValueError:
        return ['\n Error: Are you triing to be funny here?!', n1.get()]
    except OverflowError:
        return ['\n Error: Uh oh, your numbers are bigger than even the biggest piggy bank can handle! Try using smaller numbers or switching to a bigger bank (like a vault).?!', n1.get()]
