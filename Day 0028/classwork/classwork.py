# N1
# Complete the function that 
# accepts a string parameter, 
# and reverses each word in the 
# string. All spaces in the 
# string should be retained.

def reverse_words(text):
    text = text.split(" ")
    rev_text = []
    
    for i in text:
        rev_text.append(i[::-1])
        
    return str(" ".join(rev_text))