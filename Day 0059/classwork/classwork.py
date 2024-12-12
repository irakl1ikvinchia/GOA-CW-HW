# N1
# Given a set of numbers, return the additive 
# inverse of each. Each positive becomes negatives, 
# and the negatives become positives.

def invert(lst):
    result = []
    
    for i in lst:
        result.append(-i)
    return result


# N2
# Write a function that takes an array of words 
# and smashes them together into a sentence and 
# returns the sentence. You can ignore any need 
# to sanitize words or add punctuation, but you 
# should add spaces between each word. Be careful, 
# there shouldn't be a space at the 
# beginning or the end of the sentence!

def smash(words):
    return " ".join(words)


# N3
# Complete the function that takes two integers 
# (a, b, where a < b) and return an array of all 
# integers between the input parameters, including them.

def between(a,b):
    result = []
    
    for i in range(a, b + 1):
        result.append(i)
        
    return result


# N5
# At the annual family gathering, the family 
# likes to find the oldest living family member’s 
# age and the youngest family member’s 
# age and calculate the difference between them.

def difference_in_ages(ages):
    min_ages = min(ages)
    max_ages = max(ages)
    difference_ages = max_ages - min_ages
    
    return (min_ages, max_ages, difference_ages)


# N6
# Given a number, write a function to output 
# its reverse digits. (e.g. given 123 the answer is 321)

def reverse_number(n):
    n = str(n)
    n = n[::-1]
    
    if n[-1] == "-":
        n = n[:-1]
        n = "-" + n
        
    return int(n)