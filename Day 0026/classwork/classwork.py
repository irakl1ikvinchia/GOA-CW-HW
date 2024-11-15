def number(numbers):
    for i in range(len(numbers) -1, -1, -1):
        if numbers[i] % 4 == 0:
            return numbers[i]

numbers_list = []

for i in range(10, 50 + 1):
    numbers_list.append(i)

print(number(numbers_list))