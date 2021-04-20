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
        turtle.penup()
        turtle.left(90)
        turtle.forward(hosszuvonal)
        self.trapezbal(turtle)
        turtle.left(90)
        self.trapezbal(turtle)
        turtle.left(90)
        turtle.penup()
        turtle.forward(hosszuvonal)
        self.trapezbal(turtle)
        turtle.left(90)
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.forward(hosszuvonal)
        turtle.right(90)
        self.emerald(turtle)

    def het(self, turtle):
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        for e in range(2):
            self.trapezbal(turtle)
            turtle.left(90)
        self.trapezbal(turtle)

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
        for q in range(3):
            self.trapezbal(turtle)
            turtle.left(90)
        self.trapezbal(turtle)
        for t in range(2):
            turtle.right(90)
            turtle.forward(100)
        turtle.setheading(0)
    def __init__(self):
        screen = Screen()
        turtle = Turtle()
        turtle.speed(0)
        turtle.fillcolor('red')
        self.kilenc(turtle)
        screen.mainloop()

Mukodjel()