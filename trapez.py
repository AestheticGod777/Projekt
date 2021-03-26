from turtle import *


class Kattintgato:

    screen = Screen()
    turtle = Turtle()

    def trapez(self):
        hosszuvonal = 90
        rovidvonal = 20
        kozepesvonal = 70
        self.turtle.forward(hosszuvonal)
        self.turtle.left(120)
        self.turtle.forward(rovidvonal)
        self.turtle.left(60)
        self.turtle.forward(kozepesvonal)
        self.turtle.left(60)
        self.turtle.forward(rovidvonal)
        self.turtle.left(120)
        self.turtle.penup()
        self.turtle.forward(100)
        self.turtle.pendown()

    def nulla(self):
        self.turtle.left(90)
        self.trapez()
        self.trapez()
        self.turtle.left(90)
        self.turtle.penup()
        self.turtle.forward(90)
        self.turtle.pendown()
        self.turtle.left(90)
        self.trapez()
        self.trapez()




    def __init__(self):
        self.turtle.speed(0)
        self.nulla()

        self.screen.mainloop()


Kattintgato()