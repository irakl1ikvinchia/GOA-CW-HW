# N1

numbers = []

for i in range(50, 100):
    numbers.append(i)

print(numbers[0:26:3])


# N2

start = int(input("Enter your number: "))
end = start + 10
my_list = []

for i in range(start, end + 1):
    my_list.append(i)

print(my_list[::2])