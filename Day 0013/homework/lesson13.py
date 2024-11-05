# # N1

i = 0

while i <= 10:
    print(i)
    i = i + 1


# # N2

for i in range(10):
    if i % 2 == 0:
        print(i)


# # N3

number = int(input("please enter your number: "))

if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")


# # N4

authorized = False
password = "ika123"

while authorized != True:
    user_password = input("please enter your password: ")
    if user_password == password:
        print("Accses granted")
        authorized = True
    else:
        print("try again")


# # N5

i = 0

while i <= 10:
    if i == 5:
        break
    else:
        print(i)
    i = i + 1


# N6

result = False

while result != True:
    user_input  = int(input("please enter number: "))
    if user_input >= 1 and user_input <= 5:
        print("Valid input")
        result = True
    else:
        print("Invalid input")


# N7

num1 = int(input("Enter your number: "))

if num1 % 3 == 0:
    print("Fizz")
elif num1 % 5 == 0:
    print("Buzz")
elif num1 % 3 and num1 % 5 == 0:
    print("FizzBuzz")
else:
    print(num1)