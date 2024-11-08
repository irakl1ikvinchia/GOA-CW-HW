# N1

def func():
    for i in range(10):
        print(i + 1)

func()
func()
func()
func()


# N2

def welcome(name, lastname):
    print("welcome " + name + " " + lastname)

welcome("irakli", "kvinchia")


# N3

def number(num):
    for i in range(num):
        print(i)

number(23)


# N4

def multiplay(num1, num2):
    return num1 * num2

result = multiplay(5, 4)
print(result)


# N5

def operation1(num1, num2):
    return num1 + num2

print(operation1(5, 4))

def operation2(num1, num2):
    return num1 - num2

print(operation2(5, 4))

def operation3(num1, num2):
    return num1 * num2

print(operation3(5, 4))

def operation4(num1, num2):
    return num1 / num2

print(operation4(5, 4))


# N6

number = []

for i in range(100):
    number.append(i)

print(i)