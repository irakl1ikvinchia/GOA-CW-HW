# N1
# A Narcissistic Number (or Armstrong Number) 
# is a positive number which is the sum of its 
# own digits, each raised to the power of the 
# number of digits in a given base. In this Kata, 
# we will restrict ourselves to decimal (base 10).

def narcissistic( value ):
    str_value = str(value)
    digit = len(str_value)
    sum = 0
    
    for i in str_value:
        sum += int(i) ** digit
        
    return value == sum


# N2
# A bookseller has lots of books classified in 26 
# categories labeled A, B, C, ..., Z. Each book has 
# a code of at least 3 characters. The 1st character 
# of a code is a capital letter which defines the book category.

def stock_list(art, cat):
    if len(art) == 0 or len(cat) == 0:
        return ""
    
    books_amout = {}
    
    for i in cat:
        books_amout[i] = 0
        
    for i in cat:
        for x in art:
            if i == x[0]:
                books_amout[i] += int(x.split(" ")[1])
                
    result_str = []
    
    for y in books_amout:  
        result_str.append(f"({y} : {books_amout[y]})")
        
    return " - ".join(result_str)


# N3
# A child is playing with a ball on the nth floor of 
# a tall building. The height of this floor above ground level, h, is known.

def bouncing_ball(h, bounce, window):
    if not(h > 0) or not(bounce > 0 and bounce < 1) or not(window < h):
        return -1
    
    count = 0
    
    while h > window:
        h *= bounce
        count += 2
        
    return count - 1 


# N4
# … a man was given directions to go from one point to another. 
# The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly 
# "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

def dir_reduc(arr):
    complate_list = []
    opposite = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    
    for i in arr:
        if len(complate_list) != 0 and complate_list[-1] == opposite[i]:
            complate_list.pop()
        else:
            complate_list.append(i)
            
    return complate_list