# N1
# Return the number 
# (count) of vowels in the given string.

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


# N2
# Your task is to make a 
# function that can take 
# any non-negative integer 
# as an argument and return 
# it with its digits in 
# descending order. 
# Essentially, rearrange 
# the digits to create 
# the highest possible number.

def descending_order(num):
    str_num = ""
    new_num = str(num)
    reversed_str = ""
    res_list = []
    
    for i in range(len(new_num) -1, -1, -1):
        reversed_str += new_num[i]
        
    for i in reversed_str:
        res_list.append(i)
    res_list.sort(reverse = True)
    
    return int("".join(res_list))


# N3
# Given an array of integers, 
# find the one that appears an odd number of times.

def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i
        

# N4
# 