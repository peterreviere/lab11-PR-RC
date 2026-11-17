"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a
def logarithm(a, b):
    if a == 0:
        raise ValueError
    else:
        return math.log(b, a)

def exponent(a, b):
    return a ** b

def hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 1/2

def square_root(a):
    if a > 0:
        return a ** (1/2)
    else:
        raise ValueError

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a
def log(a, b):
    if a == 0:
        raise ValueError
    else:
        return math.log(b, a)

def exp(a, b):
    return a ** b