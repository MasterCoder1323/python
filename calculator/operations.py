# -*- coding: utf-8 -*-
"""
@version: 1.0.1
@author: mastercoder1323
@desc: This holds the operations for the main.py.
"""
# Import Math Module 
import math


def roundToFive(value):
    """Rounds a given number to 5 decimal places.

    Args:
        value: The number to be rounded.

    Returns:
        float: The rounded number with 5 decimal places.
    """
    formatted_string = f"{value:.5f}"
    return float(formatted_string)


def addition(n1,n2):
    """Adds two numbers together.

    Args:
        n1: A tkinter Entry widget which holds the first number.
        n2: A tkinter Entry widget which holds the second number.

    Returns:
        list: A list containing:
            - A string formatted as "n1 + n2 = result", where result is the sum.
            - The numerical value of the sum.

    Raises:
        ValueError: If either n1 or n2 cannot be converted to a float.
    """
    try:
        resultN = float(n1.get()) + float(n2.get())
        returnValue = [f'\n{n1.get()} + {n2.get()} = {str(resultN)}', resultN]
        return returnValue
    except ValueError:
        return ['\n Error: This is Addition! Do It Yourself!', n1.get()]
   
    
def subtraction(n1,n2):
    """Subtracts one number from another.

    Args:
        n1: A tkinter Entry widget which holds the first number.
        n2: A tkinter Entry widget which holds the second number.

    Returns:
        list: A list containing:
            - A string formatted as "n1 - n2 = result", where result is the 
            differance.
            - The numerical value of the differance.

    Raises:
        ValueError: If either n1 or n2 cannot be converted to a float.
    """
    try:
        resultN = float(n1.get()) - float(n2.get())
        returnValue = [f'\n{n1.get()} - {n2.get()} = {str(resultN)}', resultN]
        return returnValue
    except ValueError:
        return ['\n Error: You get an F for breaking subtraction, how do you even break subtraction!', n1.get()]
  
    
def multiplication(n1,n2):
    """Multiplies two numbers together.

    Args:
        n1: A tkinter Entry widget which holds the first number.
        n2: A tkinter Entry widget which holds the second number.

    Returns:
        list: A list containing:
            - A string formatted as "n1 X n2 = result", where result is the 
            product.
            - The numerical value of the differance.

    Raises:
        ValueError: If either n1 or n2 cannot be converted to a float.
    """
    try:
        resultN = float(n1.get()) * float(n2.get())
        returnValue = [f'\n{n1.get()} X {n2.get()} = {str(resultN)}', resultN]
        return returnValue
    except ValueError:
        return ['\n Error: Are you multipliing "Me" X "You"!', n1.get()]
  
    
def division(n1,n2):
    """Divides two numbers.

    Args:
        n1: A tkinter Entry widget which holds the first number.
        n2: A tkinter Entry widget which holds the second number.

    Returns:
        list: A list containing:
            - A string formatted as "n1 / n2 = result", where result is the 
            quotient.
            - The numerical value of the quotient.

    Raises:
        ValueError: If either n1 or n2 cannot be converted to a float.
        ZeroDivsionError: If the numerical value of n2 is equal to 0.
    """
    try:
        resultN = float(n1.get()) / float(n2.get())
        returnValue = [f'\n{n1.get()} / {n2.get()} = {str(resultN)}', resultN]
        return returnValue
    except ValueError:
        return ['\n Error: Try dividing "this" by "that" and then use numbers, with no letters!', n1.get()]
    except ZeroDivisionError:
        return ['\nError: Uh oh, dividing by zero is like trying to use the Force on an empty fridge. It just doesn\'t work! May the odds be ever in your favor for future calculations.']


def exponent(n1,n2):
    """Number 1 to the power of number 2.

    Args:
        n1: A tkinter Entry widget which holds the first number.
        n2: A tkinter Entry widget which holds the second number.

    Returns:
        list: A list containing:
            - A string formatted as "n1 ^ n2 = result", where result is 
            n1 ^ n2.
            - The numerical value of the differance.

    Raises:
        ValueError: If either n1 or n2 cannot be converted to a float.
        OverFlowError: If the answer is too large to calculate.
    """
    try:
        resultN = float(n1.get()) ** float(n2.get())
        returnValue = [f'\n{n1.get()} ^ {n2.get()} = {str(resultN)}', resultN]
        return returnValue
    except ValueError:
        return ['\n Error: What did you put in? Tell Me NOW!', n1.get()]
    except OverflowError:
        return ['\nError: Whoa there, seems your numbers are bigger than the universe can handle! Try using smaller numbers or a more powerful calculator (like the one in your head, not me).', n1.get()]
  
    
def rooting(n1,n2):
    """The root of n1.

    Args:
        n1: A tkinter Entry widget which holds the first number.
        n2: A tkinter Entry widget which holds the second number.

    Returns:
        list: A list containing:
            - A string formatted as "n1 X (1/n2) = result", where result is the
            root of the first number.
            - The numerical value of the differance.

    Raises:
        ValueError: If either n1 or n2 cannot be converted to a float.
    """
    try:
        resultN = float(n1.get()) ** (1/float(n2.get()))
        returnValue = [f'\n{n1.get()} ^ (1/{n2.get()}) = {str(resultN)}', resultN]
        return returnValue
    except ValueError:
        return ['\n Error: Are you (root)ing for somone?!', n1.get()]
  
    
def sine(n1, n2, inverse):
    """Calculates the sine or inverse sine of a number.

    Args:
        n1: The number for which to calculate the sine or inverse sine.
        n2: Not used for this function, but included for consistency with other
        function calls.
        inverse: A boolean indicating whether to calculate the inverse sine 
        (arcsine).

    Returns:
        list: A list containing:
            - A string formatted as "sin(n1) = result" or "sin-1(n1) = result".
            - The numerical value of the sine or inverse sine.

    Raises:
        ValueError: If n1 is outside the valid range for inverse sine (-1 to 1).
    """
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
    """Calculates the cosine or inverse cosine of a number.

    Args:
        n1: The number for which to calculate the cosine or inverse cosine.
        n2: Not used for this function, but included for consistency with other
        function calls.
        inverse: A boolean indicating whether to calculate the inverse cosine 
        (arccosine).

    Returns:
        list: A list containing:
            - A string formatted as "cosin(n1) = result" or 
            "cosin-1(n1) = result".
            - The numerical value of the cosine or inverse cosine.

    Raises:
        ValueError: If n1 is outside the valid range for inverse cosine (-1 to 1).
    """

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
    """Calculates the tangent or inverse tangent of a number.

    Args:
        n1: The number for which to calculate the tangent or inverse tangent.
        n2: Not used for this function, but included for consistency with other
        function calls.
        inverse: A boolean indicating whether to calculate the inverse tangent.

    Returns:
        list: A list containing:
            - A string formatted as "tangent(n1) = result" or 
            "tangent-1(n1) = result".
            - The numerical value of the tangent or inverse sine.

    Raises:
        ValueError: If n1 is outside the valid range for inverse tangent.
    """

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
    """Calculates the logarithm or antilogarithm of a number.

    Args:
        n1: The number for which to calculate the logarithm or antilogarithm.
        n2: The base of the logarithm (optional, defaults to 10).
        inverse: A boolean indicating whether to calculate the antilogarithm 
        (exponential function).

    Returns:
        list: A list containing:
            - A string formatted with the appropriate notation for the calculation.
            - The numerical value of the logarithm or antilogarithm.

    Raises:
        ValueError: If n1 is less than or equal to zero for non-exponential 
        calculations.
        OverflowError: If the calculation results in a number too large to 
        represent.
    """
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


def FtoC(n1,n2,inverse):
    """Converts a temperature between Fahrenheit and Celsius.

    Args:
        n1: The temperature value to convert.
        n2: Not used for this function, but included for consistency with other function calls.
        inverse: A boolean indicating whether to convert from Fahrenheit to Celsius (True) or vice versa (False).

    Returns:
        list: A list containing:
            - A string formatted as "toC(n1°F) = result°C" or "toF(n1°C) = result°F".
            - The numerical value of the converted temperature.

    Raises:
        ValueError: If n1 cannot be converted to a float.
        OverflowError: If the calculation results in a number too large to represent.
    """
    try:
        temp = float(n1.get())
        if inverse.get():
            resultN = (temp * 9 / 5) + 32
            return [ f'\ntoF({n1.get()}°C) = {str(resultN)}', resultN]
        else:
           resultN = (temp - 32) * 5 / 9 
           return [ f'\ntoC({n1.get()}°F) = {str(resultN)}', resultN]
    except ValueError:
        return ['\n Error: Try Putting in a number in inches!', n1.get()]
    except OverflowError:
        return ['\n Error: Uh oh, your numbers are bigger than even the biggest piggy bank can handle! Try using smaller numbers or switching to a bigger bank (like a vault).?!', n1.get()]
