# N1
# Create a function that returns 
# the sum of the two lowest positive 
# numbers given an array of minimum 
# 4 positive integers. No floats or 
# non-positive integers will be passed

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]



# N2
# Given a Divisor and a Bound , 
# Find the largest integer N , Such That ,

def max_multiple(divisor, bound):
    if bound % divisor == 0:
        return bound
    
    multiples = []
    
    for i in range(divisor, bound):
        if i % divisor == 0:
            multiples.append(i)
            
    return max(multiples)