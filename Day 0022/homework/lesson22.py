# N1
# You get an array of numbers, return the sum of all of the positives ones.

def positive_sum(arr):
    result = 0
    
    for i in arr:
        if i > 0:
            result += i
    return result