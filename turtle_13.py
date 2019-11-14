
from turtle import *
from math import *

def circle(r):
    for i in range(100):
        forward(r*2 / 100*pi)
        right(360 / 100)

def smile(r):
    for i in range(100):
        forward(r*2 / 100*pi)
        right(180 / 100)


penup()
goto(-250, 0)
left(90)
pendown()
begin_fill()
color('yellow')
circle(250)
end_fill()

penup()
goto(-160, 140)
pendown()
begin_fill()
color('blue')
circle(40)
end_fill()

penup()
goto(90, 140)
pendown()
begin_fill()
color('blue')
circle(40)
end_fill()

penup()
goto(200, -20)
pendown()
right(180)
color('red')
width(25)
smile(100)

penup()
goto(0, 50)
pendown()
color('brown')
right(180)
forward(70)

done()