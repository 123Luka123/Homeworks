from turtle import*

#we want to paint house 

#step1: draw a square
speed(10)
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

#End of square

#drawing a door


forward(70)
color("yellow")
begin_fill()
left(90)


forward(120)
right(90)


forward(60)
right(90)


forward(120)
end_fill()


#Door over

#start roof

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# roof over

#start window1

left(30)


penup()
goto(20,130)
right(180)
color("blue")
begin_fill()
pendown()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

#start window2

penup()
goto(180,130)
pendown()
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()





#brown windows 
#fill windows
#fill door






exitonclick()




