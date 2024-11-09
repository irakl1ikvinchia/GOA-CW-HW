# N1

def filter_evens(numbers):
    filtered_list = []

    for i in numbers:
        if i > 10 and i % 2 == 0:
            filtered_list.append(i)

    return filtered_list

def sum_of_numbers(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i

    return sum

user_input = int(input("enter how many numbers do you wantto input: "))
numbers = []

for i in range(user_input):
    number = int(input("Entr number: "))
    numbers.append(number)

print(sum_of_numbers(numbers))
print(filter_evens(numbers))


# N2

def sort_list(numbers):
    for index in range(len(numbers)):
        if numbers[index - 1] < numbers[index]:
            temp = numbers[index]
            numbers[index - 1] = numbers[index]
            numbers[index] = temp
    return numbers

numbers = [1, 5, 4, 3, 6, 2, 9, 7, 8]
print(sort_list(numbers))