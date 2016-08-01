from tkinter import *
from random import choice, randint

screen_width = 400
screen_height = 300
timer_delay = 100
gravitational_acceleration = 9.8
dt = 2


"""class MovingUnit:

    def __init__(self, x, y, Vx, Vy, R, avatar):
        self._R = R
        self._x = x
        self._y = y
        self._Vx = Vx
        self._Vy = Vy
        self._avatar = avatar

    def fly(self):
        raise RuntimeError()



class shell(MovingUnit):
"""

#!!!


class Ball:  #(MovingUnit):
    initial_number = 20
    minimal_radius = 15
    maximal_radius = 30
    available_colors = ['green', 'blue', 'red']

    def __init__(self):
        """
        создает шарик в случайном месте игрового холста canvas,
        при этом шарик не выходит за границы холста!
        """
        R = randint(Ball.minimal_radius, Ball.maximal_radius)
        x = randint(0, screen_width-1-2*R)
        y = randint(0, screen_height-1-2*R)
        self._R = R
        self._x = x
        self._y = y
        fillcolor = choice(Ball.available_colors)
        self._avatar = canvas.create_oval(x, y, x+2*R, y+2*R, width = 1,
                                          fill = fillcolor, outline = fillcolor)
        self._Vx = randint(-2, +2)
        self._Vy = randint(-2, +2)

    # fillcolor =
    # canvas.create_oval (x, y, x+2*R, y+2*R, width=1, fill=random_color())

    def fly(self):
        ax = 0
        ay = gravitational_acceleration
        self._x += self._Vx*dt + ax*dt**2/2
        self._y += self._Vy*dt + ay*dt**2/2
        #self._Vx += ax*dt
        #self._Vy += ay*dt
        # отбивается от горизонтальных стенок
        if self._x < 0:
            self._x = 0
            self._Vx = -self._Vx
        elif self._x + 2*self._R >= screen_width:
            self._x = screen_width - 2*self._R - 1
            self._Vx = -self._Vx
        # отбивается от вертикальных стенок
        if self._y < 0:
            self._y = 0
            self._Vy = -self._Vy
        elif self._y + 2*self._R >= screen_height:
            self._y = screen_height - 2*self._R - 1
            self._Vy = -self._Vy
        canvas.coords(self._avatar, self._x, self._y,
                       self._x + 2*self._R, self._y + 2*self._R)



class Gun:
    def __init__(self):
        self._x = 0
        self._y = screen_height-1
        self._lx = +30
        self._ly = -30
        self._avatar = canvas.create_line(self._x, self._y,
                                          self._x+self._lx,
                                          self._y+self._ly)

    def shoot(self):
        """
        :return Возвращает объект снаряда
        """
        shell = Ball()
        shell._x = self._lx + shell._x
        shell._y = self._ly + shell._y
        shell._Vx = self._lx/10
        shell._Vy = self._ly/10
        #shell = Shell(shell._x + self._lx, shell._y + self._ly,
                      #self._lx/10, self._ly/10)
        shell._R = 5
        shell.fly()

        return shell

def init_game():
    """ создаёт необходимое для игры количество шариков,
    а также объект - пушку
    """
    global balls, gun, shells_on_fly
    balls = [Ball() for i in range(Ball.initial_number)]
    gun = Gun()
    shells_on_fly = []


def init_main_window():
    global root, canvas, scores_text, scores_value
    root = Tk()
    root.title("Пушка")
    scores_value = IntVar()
    canvas = Canvas(root, width=screen_width, height=screen_height,
                    bg="white")
    scores_text = Entry(root, textvariable=scores_value)
    canvas.grid(row=1, column=0, columnspan=3)
    scores_text.grid(row=0, column=2)

    #canvas = tkinter.Canvas(root, background='white', width=400, height=400)
    canvas.bind("<Button-1>", click_event_handler)
    #canvas.bind("<Motion>", move_all_balls)
    #canvas.pack()



def click_event_handler(event):
    global shells_on_fly
    shell = gun.shoot()
    shells_on_fly.append(shell)



def timer_event():
    for ball in balls:
        ball.fly()
    for shell in shells_on_fly:
        shell.fly()
    canvas.after(timer_delay, timer_event)




if __name__ == "__main__":
    init_main_window()
    init_game()
    timer_event()
    root.mainloop()
    print("приходите играть.")
