from drawman import *
from time import sleep

t.left(90)
x = 30
for i in range(10):
    t.penup()
    t.backward(30)
    t.left(-45)
    t.pendown()
    for i in range(4):
        t.forward(x*2**0.5)
        t.left(90)
    t.left(45)
    x += 30


sleep(3)