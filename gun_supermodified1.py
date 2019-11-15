# menu

from tkinter import *
from random import randrange as rnd, choice
import math
import time
root = Tk()

canv = Canvas(root, bg='white')

# print (dir(math))

fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


class ball():
    def __init__(self, x=20, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.ay = 1.5
        self.xtr = 0
        self.ytr = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        self.xtr = -0.1 * self.vx
        self.ytr = -0.1 * self.vy
        if (self.x - self.r < 0 or self.x + self.r > 800):
            self.vx = -self.vx
            self.ytr = -0.1 * self.vy
            self.vy += self.ay + self.ytr
        elif (self.y - self.r < 0 or self.y + self.r > 600):
            self.vy = -self.vy
            self.vx += self.xtr
            self.vy += self.ay
        else:
            self.vy += self.ay
        self.vy += self.ay
        self.y += self.vy
        self.x += self.vx
        canv.move(self.id, self.vx, self.vy)
        if self.y + self.r > 650:
            self.vy = 0
            self.ay = 0
            self.vx = 0
            self.xtr = 0
            self.ytr = 0
            canv.delete(self.id)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < (obj.r + self.r) ** 2:
            return True
        else:
            return False


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.vy = 5
        self.x = 20
        self.y = 450
        self.id = canv.create_line(self.x, self.y, self.x + 30, self.y - 20,
                                   width=7)  # FIXME: don't know how to set it...

    def onclick1(self, event):
        self.y -= 5
        # canv.move(self.id, 0, self.vy)
    def onclick2(self, event):
        self.y += 5

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball(g1.x, g1.y)
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():

    # FIXME: don't work!!! How to call this functions when object is created?
    def __init__(self):
        self.points = 0
        self.live = 1
        self.x = 0
        self.y = 0
        self.r = 0
        self.color = 'red'

        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(10, 60)
        self.vy = rnd(1, 10)
        self.vx = rnd(5, 15)
        self.color = 'red'
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=self.color)

    def move(self):
        self.y += self.vy
        self.x += self.vx
        if (self.x - self.r < 0 or self.x + self.r > 800):
            self.vx = -self.vx
        if (self.y - self.r < 0 or self.y + self.r > 600):
            self.vy = -self.vy
        canv.move(self.id, self.vx, self.vy)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)


t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []


def new_game(event=''):
    global gun, t1, t2, screen1, balls, bullet
    t1.new_target()

    t2.new_target()
    bullet = 0
    balls = []
    root.bind("<KeyPress-Up>", g1.onclick1)
    root.bind("<KeyPress-Down>",g1.onclick2)
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    t1.live = 1
    t2.live = 1
    while (t1.live and t2.live) or balls:
        t1.move()
        t2.move()
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()

            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()

            if t1.live == 0 and t2.live == 0:
                canv.itemconfig(screen1, text='Попыток: ' + str(bullet) )
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


def click_instructions(event):
    global c0, c1, c2, c3, c4, c5, i0, i1, i2, i3, i4,i5
    canv.delete(c0)
    canv.delete(c1)
    canv.delete(c2)
    canv.delete(c3)
    canv.delete(c4)
    canv.delete(c5)
    i5=canv.create_rectangle(0, 0, 800, 600, fill='white')
    i0=canv.create_text(400, 140, text="ИНСТРУКЦИЯ",
                 fill="magenta", justify=CENTER, font="Verdana 20")
    i1=canv.create_text(400, 160, text="1.Ваша цель-попасть в обе цели из пушки.",
                 fill="magenta", justify=CENTER, font="Verdana 14")
    i2 = canv.create_text(400, 180, text="2.Чтобы начать играть,вам нужнo вернуться в основное меню и нажать f",
                          fill="magenta", justify=CENTER, font="Verdana 14")
    i3= canv.create_text(400, 200, text="3.Чтобы вернуться в меню,вам нужно нажать b",
                          fill="magenta", justify=CENTER, font="Verdana 14")
    i4=canv.create_text(400, 220, text="4.Чтобы выйти из игры,нужно нажать e",
                          fill="magenta", justify=CENTER, font="Verdana 14")
def click_out(event):
    global root
    root.destroy()

def click_b(event):
    global c0,c1,c2,c3,c4,c5,i0,i1,i2,i3,i4,i5
    canv.delete(i0)
    canv.delete(i1)
    canv.delete(i2)
    canv.delete(i3)
    canv.delete(i4)
    canv.delete(i5)
    c5 = canv.create_rectangle(0, 0, 800, 600, fill='white')
    c0 = canv.create_text(400, 140, text="GAME",
                          fill="magenta", justify=CENTER, font="Verdana 20")
    c1 = canv.create_rectangle(150, 170, 650, 220, fill='skyblue', outline='magenta', width=3)
    c2 = canv.create_text(400, 195, text="ИГРАТЬ(нажмите f)",
                          fill="magenta", justify=CENTER, font="Verdana 14")
    c3 = canv.create_rectangle(150, 240, 650, 290, fill='skyblue', outline='magenta', width=3)
    c4 = canv.create_text(400, 265, text="ИНСТРУКЦИЯ(нажмите a)",
                          fill="magenta", justify=CENTER, font="Verdana 14")

def click_game(event):
    global c0,c1,c2,c3,c4,c5,i5
    canv.delete(i5)
    canv.delete(c0)
    canv.delete(c1)
    canv.delete(c2)
    canv.delete(c3)
    canv.delete(c4)
    canv.delete(c5)
    new_game()
    print('function')


c5=canv.create_rectangle(0, 0, 800, 600, fill='white')
c0=canv.create_text(400, 140, text="GAME",
                 fill="magenta", justify=CENTER, font="Verdana 20")
c1=canv.create_rectangle(150, 170, 650, 220, fill='skyblue', outline='magenta', width=3)
c2=canv.create_text(400, 195, text="ИГРАТЬ(нажмите f)",
                 fill="magenta", justify=CENTER, font="Verdana 14")
c3=canv.create_rectangle(150, 240, 650, 290, fill='skyblue', outline='magenta', width=3)
c4=canv.create_text(400, 265, text="ИНСТРУКЦИЯ(нажмите a)",
                 fill="magenta", justify=CENTER, font="Verdana 14")
i0=0
i1=0
i2=0
i3=0
i4=0
i5=0
root.bind('a',click_instructions)
root.bind('f',click_game)
root.bind('b',click_b)
root.bind('e',click_out)

mainloop()