# N1
# Create a function that returns 
# the sum of the two lowest positive 
# numbers given an array of minimum 
# 4 positive integers. No floats or 
# non-positive integers will be passed.

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]


# N2
# Make a program that filters a 
# list of strings and returns a 
# list with only your friends name in it.

def friend(x):
    result = []
    
    for i in x:
        if len(i) == 4:
            result.append(i)
            
    return result


# N3
# Simple, given a string of words, 
# return the length of the shortest word(s).

def find_short(s):
    new_s = s.split(" ")
    min_len = len(new_s[0])
    
    for i in new_s:
        if min_len > len(i):
            min_len = len(i)
            
    return min_len


# N4
# You are going to be given 
# a non-empty string. Your 
# job is to return the middle 
# character(s) of the string.

def get_middle(s):
    str_len = len(s)
    index = str_len // 2
    
    if str_len % 2 == 0:
        return s[index - 1] + s[index]
    
    return s[index]


# N5
# In this little assignment you 
# are given a string of space 
# separated numbers, and have 
# to return the highest and lowest number.

def high_and_low(numbers):
    string_list = numbers.split(" ")
    numbers_list = []
    
    for i in string_list:
        numbers_list.append(int(i))
        
    return str(max(numbers_list)) + " " + str(min(numbers_list))