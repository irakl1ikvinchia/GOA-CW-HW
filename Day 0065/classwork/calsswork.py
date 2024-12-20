# N1
# Write a function that takes a string of braces, 
# and determines if the order of the braces is valid. 
# It should return true if the string is valid, 
# and false if it's invalid.

def valid_braces(s):
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "")
        s = s.replace("[]", "")
        s = s.replace("{}", "")
    return s == ""


# N2
# In this kata you are required to, given a string, 
# replace every letter with its position in the alphabet.

def alphabet_position(text):
    result = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for i in text.lower():
        if i.isalpha():
            index = alphabet.index(i) + 1
            result.append(str(index))
            
    return " ".join(result)