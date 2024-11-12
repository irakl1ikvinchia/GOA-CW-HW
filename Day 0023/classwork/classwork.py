# N1 

def count_evens(numbers_list):
    count = 0

    for i in numbers_list:
        if i % 2 == 0:
            count += 1
    return count

print(count_evens([1,2,3,4,5,6,7,8,9]))


# N2

def replace_even_indexes(word, replace_char):
    changed_word = ""
    for i in range(len(word)):
        if i % 2 == 0:
            changed_word += replace_char
        else:
            changed_word += word[i]
    return changed_word

print(replace_even_indexes("irakli", "g"))


# N3

def find_last_even(numbers_list):
    for i in range(len(numbers_list) -1, -1,-1):
        if numbers_list[i] % 2 == 0:
            return numbers_list[i]
        
print(find_last_even([1,2,3,4,5,6,7,8,9]))


# N4

def my_join(join_str, strings_list):
    joined_elements = ""

    for i in strings_list:
        joined_elements += join_str + i
    
    return joined_elements[1:]

print(my_join("+", ["1", "2", "3"]))