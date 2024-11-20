# N1
# Write a method 
# (or function, depending on the language) 
# that converts a string to camelCase, 
# that is, all words must have their 
# first letter capitalized and spaces 
# must be removed.

def camel_case(s):
    result = []
    s = s.split(" ")
    
    for i in s:
        result.append(i.capitalize())
    return "".join(result)


# N2
# ATM machines allow 4 or 6 digit 
# PIN codes and PIN codes cannot 
# contain anything but exactly 4 
# digits or exactly 6 digits.
# If the function is passed a 
# valid PIN string, return true, 
# else return false.

def validate_pin(pin):
    if int(len(pin)) == 4 or int(len(pin)) == 6:
        result = True
        numbers = "0123456789"
        
        for i in pin:
            if i not in numbers:
                result = False
        return result
    return False