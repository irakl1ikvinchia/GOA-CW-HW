# N1
# This code does not execute properly. Try to figure out why.

def multiply(a, b):
    return a * b


# N2
# Create a function that takes an integer as an argument 
# and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

# N3
# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?

def number_to_string(num):
    num = str(num)
    return num


# N4
# Complete the solution so that it reverses the string passed into it

def solution(string):
    return string[::-1]


# N5
# Write a function that accepts an integer n and a string s as parameters, 
# and returns a string of s repeated exactly n times.

def repeat_str(repeat, string):
    return repeat * string