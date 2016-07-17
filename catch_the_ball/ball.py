import tkinter

def click_ball(event):
    """
    Обработчик событий для игрового холста canvas
    :param event:  события с координатами клика
    по клику мышкой нужно удалять тот объект, на который мышка указывает.
    А также засчитывать его в очки пользователя.
    """

    # event.x, event.y


def create_random_ball():
    """
    создает шарик в случайном месте игрового холста canvas,
    при этом шарик не выходит за границы холста!
    :return:
    """
    canvas.create_oval (x, y, x+2*R, y+2*R, width=1, fill=random_color())

def init_ball_catch_game():
    """ создаёт необходимое для игры количество шариков,
    по которым нужно будет кликать
    :return:
    """

def init_main_windows():
    global root, canvas

    root = tkinter.Tk()

    canvas = tkinter.Canvas(root, background='white', width=400, height=400)
    canvas.bind("<Motion>", paint)
    canvas.pack()



    for i in range(10):
    oval = canvas.create_oval(2+i*40, 2+i*40, i*40+30, i*40+30, width=2, fill='green')

root.mainloop()
print("Эта строка будет достигнута только при выходе из приложения.")
