import turtle
from math import sin

n=int(input("Введите целое число "))
t = turtle.Turtle()
t.shape("turtle")
t.color("darkgreen", "red")
t.shapesize(1)
t.speed(20)
t.penup()
t.backward(300)


def main():
    number = str(n)
    for i in range(len(number)):
        if int (number[i]) == 1:
            digit_one(50)
            t.forward(30)
        elif int (number[i]) == 2:
            digit_two(50)
            t.forward(30)
        elif int (number[i]) == 3:
            digit_three(50)
            t.forward(30)
        elif int (number[i]) == 4:
            digit_four(50)
            t.forward(30)
        elif int (number[i]) == 5:
            digit_five(50)
            t.forward(30)
        elif int (number[i]) == 6:
            digit_six(50)
            t.forward(30)
        elif int (number[i]) == 7:
            digit_seven(50)
            t.forward(30)
        elif int (number[i]) == 8:
            digit_eight(50)
            t.forward(30)
        elif int (number[i]) == 9:
            digit_nine(50)
            t.forward(30)
        elif int (number[i]) == 0:
            digit_zero(50)
            t.forward(30)
    t.hideturtle()


def digit_one(length):
    """Рисует цифру с высотой length
    слева от направления черепахи
    контракт (договорённость):
          черепаха возвращается в исходную точку,
          и имеет исходную ориентацию
          перо по оканчанию функции поднято"""
    t.penup()
    t.forward(length/2)
    t.pendown()
    t.left(90)
    t.forward(length)
    t.left(90+45)
    t.forward(length*sin(45*3.14/180))
    # обратный ход
    t.backward(length*sin(45*3.14/180))
    t.right(90+45)
    t.backward(length)
    t.right(90)
    t.penup()


def digit_two(length):
    """Рисует цифру с высотой length
    слева от направления черепахи
    контракт (договорённость):
          черепаха возвращается в исходную точку,
          и имеет исходную ориентацию
          перо по оканчанию функции поднято"""
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [180, -135, 45, 90]
    A = [ L1,   L2, L1, L1]

    t.penup()
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    # обратный ход
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()


def digit_three(length):
    """Рисует цифру с высотой length
    слева от направления черепахи
    контракт (договорённость):
          черепаха возвращается в исходную точку,
          и имеет исходную ориентацию
          перо по оканчанию функции поднято"""
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [45, 135, -135, 135]
    A = [L2,  L1,   L2,  L1]

    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    # обратный ход
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    t.forward(L1)


def digit_four(length):
    """Рисует цифру с высотой length
    слева от направления черепахи
    контракт (договорённость):
          черепаха возвращается в исходную точку,
          и имеет исходную ориентацию
          перо по оканчанию функции поднято"""
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [90, 90, -90, 180, 90, 90]
    A = [L1, L1,  L1,  L1, L1, L1]

    t.penup()
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    # обратный ход
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()


def digit_five(length):
    """Рисует цифру с высотой length
    слева от направления черепахи
    контракт (договорённость):
          черепаха возвращается в исходную точку,
          и имеет исходную ориентацию
          перо по оканчанию функции поднято"""
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [90, 90, -90, -90, -90]
    A = [L1, L1,  L1,  L1,  L1]

    t.pendown()
    for lenght, degree in zip(A, B):
        t.forward(lenght)
        t.left(degree)
    # обратный ход
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.right(degree)
        t.backward(lenght)
    t.forward(L1)
    t.penup()


def digit_six(length):
    """Рисует цифру с высотой length
    слева от направления черепахи
    контракт (договорённость):
          черепаха возвращается в исходную точку,
          и имеет исходную ориентацию
          перо по оканчанию функции поднято"""
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [90, 90, 90, 180, -45,  0]
    A = [L1, L1, L1,  L1,  L1, L2]

    t.pendown()
    for lenght, degree in zip(A, B):
        t.forward(lenght)
        t.left(degree)
    # обратный ход
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.right(degree)
        t.backward(lenght)
    t.penup()
    t.forward(L1)


def digit_seven(length):
    """Рисует цифру с высотой length
    слева от направления черепахи
    контракт (договорённость):
          черепаха возвращается в исходную точку,
          и имеет исходную ориентацию
          перо по оканчанию функции поднято"""
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [90, -45, 135]
    A = [L1,  L2,  L1]

    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    # обратный ход
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    t.forward(L1)


def digit_eight(length):
    """Рисует цифру с высотой length
    слева от направления черепахи
    контракт (договорённость):
          черепаха возвращается в исходную точку,
          и имеет исходную ориентацию
          перо по оканчанию функции поднято"""
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [90, 90, -90, -90, -90, -90, 90,  0]
    A = [L1, L1,  L1,  L1,  L1,  L1, L1, L1]

    t.pendown()
    for lenght, degree in zip(A, B):
        t.forward(lenght)
        t.left(degree)
    # обратный ход
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.right(degree)
        t.backward(lenght)
    t.forward(L1)
    t.penup()


def digit_nine(length):
    """Рисует цифру с высотой length
    слева от направления черепахи
    контракт (договорённость):
          черепаха возвращается в исходную точку,
          и имеет исходную ориентацию
          перо по оканчанию функции поднято"""
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [45, 135, -90, -90, -90]
    A = [L2,  L1,  L1,  L1,  L1]

    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    # обратный ход
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    t.forward(L1)


def digit_zero(length):
    """Рисует цифру с высотой length
    слева от направления черепахи
    контракт (договорённость):
          черепаха возвращается в исходную точку,
          и имеет исходную ориентацию
          перо по оканчанию функции поднято"""
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [90,  0, 90, 90,  0,  0]
    A = [L1, L1, L1, L1, L1, L1]

    t.pendown()
    for lenght, degree in zip(A, B):
        t.forward(lenght)
        t.left(degree)
    # обратный ход
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.right(degree)
        t.backward(lenght)
    t.forward(L1)
    t.penup()

main()


# t.hideturtle() # спрятать черепашку
# t.right(30)
# t.left(30)
# t.backward(100)
# t.penup()  # поднять перо
# t.pendown()  # перо опустить
# t.forward(100)
# t.begin_fill # для закраски внутри
# t.end_fill() # впаре с предыдущ...
