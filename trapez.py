from turtle import *


class Kattintgato:

    screen = Screen()
    turtle = Turtle()

    def trapez(self):
        hosszuvonal = 98
        rovidvonal = 20
        kozepesvonal = 70
        self.turtle.forward(hosszuvonal)
        self.turtle.left(135)
        self.turtle.forward(rovidvonal)
        self.turtle.left(45)
        self.turtle.forward(kozepesvonal)
        self.turtle.left(45)
        self.turtle.forward(rovidvonal)
        self.turtle.left(135)
        self.turtle.penup()
        self.turtle.forward(100)
        self.turtle.pendown()

    def nulla(self):
        self.turtle.left(90)
        self.trapez()
        self.trapez()
        self.turtle.left(90)
        self.trapez()
        self.turtle.left(90)
        self.trapez()
        self.trapez()
        self.turtle.left(90)
        self.trapez()

    def __init__(self):
        self.turtle.speed(0)
        self.nulla()

        self.screen.mainloop()


Kattintgato()