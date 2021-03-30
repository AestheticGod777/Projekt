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

    def nyolc(self):
        for i in range(2):
            self.turtle.left(90)
            self.trapez()
            self.trapez()
            self.turtle.left(90)
            self.trapez()
        self.turtle.penup()
        self.turtle.left(90)
        self.turtle.forward(98)
        self.turtle.pendown()
        self.turtle.left(135)
        self.turtle.forward(20)
        self.turtle.right(45)
        self.turtle.forward(70)
        self.turtle.right(45)
        self.turtle.forward(20)
        self.turtle.right(90)
        self.turtle.forward(20)
        self.turtle.right(45)
        self.turtle.forward(70)
        self.turtle.right(45)
        self.turtle.forward(20)
        self.turtle.right(45)

    def __init__(self):
        self.turtle.speed(0)
        self.nyolc()

        self.screen.mainloop()


Kattintgato()