# N1
# In Python, there is a built-in filter 
# function that operates similarly to JS's 
# filter. For more information on how 
# to use this function, visit

def get_even_numbers(arr):
    numbers = []
    
    for i in arr:
        if i % 2 == 0:
            numbers.append(i)
            
    return numbers


# N2
# The first input array 
# is the key to the correct 
# answers to an exam, like 
# ["a", "a", "b", "d"]. 
# The second one contains 
# a student's submitted answers.

def check_exam(arr1,arr2):
    result = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            result += 4
        elif arr2[i] == "":
            result += 0
        else:
            result -= 1
            
    if result < 0:
        return 0
    else:
        return 
    

# N3
# Several people are standing 
# in a row divided into two teams. 
# The first person goes into team 1, 
# the second goes into team 2, 
# the third goes into team 1, and so on.

def row_weights(array):
    team1 = 0
    team2 = 0
    
    for i in range(len(array)):
        if i % 2 == 0:
            team1 = team1 + array[i]
        else:
            team2 = team2 + array[i]
            
    return (team1, team2)