# # N1

user_num = int(input("Enter your number: "))

if user_num % 2 == 0:
    print(user_num, "even")
else:
    print(user_num + 1)


# # N2

password = "GOA best"
autorized = False

while autorized != True:
    user_input = input("Please enter your password: ")
    if user_input == password:
        print("Accses granted")
        autorized = True
    else:
        print("Noop")


# # N3

user_string = input("Enter your string: ")

if user_string[0] == "G":
    print(True)
else:
    print(False)


# N4

name1 = input("Enter name1: ")
name2 = input("Enter name2: ")
name3 = input("Enter name3: ")
name4 = input("Enter name4: ")
name5 = input("Enter name5: ")

users_list = []

users_list.append([name1, name2, name3, name4, name5])

print(users_list)


# N5

user_input = int(input("Enter the number: "))

for i in str(user_input):
    i = int(i)
    if i % 1 == 0 and i % i == 0:
        print(i, "this number is prime")
    else:
        print(i, "this number is'n prime")


# N6

i = 10

while i >= 0:
    print(i)
    i = i - 1


# N7

user_num1 = int(input("Enter first num: "))
user_num2 = int(input("Enter second num: "))
user_choise = input("enter operation: ")

if user_choise == "-":
    print(user_num1 - user_num2)
elif user_choise == "+":
    print(user_num1 + user_num2)
elif user_choise == "*":
    print(user_num1 * user_num2)
elif user_choise == "**":
    print(user_num1 ** user_num2)
else:
    print("eror")


# N8

user_name = input("Please enter your name: ")
print(user_name[-1])


# N9


user_number = int(input("Enter your number: "))
even_num = []

for i in range(0, user_number + 1):
    if i % 2 == 0:
        even_num.append(i)

print(even_num)


# N10

user_num = int(input("Enter your num: "))

for i in range(1, user_num):
    print(i * i - 1)