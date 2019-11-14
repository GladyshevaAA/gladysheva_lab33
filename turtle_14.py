
from turtle import *

def star(n, length):
    for i in range(n):
        forward(length)
        right(180 - 180/n)

star(5, 100)
penup()
goto(0,100)
pendown()
star(11,100)

done()