from turtle import *


class Szamok:

    turtle : Turtle

    def trapezbal(self):
        hosszuvonal = 49
        rovidvonal = 10
        kozepesvonal = 35
        self.turtle.fillcolor('red')
        self.turtle.begin_fill()
        self.turtle.forward(hosszuvonal)
        self.turtle.left(135)
        self.turtle.forward(rovidvonal)
        self.turtle.left(45)
        self.turtle.forward(kozepesvonal)
        self.turtle.left(45)
        self.turtle.forward(rovidvonal)
        self.turtle.left(135)
        self.turtle.penup()
        self.turtle.forward(50)
        self.turtle.pendown()
        self.turtle.end_fill()

    def trapezjobb(self):
        hosszuvonal = 49
        rovidvonal = 10
        kozepesvonal = 35
        self.turtle.fillcolor('red')
        self.turtle.begin_fill()
        self.turtle.left(180)
        self.turtle.forward(hosszuvonal)
        self.turtle.right(135)
        self.turtle.forward(rovidvonal)
        self.turtle.right(45)
        self.turtle.forward(kozepesvonal)
        self.turtle.right(45)
        self.turtle.forward(rovidvonal)
        self.turtle.right(135)
        self.turtle.penup()
        self.turtle.forward(50)
        self.turtle.pendown()
        self.turtle.end_fill()

    def emerald(self):
        self.turtle.fillcolor('red')
        self.turtle.begin_fill()
        self.turtle.left(225)
        self.turtle.forward(10)
        self.turtle.right(45)
        self.turtle.forward(35)
        self.turtle.right(45)
        self.turtle.forward(10)
        self.turtle.right(90)
        self.turtle.forward(10)
        self.turtle.right(45)
        self.turtle.forward(35)
        self.turtle.right(45)
        self.turtle.forward(10)
        self.turtle.right(45)
        self.turtle.end_fill()

    def nulla(self):
        for i in range(2):
            self.turtle.left(90)
            self.trapezbal()
            self.trapezbal()
            self.turtle.left(90)
            self.trapezbal()

    def egy(self):
        self.turtle.left(90)
        for i in range(2):
            self.trapezbal()

    def ketto(self):
        self.trapezjobb()
        self.turtle.left(90)
        self.trapezjobb()
        self.turtle.left(90)
        self.emerald()
        self.turtle.right(90)
        self.turtle.penup()
        self.turtle.forward(50)
        self.turtle.pendown()
        self.turtle.left(90)
        self.trapezbal()
        self.turtle.left(90)
        self.trapezbal()

    def harom(self):
        self.trapezbal()
        self.turtle.left(90)
        self.trapezbal()
        self.turtle.right(90)
        self.emerald()
        self.turtle.left(180)
        self.trapezbal()
        self.turtle.left(90)
        self.trapezbal()

    def negy(self):
        self.turtle.left(90)
        self.trapezbal()
        self.trapezbal()
        self.turtle.left(180)
        self.turtle.penup()
        self.turtle.forward(49)
        self.turtle.pendown()
        self.turtle.left(90)
        self.emerald()
        self.turtle.right(90)
        self.turtle.penup()
        self.turtle.forward(49)
        self.turtle.pendown()
        self.turtle.left(90)
        self.trapezjobb()

    def ot(self):
        self.trapezbal()
        self.turtle.left(90)
        self.trapezbal()
        self.turtle.right(90)
        self.emerald()
        self.turtle.right(90)
        self.turtle.penup()
        self.turtle.forward(49)
        self.turtle.pendown()
        self.turtle.left(90)
        self.trapezjobb()
        self.turtle.left(90)
        self.trapezjobb()

    def hat(self):
        self.trapezbal()
        self.turtle.left(90)
        self.trapezbal()
        self.turtle.right(90)
        self.emerald()
        self.turtle.right(90)
        self.turtle.penup()
        self.turtle.forward(49)
        self.turtle.pendown()
        self.turtle.left(90)
        self.trapezbal()
        self.turtle.left(180)
        self.turtle.penup()
        self.turtle.forward(49)
        self.turtle.pendown()
        self.turtle.right(180)
        self.trapezjobb()
        self.turtle.left(90)
        self.trapezjobb()

    def het(self):
        self.turtle.left(90)
        self.trapezbal()
        self.trapezbal()
        self.turtle.left(90)
        self.trapezbal()

    def nyolc(self):
        for i in range(2):
            self.turtle.left(90)
            self.trapezbal()
            self.trapezbal()
            self.turtle.left(90)
            self.trapezbal()
        self.turtle.penup()
        self.turtle.left(90)
        self.turtle.forward(50.5)
        self.turtle.pendown()
        self.turtle.left(135)
        self.turtle.forward(10)
        self.turtle.right(45)
        self.turtle.forward(35)
        self.turtle.right(45)
        self.turtle.forward(10)
        self.turtle.right(90)
        self.turtle.forward(10)
        self.turtle.right(45)
        self.turtle.forward(35)
        self.turtle.right(45)
        self.turtle.forward(10)
        self.turtle.right(45)

    def kilenc(self):
        self.trapezbal()
        self.turtle.left(90)
        self.trapezbal()
        self.trapezbal()
        self.turtle.left(90)
        self.trapezbal()
        self.turtle.left(90)
        self.trapezbal()
        self.turtle.right(90)
        self.emerald()

    def __init__(self):
        self.turtle = Turtle()
        self.turtle.speed(0)

