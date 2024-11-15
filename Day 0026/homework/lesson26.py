# N1
# Manual Sum Function: Create a function 
# called manual_sum that iterates over 
# list and adds their sum in a variable, 
# then returns variable. Use for loop for this task.

def manual_sum(numbers):
    result = 0

    for i in numbers:
        result += i

    return result

print(manual_sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# N2
#  Manual Max Function: Define a function 
# named manual_max that iterates through 
# list, updating a variable with the 
# maximum value, then returns the maximum 
# value found. Use for loop for this task.

def manual_max(numbers):
    max_num = numbers[0]

    for i in numbers:
        if max_num < i:
            max_num = i

    return max_num

print(manual_max([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# N3
# Manual Min Function: Define a function 
# named manual_min that iterates through 
# list, updating a variable with the minimum 
# value, then returns the minimum value found. 
# Use for loop for this task.

def manual_max(numbers):
    max_num = numbers[0]

    for i in numbers:
        if max_num > i:
            max_num = i

    return max_num

print(manual_max([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# N4
#  Manual Len Function: Develop a function 
# named manual_len that iterates through list, 
# counting each element, and returns the 
# count as the length of the list. Use for loop for this task.

def manual_len(collection):
    result = 0

    for i in collection:
        result += 1

    return result

print(manual_len([1, 2, 3, 4, 5, 6, 7, 8, 9]))