from tkinter import *
from random import choice, randint

screen_width = 400
screen_height = 300
timer_delay = 100

class Ball:
    initial_number = 20
    minimal_radius = 15
    maximal_radius = 40
    available_colors = ['green', 'blue', 'red']

    def __init__(self):
    """
    создает шарик в случайном месте игрового холста canvas,
    при этом шарик не выходит за границы холста!
    :return:
    """
    R = randint(Ball.minimal_radius, Ball.maximal_radius)
    x = randint(0, screen_width-1-2*R)
    y = randint(0, screen_height-1-2*R)
    self._R = R
    self._x = x
    self._y = y
    # fillcolor =  \
    # canvas.create_oval (x, y, x+2*R, y+2*R, width=1, fill=random_color())



class Gun:
    def __init__(selfself):
        self._x = 0
        self._y = screen_height-1
        self._lx = +30
        self._ly = -30
        self._avatar = canvas.create_line(self._x, self._y,
                                          self._x+self._lx,
                                          self._y+self._ly)

    def shoot(self):
        shell = Ball()
        shell._x = self._lx
        shell._y = self._ly
        shell._Vx = self._lx/10
        shell._Vy = self._ly/10
        shell._R = 5

        return shell

def init_game():
    """

    """


def init_main_window():
    global root, canvas, scores_text, scores_value

    root = tkinter.Tk()

    canvas = tkinter.Canvas(root, background='white', width=400, height=400)
    canvas.bind("<Button>", click_ball)
    canvas.bind("<Motion>", move_all_balls)
    canvas.pack()


def click_event_handler():
    global shells_on_fly
    shell = gun

if __name__ == "__main__":
    init_main_window()
    init_game()
    root.mainloop()
    print("приходите играть.")
