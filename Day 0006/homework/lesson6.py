num1 = int(input("enter your num1: "))       # პირველ ხაზზე დავადეკლალირეთ ცვლადი სახელად num1 და მნიშვნელობაში გამოვიყენეთ input("") ფუნქცია
                                             # და შემოტანილი მნიშვნელობა გადავაქციეთ ინტეჯერად int().
num2 = int(input("please enter your num2: "))
num3 = int(input("please enter your num3: "))

result = num1 * num2 * num3   # მეექვსე ხაზზე დავადეკლალირეთ ცვლადი სახელად result და მნიშვნელობად გადავეცით ჩვენი შექმნილი ცვლადების ნამრავლი
print(num1 * num2 * num3)    # მეშვიდე ხაზზე გამოვიძახეთ print() ფუნქცია და დავბეჭდეთ ტერმინალში ჩვენი ცვლადის მნიშვნელობები 


name = input("please enter your name: ")   # მეათე ხაზზე დავადეკლალირეთ ცვლადი სახელად name და გადავეცით მნიშვნელობად input("") ფუნქცია
                                           # რომელიც მნიშვნელობად იღებს სტრინგს str() 
lastname = input("please enter your lastname: ")
age = int(input("please enter your age: "))

introduction = "hello i am", name, lastname, "and iam", age, "years old"   # მეთხუთმეტე ხაზზე დავადეკლალირთ ცვლადი სახელად introduction 
                                                                           # და მნიშვნელობა დავწერეთ ერთი დიდი წინადადება ცვლადების გამოყენებით 
print(introduction)   # და საბოლოოდ დავბეჭდეთ ტერმინალში print() ფუნქციის გამოყენებით 