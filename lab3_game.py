from tkinter import *
import random
import math
import time
root = Tk()
root.geometry('800x600')
e = Entry(root, width=20)
b = Button(root, text="Ввод имени")
lab = Label(root, bg='black', fg='white', width=20)
canv = Canvas(root,width=800,height=600,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']
#def new_ball():
    #global x,y,r
    #canv.delete(ALL)
    #x = rnd(100,700)
    #y = rnd(100,500)
    #r = rnd(30,50)
    #canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    #root.after(1000,new_ball)
def move_ball():
    global leftx,lefty,rightx,righty,vx,vy
    leftx, lefty, rightx, righty = canv.coords(ball)
    if leftx < 0:
        vx = -vx
    if lefty < 0:
        vy = -vy
    if rightx >800:
        vx = -vx
    if righty>600:
        vy=-vy
    canv.move(ball,vx,vy)
    canv.after(30, move_ball)
def move_ball2():
    global leftx1,lefty1,rightx1,righty1,vx1,vy1
    leftx1, lefty1, rightx1, righty1 = canv.coords(ball2)
    if leftx1 < 0:
        vx1 = -vx1+random.choice([2,3,1,-2,-3,-1])
    if lefty1 < 0:
        vy1 = -vy1+random.choice([2,3,1,-2,-3,-1])
    if rightx1 >800:
        vx1 = -vx1+random.choice([2,3,1,-2,-3,-1])
    if righty1>600:
        vy1=-vy1+random.choice([2,3,1,-2,-3,-1])
    canv.move(ball2,vx1,vy1)
    canv.after(30, move_ball2)
def move_rec():
    global leftx2,lefty2,rightx2,righty2,vx3,l
    l=l+0.2
    leftx2, lefty2, rightx2, righty2=canv.coords(rec)
    canv.move(rec,vx3*math.sin(l),vx3*math.cos(l))
    canv.after(30, move_rec)

c1=0
def click(event):
    global x1,y1,c,c1
    x1=event.x
    y1=event.y
    if c1!=3:
        if (x1>leftx1 and x1<rightx1) and (y1>lefty1 and y1<righty1):
            c += 1
        if (x1>leftx and x1<rightx) and (y1>lefty and y1<righty):
            c += 1
        if (x1>leftx2 and x1<rightx2) and (y1>lefty2 and y1<righty2):
            c += 1
        if ((x1 <leftx2 or x1 >rightx2) or (y1 <lefty2 or y1 > righty2)) and ((x1 <leftx1 or x1 >rightx1) or (y1 <lefty1 or y1 > righty1)) and ((x1 <leftx or x1 >rightx) or (y1 <lefty or y1 > righty)):
            c1+=1
        print(c1)
    else:
        Text = "ВЫ ПРОИГРАЛИ.УЖАС."
        label = Label(root, text=Text)
        label_x = 400
        label_y = 400
        label.place(x=label_x, y=label_y)
        f.open('laba.txt','a')
        f.append(str(c))
        f.close()

    Text = "Score:" + str(c)
    label = Label(root, text=Text)
    label_x = 700
    label_y = 550
    label.place(x=label_x, y=label_y)


c=0
x1=0
y1=0
r2=30
vx=5
vy=10
vx1=15
vy1=-10
l=0
#new_ball()
ball=canv.create_oval(100,100,200,200,fill = random.choice(colors))
ball2=canv.create_oval(100,100,170,170,fill = random.choice(colors))
vx3=20
rec=canv.create_rectangle(400,300,450,350,fill=random.choice(colors))
move_rec()
Text = "Score:" + str(c)
Text2="У вас три попытки"
label1 = Label(root, text=Text2)
label1_x = 350
label1_y = 0
label1.place(x=label1_x, y=label1_y)
label = Label(root, text=Text)
label_x = 700
label_y = 550
label.place(x=label_x, y=label_y)
move_ball()
move_ball2()
canv.bind('<Button-1>', click)
name1=e.get()
f=open("laba.txt",'a')
f.write(str(name1))
f.close()
e.pack()
b.pack()
lab.pack()

mainloop()
