# N1
# You live in the city of Cartesia where all roads are 
# laid out in a perfect grid. You arrived ten minutes 
# too early to an appointment, so you decided to take 
# the opportunity to go for a short walk. The city 
# provides its citizens with a Walk Generating App on 
# their phones -- everytime you press the button it 
# sends you an array of one-letter strings representing 
# directions to walk (eg. ['n', 's', 'w', 'e']). 
# You always walk only a single block for each 
# letter (direction) and you know it takes you one 
# minute to traverse one city block, so create a 
# function that will return true if the walk the 
# app gives you will take you exactly ten minutes 
# (you don't want to be early or late!) and will, 
# of course, return you to your s
# tarting point. Return false otherwise.

def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    arr = [0, 0]
    
    for i in walk:
        if i == "n":
            arr[0] += 1
        elif i == "s":
            arr[0] -= 1
        elif i == "w":
            arr[1] += 1
        else:
            arr[1] -= 1
            
    return arr == [0, 0]


# N2
# You will be given an array of numbers. 
# You have to sort the odd numbers in 
# ascending order while leaving the even 
# numbers at their original positions.

def sort_array(source_array):
    odd_list = []
    
    for i in source_array:
        if i % 2 != 0:
            odd_list.append(i)
    odd_list.sort()
    
    index = 0
    result = []
    
    for i in source_array:
        if i % 2 != 0:
            result.append(odd_list[index])
            index += 1
        else:
            result.append(i)
    return result