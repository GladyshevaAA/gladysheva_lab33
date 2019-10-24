from tkinter import *
from random import randrange as rnd, choice
import time
import math
import array
root = Tk()

c = Canvas(root, width=700, height=700, bg='white')
width = 700
height = 700
c.pack()
root.geometry('700x700')
colors = ['red','orange','yellow','green','blue']


class Ball:
    def __init__(self):
        self.x = rnd(50, width - 50)
        self.y = rnd(50, height - 50)
        self.vx = rnd(-10, 10)
        self.vy = rnd(-10, 10)
        self.r = rnd(20, 50)
        self.obj = c.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = choice (colors), width = 0)



    def WallCollision(self):
        if self.x + self.r >= width and self.vx > 0:
            self.vx = -self.vx

        if self.x - self.r <= 0 and self.vx < 0:
            self.vx = -self.vx

        if self.y + self.r >= height and self.vy > 0:
            self.vy = -self.vy

        if self.y - self.r <= 0 and self.vy < 0:
            self.vy = -self.vy



    def MoveBall(self):
        c.move(self.obj, self.vx, self.vy)
        self.y += self.vy
        self.x += self.vx



Num = 0
m = rnd (3, 7)
balls = [0] * m
for i in range (m):
    balls[i] = Ball()



def Anime():
    global balls
    for i in range (m):

        balls[i].MoveBall()
        balls[i].WallCollision()

    root.after(30, Anime)



def click (event):
    global ex, ey, Num
    ex = event.x
    ey = event.y
    for i in range (m):
        if (ex - balls[i].x)**2 + (ey - balls[i].y)**2 <= balls[i].r**2:
            Num += 1
            Text = "Score:" + str(Num)
            label1 = Label(root, text=Text)
            label1_x = 350
            label1_y = 200
            label1.place(x=label1_x, y=label1_y)

Anime()
c.bind('<Button-1>', click)
Text = "Score:" + str(Num)
label1 = Label(root, text=Text)
label1_x = 350
label1_y = 200
label1.place(x=label1_x, y=label1_y)
mainloop()

print("Total score:")
print(Num)
