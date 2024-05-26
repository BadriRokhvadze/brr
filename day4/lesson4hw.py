from turtle import *
import turtle

bgcolor("cyan")

tracer(0)
 #field and river
penup()
goto(-1000,-30)
pendown()

color("green")

begin_fill()

right(90)
forward(220)
left(90)
forward(2000)
left(90)
forward(220)
left(90)
forward(2000)

left(180)


end_fill()

begin_fill()

penup()
goto(-1000,-360)
pendown()

forward(2000)
right(90)
forward(30)
right(90)
forward(2000)
right(90)
forward(30)

right(90)

end_fill()

color("blue")

penup()
goto(-1000,-250)
pendown()

begin_fill()

forward(2000)
right(90)
forward(110)
right(90)
forward(2000)
right(90)
forward(110)

right(90)
end_fill()

 #field and river done

 #bridge
color("brown")

penup()
goto(-50,-250)
pendown()

begin_fill()

left(250)
forward(120)
left(110)
forward(200)
left(110)
forward(120)
left(70)
forward(120)

end_fill()

right(180)

 #bridge done

 #castle walls
color("aquamarine4")

penup()
goto(-300,-250)
pendown()

begin_fill()

forward(600)
left(90)
forward(250)
left(90)
forward(600)
left(90)
forward(250)

end_fill()
 #castle walls done

 #castle towers
begin_fill()

left(180)
forward(400)
right(90)
forward(100)
right(90)
forward(150)

left(90)
forward(100)
left(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)

left(90)
forward(100)
left(90)
forward(150)
right(90)
forward(100)
right(90)
forward(150)

end_fill()

penup()
goto(-200,20)
pendown()

begin_fill()

left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)
right(90)
forward(100)
right(90)
forward(20)

end_fill()

right(90)

penup()
goto(100,20)
pendown()

begin_fill()

forward(20)
left(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)
right(90)
forward(100)
right(90)
forward(20)

end_fill()

right(180)
 #castle towers done

 #tower roofs
color("brown")

penup()
goto(-305,150)
pendown()

begin_fill()

left(90)
forward(110)
left(120)
forward(110)
left(120)
forward(110)
end_fill()

penup()
goto(-105,200)
pendown()

begin_fill()

left(120)
forward(210)
left(120)
forward(210)
left(120)
forward(210)

end_fill()

penup()
goto(305,150)
pendown()

begin_fill()

right(120)
forward(110)
left(120)
forward(110)
left(120)
forward(110)

end_fill()

color("black")
 #tower roofs done

 #castle gate
color("brown")

penup()
goto(-50,-250)
pendown()

begin_fill()

left(90)
forward(100)
right(90)
forward(120)
right(90)
forward(100)

end_fill()

penup()
goto(-50,-150)
pendown()
begin_fill()

circle(radius=60)

end_fill()

color("black")

penup()
goto(10,-250)
pendown()

left(180)
forward(160)

right(180)
 #castle gate done

 #castle windows
color("brown")

penup()
goto(-75,100)
pendown()

begin_fill()

circle(radius=75)

end_fill()

penup()
goto(-275,75)
pendown()

begin_fill()

circle(radius=25)

end_fill()

penup()
goto(225,75)
pendown()

begin_fill()

circle(radius=25)

end_fill()
 #castle windows done

 #goa flags
color("black")

penup()
goto(-250,240)
pendown()

begin_fill()

right(180)
forward(60)
right(90)
forward(70)
left(90)
forward(40)
left(90)
forward(70)
left(90)
forward(40)

end_fill()

penup()
goto(250,240)
pendown()

begin_fill()

right(180)
forward(60)
right(90)
forward(70)
left(90)
forward(40)
left(90)
forward(70)
left(90)
forward(40)

end_fill()

color("white")

penup()
goto(-235,310)
pendown()

turtle.write("GOA",font="Verdana")

penup()
goto(265,310)
pendown()

turtle.write("GOA",font="Verdana")
 #goa flags done

 #queen
color("black")

penup()
goto(-50,90)
pendown()

left(90)

circle(10)

right(90)
forward(48)

penup()
goto(-50,80)
pendown()

left(10)
forward(30)

penup()
goto(-50,80)
pendown()

right(20)
forward(30)

width(5)

color("yellowgreen")

penup()
goto(-60,105)
pendown()

forward(30)
left(20)

penup()
goto(-40,105)
pendown()

forward(30)

color("yellow")

width(10)

penup()
goto(-60,105)
pendown()

left(80)
forward(20)

left(90)
forward(10)

penup()
goto(-60,105)
pendown()

forward(10)

penup()
goto(-50,105)
pendown()

forward(10)

penup()
goto(-50,105)
pendown()

color("magenta")

circle(0.2)
 #queen done

 #king
width(1)

color("black")

penup()
goto(40,100)
pendown()

right(90)

circle(15)

right(90)
forward(63)

penup()
goto(40,90)
pendown()

left(10)
forward(47)

penup()
goto(40,90)
pendown()

right(20)
forward(47)

penup()
goto(25,125)
pendown()

color("yellow")

width(10)

left(100)
forward(30)

width(5)

left(90)
forward(10)

penup()
goto(25,125)
pendown()

forward(10)

penup()
goto(40,125)
pendown()

forward(20)

penup()
goto(55,125)
pendown()

forward(10)

penup()
goto(32.5,125)
pendown()

forward(15)

penup()
goto(47.5,125)
pendown()

forward(15)

penup()
goto(-50000000,1000000)
pendown()
 #king done

exitonclick()
