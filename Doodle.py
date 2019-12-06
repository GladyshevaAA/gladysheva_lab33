from tkinter import *
import math
import array
root = Tk()
from random import randrange as rnd

c = Canvas(root, width=600, height=800, bg='white')
width = 600
height = 800
c.pack()
root.geometry('600x800')
v_0 = 10 #скорость при отскоке от платформы
Level = 300
P_Width = 80
P_Height = 3

def doodle_draw(x, y) :
    c.create_oval(x + 20, y - 40, x + 40, y -20, fill = "blue")
    c.create_rectangle(x, y - 20, x + 60, y, fill = "green")
    c.create_line(x, y, x, y + 10)
    c.create_line(x + 20, y, x, y + 10)
    c.create_line(x + 40, y, x, y + 10)
    c.create_line(x + 60, y, x, y + 10)

class Doodle():
    def __init__(self):
        self.x=50
        self.y=30
        self.vx =20
        self.vy = 0
        self.g=10
        self.r = 20
        self.max_H = self.y - (self.vy ^ 2) / (2 * self.g)
        self.obj = doodle_draw(self.x, self.y)
    def Move_y(self):
        c.move(self.obj, 0, self.vy)
        self.vy -= self.g
    def MoveLeft(self):
        c.move(self.obj, -self.vx, 0)
        self.x -= self.vx
    def MoveRight(self):
        c.move(self.obj, self.vx, 0)
        self.x += self.vx
    def jump(self):
        for p in Platform :
            if self.vy <= 0 and ( self.x >= p.x and self.x <= p.x + p.width )  and self.y >= p.y :
                self.vy = v_0

class Platform():
    def __init__(self):
        self.width = P_Width
        self.height = P_Height
        self.x=-10
        self.y=-10
        self.vx=0
        self.vy=0
        self.type = 1
        self.life = 1
        if self.type == 1 :
            self.color = "green"
        elif self.type == 2 :
            self.color = "blue"
        elif self.type == 3 :
            self.color = "red"
        self.obj = c.create_(self.x, self.y, self.x + self.width, self.y + self.height, fill = self.color)
    def Move(self):
        if self.x + self.width >= 600 and self.vx > 0:
            self.vx = -self.vx
            self.x = 599
        if self.x <= 0 and self.vx < 0:
            self.vx = -self.vx
            self.x = 1

doodle = Doodle()


if doodle.max_H < Level :
    delta = Level - doodle.y
    for p in Platform :
        p.y -= delta

n=0
count = 0
plat = []
while h*(n + 1)<delta:
    for i in range (1, 10):
        a=rnd(1, 100)
        if a > p_lim :
            plat.append( Platform() )
            l = len(plat) - 1
            plat[l].x = i * P_Width
            plat[l].y = rnd()
