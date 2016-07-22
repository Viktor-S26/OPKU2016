from drawman import *
from time import sleep


def list1():
    """Рисуем лист, справой стороны стебля"""
    t.pendown()
    for i in range(2):
        for i in range(90):
            t.forward(1.5)
            t.right(1)
        t.right(90)
    t.penup()


def list2():
    """Рисуем лист, слевой стороны стебля"""
    t.pendown()
    for i in range(2):
        for i in range(90):
            t.forward(1.5)
            t.left(1)
        t.left(90)
    t.penup()


def list3():
    """Рисуем лепесток цветка"""
    t.pendown()
    for i in range(90):
        t.forward(1.5)
        t.right(1)
    for i in range(90):
        t.forward(1.5)
        t.left(1)
    t.right(180)
    for i in range(90):
        t.forward(3)
        t.right(1)
    t.right(90)
    t.penup()


t.left(90)
t.penup()
t.backward(350)
t.pendown()
t.forward(70)
list1()
t.pendown()
t.forward(80)
list2()
t.pendown()
t.forward(340)
for i in range(10):
    list3()
    t.right(36)

sleep(5)
