from turtle import *

def draw_square():
    for i in range(4):
        forward(100)
        left(90)

def move_coursor(x, y):
    penup()
    goto(x, y)
    pendown()

draw_square()
move_coursor(0, 200)
draw_square()
move_coursor(-150, 200)
draw_square()
move_coursor(-150, 0)
draw_square()
move_coursor(0, -200)
draw_square()
move_coursor(-150, -200)
draw_square()

exitonclick()