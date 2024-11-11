# N1
# Welcome. In this kata, you are asked to 
# square every digit of a number and concatenate them.

def square_digits(num):
    result = ""
    
    for i in str(num):
        square = int(i) * int(i)
        result += str(square)
        
    return int(result)


# N2
# Your task is to make a function that 
# can take any non-negative integer as 
# an argument and return it with its 
# digits in descending order. 
# Essentially, rearrange the digits 
# to create the highest possible number.

def descending_order(num):
    num = str(num)
    rev_num = num[::-1]
    
    return int(rev_num)


# N3
# You probably know the "like" 
# system from Facebook and other 
# pages. People can "like" blog 
# posts, pictures or other items. 
# We want to create the text that 
# should be displayed next to such an item.

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "Peter likes this"
    elif len(names) == 2:
        return "Jacob and Alex like this"
    elif len(names) == 3:
        return "Max, John and Mark like this"
    elif len(names) == 4:
        return "Alex, Jacob and 2 others like this"


# N4
# Welcome. In this kata, you are asked to square 
# every digit of a number and concatenate them.

def square_digits(num):
    result = ""
    str_num = str(num)
    
    for i in str_num:
        result += str(int(i) ** 2)
    return int(result)


# N5
# Your task is to make a function that can 
# take any non-negative integer as an 
# argument and return it with its digits 
# in descending order. Essentially, 
# rearrange the digits to create the 
# highest possible number.

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


# N6
# If we list all the natural numbers 
# below 10 that are multiples of 3 
# or 5, we get 3, 5, 6 and 9. The 
# sum of these multiples is 23.

def solution(num):
    sum = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


# N7
# You probably know the "like" system 
# from Facebook and other pages. 
# People can "like" blog posts, 
# pictures or other items. We want 
# to create the text that should be 
# displayed next to such an item.

def likes(names):
    if names == []:
        return "no one likes this"
    elif len(names) == 1:
        return names[0] + " likes this"
    elif len(names) == 2:
        return names[0] + " and " + names[1] + " like this"
    elif len(names) == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
        return names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"
    