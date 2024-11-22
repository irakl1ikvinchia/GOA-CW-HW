# N1
# შექმენით ფუნქცია სახელად manual_reverse, 
# რომელიც მიიღებს დალაგებულ კოლექციას. 
# თქვენი დავალებაა, რომ შეაბრუნოთ ეს 
# კოლექცია და დააბრუნოთ ამ სახით.

def manual_reverse(colection):
    result = []

    for i in colection:
        result.insert(0, i)

    return result

print(manual_reverse([1,2,3,4,5]))


