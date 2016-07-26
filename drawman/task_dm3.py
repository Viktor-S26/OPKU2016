from turtle import Turtle

# Масштаб от 1 до 10, меняем самостоятельно
n=int(input("Введите целое число - масштаб системы координат от 0 до 10 "))
default_scale = n


def init_drawman():
    """ Инициализация черепашки """
    global t, x_current, y_current, _drawman_scale
    t = Turtle()
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current, y_current)
    drawman_scale(default_scale)


def drawman_scale(scale):
    global _drawman_scale
    _drawman_scale = scale


def test_drawman():
    """ Тестирование работы Чертёжника """
    novid()
    col()
    size()
    axis()
    grid()
    edin()

    pen_down()

    col('black')
    # График функции
    col('red')
    A = (0, 0, 1.4, 2.1, 2.4, 2.7, 2.9, 3.0, 3.1, 3.2, 3.3)
    pen_width(wid=3)
    x = -4.8 + A[default_scale] #!
    scale=shag  #/vod деление на vod здесь не нужно #!
    xe=x*scale
    pen_up()
    y=x*x
    ye=y*scale
    to_point(xe, ye)
    pen_down()
    while x <= 4.8 - A[default_scale]: #!
        x += 0.2
        xe=x*scale
        y=x*x
        ye=y*scale
        to_point(xe,ye)
    pen_up()
    to_point(0, 0)   # Возврат в начало


def novid():
    global t
    t.hideturtle()


def vid():
    global t
    t.showtirtle()


def pen_down():
    global t
    t.pendown()


def pen_up():
    global t
    t.penup()


def on_vector(dx, dy):
    """ Сместиться на вектор """
    to_point(x_current + _drawman_scale*dx, y_current + _drawman_scale*dy)


def to_point(x, y):
    """ Сместиться в точку с учетом масштаба """
    global x_current, y_current
    x_current = x
    y_current = y
    t.goto(_drawman_scale*x_current, _drawman_scale*y_current)


def col(c='red'):
    """ Цвет """
    global t
    t.pencolor(c)


def size():
     """Размеры холста"""
     global t,w,h, _drawman_scale,shag, vod
     shag=20    #!
     vod=1/default_scale  # Сколько в одном делении #!
     w=60*shag  #!
     h=46*shag  #!
     t.screen.screensize(w,h)


def pen_width(wid=2):
    """ Ширина пера """
    global t
    t.width(wid)


def axis():
    global t,w,h,_drawman_scale,vod
    pass
    t.speed(10)
    # Вертикальные линия
    t.width(3)
    t.home()
    # Горизонтальные линия
    t.color('#000000')
    t.write('  0,0')
    x=0
    y=-24*shag #!
    coords=" "+str(x)+", "+str(-24*vod) #!
    t.goto(x, y)
    t.write(coords)

    # Рисуем оси координат
    t.down()
    x=0
    y=24*shag #!
    coords=str(x)+", "+str(24*vod) #!
    t.goto(x, y-shag/2)
    t.left(90)
    t.stamp()
    t.right(90)
    t.write(coords)
    t.up()
    x=-30*shag #!
    y=0
    coords=str(-30*vod)+", "+str(y) #!
    t.goto(x, y)
    t.write(coords)
    t.down()
    x=30*shag #!
    y=0
    coords=str(30*vod)+", "+str(y) #!
    t.goto(x, y)

    t.stamp()
    t.write(coords)


def grid():
    global t,w,h,_drawman_scale,shag
    pass

    t.width(1)
    t.speed(10)
     # Вертикальные линии сетки системы координат
    x=-w/2
    y=h/2
    col('gray')
    while x<=w/2:
        t.up()
        t.goto(x,y)
        t.down()
        if x!=0:
            t.goto(x,-h/2)
        x+=shag
    else:
        t.up()

     # Горизонтальные линии сетки системы координат
    x=-w/2
    y=h/2
    while y>=-h/2:
        t.up()
        t.goto(x,y)
        t.down()
        if y!=0:
            t.goto(w/2,y)
        y-=shag
    else:
        t.up()


def edin():
    global t,w,h,_drawman_scale,shag,vod
    t.color('#000000')
    t.up()
    x=shag
    y=0
    coords=" "+str(vod)
    t.goto(shag, y)
    t.write(coords)
    x=0
    y=shag
    coords="  "+str(vod)
    t.goto(x, shag)
    t.write(coords)


init_drawman()
if __name__ == '__main__':
    import time # Отсюда вынимаем sleep(sec.)
    """  Вызываем функцию тестирования чертежника в главно модуле """
    test_drawman()
    time.sleep(10)
