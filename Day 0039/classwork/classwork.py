# N1
# Complete the method/function so that 
# it converts dash/underscore delimited 
# words into camel casing. The first 
# word within the output should be 
# capitalized only if the original 
# word was capitalized (known as 
# Upper Camel Case, also often 
# referred to as Pascal case). 
# The next words should be 
# always capitalized.

def to_camel_case(text):
    if text == "":
        return ""
    text = text.replace("-", "_")
    new_text = text.split("_")
    result = ""
    if text[0].isupper():
        for i in new_text:
            result += i.capitalize()
    else:
        result += new_text[0]
        for index in range(1, len(new_text)):
            result += new_text[index].capitalize()
            
    return result


# N2
# Given an array of integers, 
# find the one that appears an odd number of times.

def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i