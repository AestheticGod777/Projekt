from turtle import *


class Kattintgato:

    scr = Screen()
    t = Turtle()

    def klikk(self, x: float, y: float):
        print(x)
        print(y)
        self.t.goto(x, y)

    def up(self):
        print("up")

    def __init__(self):
        self.scr.onclick(self.klikk)

        self.scr.onkey(self.up, "Escape")
        self.scr.listen()

        self.scr.mainloop()

