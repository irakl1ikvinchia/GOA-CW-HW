# N1
# I'm new to coding and now I want 
# to get the sum of two arrays... 
# Actually the sum of all their elements. 
# I'll appreciate for your help.

def array_plus_array(arr1,arr2):
    result = sum(arr1) + sum(arr2)
    
    return result


# N2
# You are given the length 
# and width of a 4-sided polygon. 
# The polygon can either be a rectangle or a square.
# If it is a square, return 
# its area. If it is a rectangle, return its perimeter

def area_or_perimeter(l , w):
    if l == w:
        return l * w
    return 2 * (l + w)


# N3
# Move the first letter of each 
# word to the end of it, then 
# add "ay" to the end of the 
# word. Leave punctuation marks untouched.

def pig_it(text):
    words = text.split()
    result = []
    
    for i in words:
        if i.isalpha():
            new_i = i[1:] + i[0] + 'ay'
            result.append(new_i)
        else:
            result.append(i)
    
    return ' '.join(result)