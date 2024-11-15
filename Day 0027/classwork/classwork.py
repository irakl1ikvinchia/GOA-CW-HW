# N1
# Complete the square sum function so 
# that it squares each number passed 
# into it and then sums the results together.

def square_sum(numbers):
    square = []
    sum = 0
    
    for i in numbers:
        square.append(i ** 2)
        
    for i in square:
        sum += i
        
    return sum



# N2
# We need a function that can transform 
# a string into a number. What ways of 
# achieving this do you know?

def string_to_number(s):
    s = int(s)
    return s


# N3
# Write a function which converts 
# the input string to uppercase.

def make_upper_case(s):
    s = s.upper()
    return s


# N4
# Your task is to make two functions 
# ( max and min, or maximum and minimum, 
# etc., depending on the language ) 
# that receive a list of integers as 
# input, and return the largest and 
# lowest number in that list, 
# respectively. Each function returns one number.

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)