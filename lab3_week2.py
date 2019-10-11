from graph import *
from math import *
import time
c=canvas()
windowSize(700,700)
penColor("black")
brushColor("grey")
rectangle(0,0,2000,300)
penColor('grey')
brushColor("white")
circle(120,340,90)
penColor('white')
brushColor('white')
rectangle(15,340,230,450)
penColor('grey')
line(31,317,207,317) #niz
line(40,287,205,287) #verch
line(71,317,71,340)
line(115,317,115,340)
line(159,317,159,340)
line(47,287,47,317)
line(84,287,84,317)
line(123,287,123,317)
line(165,287,165,317)
line(55,287,55,110)
line(81,287,81,110)
line(110,287,110,110)
line(138,287,138,110)
line(160,287,160,110)
line(28,340,212,340)
penColor('white')
c.create_oval(290,325,390,475, outline='#696969',fill='#696969',width=1)#tulovische
rectangle(290,415,390,515)
penColor('#2F4F4F')
brushColor('#2F4F4F')
rectangle(330,340,350,425)
c.create_oval(300,450,335,470, outline='#696969',fill='#696969',width=1)#steps
c.create_oval(345,450,380,470, outline='#696969',fill='#696969',width=1)
c.create_oval(315,410,335,465, outline='#696969',fill='#696969',width=1)#foot
c.create_oval(345,410,365,465, outline='#696969',fill='#696969',width=1)
rectangle(290,415,390,425)
brushColor('#C0C0C0')
circle(340,320,40)
brushColor('#696969')
circle(340,320,30)
brushColor('#DCDCDC')
circle(340,322,25)#golova
line(327,320,338,313)#glaza
line(353,320,342,313)
polyline([(329,331),(333,328),(337,327),(341,327),(345,328),(349,331)])#rot
c.create_oval(253,355,320,370, outline='#696969',fill='#696969',width=1)#ruka
c.create_oval(360,355,430,370, outline='#696969',fill='#696969',width=1)
line(256,285,256,460)
c.create_oval(70,400,140,425, outline='#696969',fill='#696969',width=1)#koshka
c.create_oval(430,400,455,470, outline='#696969',fill='#696969',width=1)#koshka2
brushColor('#696969')
circle(141,400,15)
circle(440,400,15)#head2
polygon([(141,387),(143,381),(147,389)])
polygon([(131,389),(133,381),(135,387)])
polygon([(422,400),(430,396),(430,404)])
polygon([(422,410),(430,406),(430,412)])
brushColor('white')
circle(134,396,4)
circle(144,396,4)
circle(438,397,4)
circle(438,406,4)
brushColor('black')
circle(136,396,2)
circle(146,396,2)
circle(438,395,2)
circle(438,404,2)
c.create_oval(77,413,85,447, outline='#696969',fill='#696969',width=1)#lapka
c.create_oval(91,413,100,447, outline='#696969',fill='#696969',width=1)
c.create_oval(116,413,125,447, outline='#696969',fill='#696969',width=1)
c.create_oval(128,413,137,447, outline='#696969',fill='#696969',width=1)
c.create_oval(445,455,475,465,outline='#696969',fill='#696969',width=1)#lapka2
c.create_oval(445,442,475,452,outline='#696969',fill='#696969',width=1)
c.create_oval(445,420,475,430,outline='#696969',fill='#696969',width=1)
c.create_oval(445,410,475,420,outline='#696969',fill='#696969',width=1)
c.create_oval(70,375,85,425, outline='#696969',fill='#696969',width=1)#khvost
c.create_oval(440,450,390,465, outline='#696969',fill='#696969',width=1)
run()