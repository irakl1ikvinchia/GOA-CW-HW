from turtle import *

# we want to paint a house
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
# end of square

# draving a door
forward(70)
color("yellow")
left(90)

forward(100)
right(90)

forward(60)
right(90)
forward(100)
# end of door

# draving a roof
penup()
goto(200, 200)
pendown()
color("red")

begin_fill()
right(150)
forward(200)
left(120)

forward(200)
end_fill()
# end of roof

exitonclick()