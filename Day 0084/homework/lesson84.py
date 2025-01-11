# N1
# Given n, take the sum of the digits of n. 
# If that value has more than one digit, 
# continue reducing in this way until a 
# single-digit number is produced. 
# The input will be a non-negative integer.

def digital_root(n):
    root = 0
    for i in str(n):
        root += int(i)
    if len(str(root)) > 1:
        root = digital_root(root)
    return root