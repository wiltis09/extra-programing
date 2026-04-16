from turtle import *
from time import sleep
import random
import time
from math import *

import time as t


click = False

def on_click(i, j):
    global click

    click = True

onscreenclick(on_click)

def waitforclick():
    global click

    update()
    click = False

    while not click:
        update()
        t.sleep(.1)

    click = False


update()

def Fly(x,y):
    pu()
    goto(x,y)
    pd()
    return()

def Tal(x,y,tur):
    Fly(x,y)
    write(tur, font=style1, align='center')
    return()
    
style1 = ("Arial", 14, "bold")
style2 = ('Courier', 20, 'bold')
style3 = ('Courier', 60, 'bold')
Num =[0,107,"1",87,72,"2",120,-9,"3",86,-96,"4",0,-130,"5",-86,-96,"6",-118,-9,"7",-85,72,"8"]

Screen().bgcolor("lightblue")

speed(0)
ht()
colormode(255)


def Ring():
    k=100
    pensize(10)
    setheading(0)
    for i in range(5):
        #sleep(0.1)
        k = k + 20
        b1 = random.randrange(1, 255)
        b2 = random.randrange(1, 255)
        b3 = random.randrange(1, 255)        
        Cerkel(0,-k,b1,b2,b3,k)
        if k == 200:
            k=80
    pensize(2)
    return()
def Dela(v,R):
    pencolor("plum")
    y = sin(radians(v))
    x = cos(radians(v))
    Fly(120*x,120*y)
    setheading(R)
    circle(120,45)

def Cerkel(x,y,a1,a2,a3,r):
    pu()
    color(a1,a2,a3)
    goto (x,y)
    pd()
    circle(r)
    pu()
    return()

def func():
    clear()
    return()
  
    
speed(0)
Fly(-30, 0)

                    
Welcom1 = "Du är välkommen till Lyckohjul spelet"
Welcom2="Klick på skärmen för att börja"
#write(Welcom, move=False, align="left", font=("Arial", 14, "normal"))
write(Welcom1, font=style2, align='center')
Fly(-30,-40)
write(Welcom2, font=style2, align='center')
hideturtle()
waitforclick()
clear()
Fly(0,0)
RK =0
#Tur = random.randrange(360, 720 ,1)
TU = random.randrange(1, 9 ,1)
Tur = TU*45 + 360
for x in range (6,Tur,6):
    pd()
    for c in ['red', 'plum', 'blue', 'yellow']:
        color(c)
        RK= RK +90
        setheading(RK)
        forward(75)
    RK = RK +6
    setheading(0)
    if x > 360 :
        Ring()
        goto(0,0)
        setheading(0)

pensize(5)
for c in ['red', 'black', 'black', 'yellow']:
    pd()
    color(c)
    RK= RK +90
    setheading(RK)
    forward(75)
setheading(0)
Fly(0,0)
pensize(15)
lt(0)

Fly(0,-120)
pencolor("red")
circle(120)
Fly(0,-140)
pencolor("yellow")
circle(140)
ht()
Dela(67,157)
Dela(157,247)
Dela(247,337)
Dela(337,67)
color(0,0,0)
for i in range (0,24,3):
    Tal(Num[i],Num[i+1],Num[i+2])

Fly(0,-30)
if TU < 8:
    TU = 8 - TU
write(TU, font=style3, align='center')
ht()
