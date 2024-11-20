# N1
# Complete the solution so that 
# the function will break up camel 
# casing, using a space between words.

def solution(s):
    new_s = ""
    
    for i in s:
        if i.isupper():
            new_s += " " + i
        else:
            new_s += i
            
    return new_s


# N2
# Define a function that 
# takes an integer argument 
# and returns a logical value 
# true or false depending on 
# if the integer is a prime.

def is_prime(num):
    if num <= 0 or num == 1:
        return False
    i = 2
    
    while (i <= num **0.5):
        if num % i == 0:
            return False
        i += 1
    return True


# N3
# Write a function that when given 
# a number >= 0, returns an Array 
# of ascending length subarrays.

def pyramid(n):
    new_n = []
    
    for i in range(1, n + 1):
        new_n.append(i * [1])
        
    return new_n


# N4
# You need to write a function 
# that reverses the words in a 
# given string. Words are always 
# separated by a single space.

def reverse(st):
    new_st = []
    splited_st = st.split()
    
    for i in splited_st[::-1]:
        new_st.append(i)
        
    return " ".join(new_st)


# N5
# In this kata you will create 
# a function that takes in a list 
# and returns a list with the reverse order.

def reverse_list(l):
    return l[::-1]


# N6
# It's pretty straightforward. 
# Your goal is to create a function 
# that removes the first and last 
# characters of a string. You're given 
# one parameter, the original string. 
# You don't have to worry about strings 
# with less than two characters.

def remove_char(s):
    return s[1:-1]


# N7
# Very simple, given a number 
# (integer / decimal / both 
# depending on the language), 
# find its opposite (additive inverse).

def opposite(number):
    return -number