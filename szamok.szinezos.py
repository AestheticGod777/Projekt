from turtle import Turtle
from turtle import Screen

hosszuvonal = 98
rovidvonal = 20
kozepesvonal = 70

class Mukodjel:
    def trapezbal(self, turtle):
        turtle.begin_fill()
        turtle.forward(hosszuvonal)
        turtle.left(135)
        turtle.forward(rovidvonal)
        turtle.left(45)
        turtle.forward(kozepesvonal)
        turtle.left(45)
        turtle.forward(rovidvonal)
        turtle.left(135)
        turtle.penup()
        turtle.forward(100)
        turtle.pendown()
        turtle.end_fill()

    def emerald(self, turtle):
        turtle.begin_fill()
        turtle.left(225)
        turtle.forward(20)
        turtle.right(45)
        turtle.forward(70)
        turtle.right(45)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(45)
        turtle.forward(70)
        turtle.right(45)
        turtle.forward(20)
        turtle.right(45)
        turtle.end_fill()

    def nulla(self, turtle):
        self.trapezbal(turtle)
        turtle.left(90)
        self.trapezbal(turtle)
        self.trapezbal(turtle)
        turtle.left(90)
        self.trapezbal(turtle)
        turtle.left(90)
        self.trapezbal(turtle)
        self.trapezbal(turtle)

    def egy(self, turtle):
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        self.trapezbal(turtle)
        self.trapezbal(turtle)

    def ketto(self, turtle):
        self.trapezbal(turtle)
        turtle.left(90)
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.pendown()
        turtle.right(90)
        self.emerald(turtle)
        turtle.left(180)
        self.trapezbal(turtle)
        turtle.left(90)
        self.trapezbal(turtle)
        turtle.left(90)
        turtle.penup()
        turtle.forward(hosszuvonal + 1)
        turtle.pendown()
        self.trapezbal(turtle)
        turtle.left(90)

    def harom(self, turtle):
        self.trapezbal(turtle)
        turtle.left(90)
        self.trapezbal(turtle)
        turtle.right(90)
        self.emerald(turtle)
        turtle.left(180)
        self.trapezbal(turtle)
        turtle.left(90)
        self.trapezbal(turtle)
        turtle.left(90)
        turtle.penup()
        turtle.forward(hosszuvonal + 1)
        turtle.forward(hosszuvonal + 1)
        turtle.left(90)
        turtle.pendown()

    def negy(self, turtle):
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.pendown()
        self.trapezbal(turtle)
        turtle.right(90)
        self.emerald(turtle)
        turtle.left(180)
        self.trapezbal(turtle)
        turtle.left(90)
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.pendown()
        self.trapezbal(turtle)
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.pendown()

    def ot(self, turtle):
        self.trapezbal(turtle)
        turtle.left(90)
        self.trapezbal(turtle)
        turtle.right(90)
        self.emerald(turtle)
        turtle.left(180)
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.pendown()
        self.trapezbal(turtle)
        turtle.left(90)
        self.trapezbal(turtle)
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.pendown()

    def hat(self, turtle):
        self.trapezbal(turtle)
        turtle.left(90)
        self.trapezbal(turtle)
        turtle.right(90)
        self.emerald(turtle)
        turtle.penup()
        turtle.right(180)
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.pendown()
        self.trapezbal(turtle)
        turtle.left(90)
        for i in range(2):
            self.trapezbal(turtle)
        turtle.left(90)

    def het(self, turtle):
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        for e in range(2):
            self.trapezbal(turtle)
        turtle.left(90)
        self.trapezbal(turtle)
        turtle.penup()
        turtle.left(90)
        turtle.forward(hosszuvonal)
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.penup()

    def nyolc(self, turtle):
        self.trapezbal(turtle)
        turtle.left(90)
        self.trapezbal(turtle)
        for w in range(2):
            self.trapezbal(turtle)
            turtle.left(90)
        for r in range(2):
            self.trapezbal(turtle)
        turtle.backward(hosszuvonal)
        turtle.right(90)
        self.emerald(turtle)
        turtle.backward(hosszuvonal)
        turtle.setheading(0)

    def kilenc(self, turtle):
        self.trapezbal(turtle)
        turtle.left(90)
        self.trapezbal(turtle)
        turtle.right(90)
        self.emerald(turtle)
        turtle.left(180)
        self.trapezbal(turtle)
        turtle.left(90)
        self.trapezbal(turtle)
        turtle.left(90)
        self.trapezbal(turtle)
        turtle.penup()
        turtle.forward(hosszuvonal + 1)
        turtle.left(90)
        turtle.pendown()

    def __init__(self):
        screen = Screen()
        turtle = Turtle()
        turtle.speed(0)
        turtle.fillcolor('red')
        self.kilenc(turtle)
        screen.mainloop()

Mukodjel()