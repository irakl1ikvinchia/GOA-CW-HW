# N1
# Given a string, remove any characters that are unique from the string.

def only_duplicates(st):
    result = ""
    for i in st:
        if st.count(i) != 1:
            result += i
    return result


# N2
# Complete the solution so that it splits the 
# string into pairs of two characters. If the 
# string contains an odd number of characters 
# then it should replace the missing second 
# character of the final pair with an underscore ('_').

def solution(s):
    if len(s) % 2 != 0:
        s += "_"
    result = []
    
    for i in range(0, len(s), 2):
        result.append(s[i] + s[i + 1])
        
    return result