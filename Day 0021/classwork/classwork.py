# N1
# Given a non-empty array of integers, 
# return the result of multiplying the 
# values together in order. Example:

def grow(arr):
    result = 1
    
    for num in arr:
        result *= num
        
    return result


# N2
# Write function bmi that calculates 
# body mass index (bmi = weight / height2).

def bmi(weight, height):
    res = height * height
    bmi = weight / res
    
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    elif bmi > 30:
        return "Obese"


# N3
# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    result = 0
    
    for i in sentence:
        if i == "a":
            result += 1
        elif i == "e":
            result += 1
        elif i == "i":
            result += 1
        elif i == "o":
            result += 1
        elif i == "u":
            result += 1
    return result