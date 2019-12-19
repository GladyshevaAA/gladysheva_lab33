from tkinter import *
from random import *
from time import *

root = Tk()

c = Canvas(root, width=800, height=1000, bg='white')
c.pack()
root.geometry('800x1000')
v_0 = 1.2  # скорость при отскоке от платформы
Level = 400  # линия, выше которой не поднимается изображение дудла на экране
P_Width = 80  # ширина платформы
P_Height = 5  # толщина платформы
doodle_stop = False  # переменная отвечает за тип движения объектов (true - движутся платформы, false - дудл)
start = True  # отвечает за начало игры
pause = False  # отвечает за приостановку игры
p_lim = 95  # начальная вероятность появления платформы


# функция рисует иконку дудла
def doodle_draw(x, y):
    c.create_oval(x + 15, y - 35, x + 45, y - 5, tags="doodle", fill="blue")
    c.create_rectangle(x, y - 20, x + 60, y, tags="doodle", fill="green")
    c.create_line(x, y, x, y + 10, tags="doodle")
    c.create_line(x + 20, y, x + 20, y + 10, tags="doodle")
    c.create_line(x + 40, y, x + 40, y + 10, tags="doodle")
    c.create_line(x + 60, y, x + 60, y + 10, tags="doodle")


# класс дудла
class Doodle():

    def __init__(self):
        self.x = 300
        self.y = 600
        self.vx = 15
        self.vy = 0
        self.g = 0
        self.life = True
        doodle_draw(self.x, self.y)

    def upd(self):
        if self.y > 800:
            self.life = False
        self.vy -= self.g
        if not doodle_stop:
            self.y -= self.vy
            c.move("doodle", 0, -self.vy)

    def move_left(self):
        if self.x < -60:
            self.x -= self.vx - 800
            c.move("doodle", 800 - self.vx, 0)
        else:
            self.x -= self.vx
            c.move("doodle", - self.vx, 0)

    def move_right(self):
        if self.x > 800:
            self.x += self.vx - 800
            c.move("doodle", -800 + self.vx, 0)
        else:
            self.x += self.vx
        c.move("doodle", self.vx, 0)


# собственно его единственный экземпляр
doodle = Doodle()


# класс платформ
class Platform():

    def __init__(self, x1, y1):
        self.width = P_Width
        self.height = P_Height
        self.x = x1
        self.y = y1
        self.vx = 0
        self.vy = 0
        self.life = True
        self.obj = c.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill='green')

    def upd(self):
        if self.y > 1600:
            self.life = False
        self.y += doodle.vy
        c.move(self.obj, 0, doodle.vy)

    def usl(self):
        if self.y > 1600:
            self.life = False
        c.move(self.obj, 0, 0)


# это массив платформ
platforms = []


# функция,которая гененрирует платформы во время игры
def generate_extra_platforms():
    n = 1
    h = 10
    l = platforms[len(platforms) - 1].y
    if doodle.y <= Level and -400 < l:
        for i in range(1, 40):
            for k in range(1, 10):
                a = randrange(1, 100)
                if a > p_lim:
                    platforms.append(Platform((k - 1) * P_Width, l - (i - 1) * h))


# функция,которая генерирует платформы в начале игры:
def generate_platforms():
    global P_Width, P_Height
    h = 20
    for i in range(1, 40):
        for k in range(0, 10):
            a = randrange(1, 100)
            if a > p_lim:
                platforms.append(Platform(k * P_Width, (i - 1) * h))


# проверяет, напрыгнул ли дудл на платформу, а ещё удаляет платформы ниже экрана (по всем платформам)
def jump_check():
    for p in platforms:
        if not p.life:
            c.delete(p.obj)
            platforms.remove(p)
        elif (doodle.vy <= 0) and (p.x - 60 < doodle.x < p.x + p.width) and (p.y - 10 <= doodle.y <= p.y + P_Height):
            doodle.vy = v_0


# функция, которая проверяет, что должно двигаться : дудл или платформы
def change_check():
    global doodle_stop
    if doodle.y <= Level and doodle.vy >= 0:
        doodle_stop = True
    elif doodle.vy < 0:
        doodle_stop = False


# движение всех объектов на экране
def scr_upd():
    doodle.upd()
    if doodle_stop:
        for p in platforms:
            p.upd()
    else:
        for p in platforms:
            p.usl()
    c.update()


# запуск игры
def start_game():
    global start
    if not start:
        c.delete(ALL)
        generate_platforms()  # функция, которая генерит платформы в начале
        start = True
        game_main()
    else:
        c.delete(ALL)


# приостановка и возобновление игры
def pause_game(event):
    global doodle, pause, d_vy, g_0, platforms, platforms_data
    if start and pause:
        pause = False
    elif start and not pause:
        pause = True


# выход из игры
def stop_game(event):
    global start
    if start:
        c.delete(ALL)
        start = False


def key(event):
    if (event.char == 'a'):
        doodle.move_left()
    if (event.char == 'd'):
        doodle.move_right()


# основной ход игры ПРОБЛЕМА - не знаю, как реализовать
def game_main():
    global start, v_0, p_lim, Level, checker
    if start:
        c.bind('<Key>', key)
        generate_platforms()
        doodle.vy = v_0
        doodle.g = 0.002
        while doodle.life:
            jump_check()
            change_check()
            generate_extra_platforms()
            if not pause:
                scr_upd()  # функция, которая занимается движением всего на экране


c.focus_set()
game_main()
mainloop()
