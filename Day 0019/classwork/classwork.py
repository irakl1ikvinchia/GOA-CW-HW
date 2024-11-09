# N1
# Given an array of integers your solution should find the smallest integer.

def find_smallest_int(arr):
    return min(arr)


# N2
# Write a function that removes the spaces from the string, 
# then return the resultant string.

def no_space(x):
    y = x.replace(" ", "")
    return y


# N3
# Implement a function which convert the given 
# boolean value into its string representation.
# Note: Only valid inputs will be given.

def boolean_to_string(b):
    b = str(b)
    return b


# N4
# Write a function that takes an array of numbers and 
# returns the sum of the numbers. The numbers can be 
# negative or non-integer. If the array does not 
# contain any numbers then you should return 0.

def sum_array(a):
    return sum(a)