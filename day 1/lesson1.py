from turtle import *

 #background
tracer(0)

shape("arrow")

color("gray")

width(15)

penup()
goto(-1000,-1000)
pendown()

begin_fill()

forward(10000)
left(90)
forward(10000)
left(90)
forward(10000)
left(180)

end_fill()
 #background_end


 #house_walls
penup()
goto(-100,-200)
pendown()

color("black")

forward(250)
left(90)
forward(250)
left(90)
forward(250)
left(90)
forward(250)
left(90)
 #house_walls_end



 #house_roof
penup()
goto(150,50)
pendown()

begin_fill()

left(120)
forward(250)
left(120)
forward(250)

end_fill()
 #house_roof_end

 #house_door
penup()
goto(0,-200)
pendown()

begin_fill()

right(150)
forward(100)
right(90)
forward(50)
right(90)
forward(100)

end_fill()
 #house_door_end

 #house_windows_1
penup()
goto(-75,-50)
pendown()

left(90)
forward(25)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
 #house_windows_1_end


 #house_windows_2
penup()
goto(125,-50)
pendown()


left(90)
forward(25)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
 #house_windows_2_end

 #house_chimney
penup()
goto(75,50)
pendown()

begin_fill()

right(90)
forward(50)
left(90)
forward(170)
left(90)
forward(50)
left(90)
forward(170)

end_fill()
 #house_chimney_end

 #house_door_handle
penup()
goto(40,-150)
pendown()

color("gray")

shape("circle")

tracer(1)
 #house_door_handle_end






exitonclick()
