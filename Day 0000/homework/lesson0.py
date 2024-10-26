from turtle import *

# we want to paint a house
begin_fill()
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
end_fill()
# end of square

# draving a door
begin_fill()
forward(70)
color("yellow")
left(90)

forward(100)
right(90)

forward(60)
right(90)
forward(100)
end_fill()
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

# drawing a windows
color("purple")
left(30)

forward(40)
left(90)

color("black")
begin_fill()
forward(50)
right(90)

forward(50)
right(90)

forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(200, 160)
pendown()

begin_fill()
left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)
end_fill()

exitonclick()