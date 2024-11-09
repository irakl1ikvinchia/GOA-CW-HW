# N1
# Write a function to convert a name into initials. 
# This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.

def abbrev_name(name):
    name = name.upper()
    splited_name = name.split(" ")
    firstname = splited_name[0]
    lastname = splited_name[1]
    result = firstname[0] + "." + lastname[0]
    
    return result


# N2
# Given an array of integers, return a new array with each value doubled.

def maps(a):
    doubled_numbers = []
    
    for i in a:
        doubled_numbers.append(i * 2)
        
    return doubled_numbers


# N3
# Write a function which converts the input string to uppercase.

def make_upper_case(s):
    s = s.upper()
    return s