from turtle import *

for i in range(4):
    forward(100)
    left(90)


penup()
goto(0, 250)
pendown()

for i in range(4):
    forward(100)
    left(90)

penup()
goto(-100, 250)
pendown()

for i in range(4):
    forward(100)
    left(90)

penup()
goto(-100, 0)
pendown()

for i in range(4):
    forward(100)
    left(90)

exitonclick()