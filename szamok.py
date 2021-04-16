from turtle import *

hosszuvonal = 98
rovidvonal = 20
kozepesvonal = 70


class Szamok:

    screen = Screen()

    def trapezbal(self):
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
        self.turtle.forward(100)
        self.turtle.pendown()
        self.turtle.end_fill()

    def trapezjobb(self):
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
        self.turtle.forward(100)
        self.turtle.pendown()
        self.turtle.end_fill()

    def emerald(self):
        self.turtle.fillcolor('red')
        self.turtle.begin_fill()
        self.turtle.left(225)
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
        self.turtle.end_fill()

    def lefttrapezbal90(self):
        self.turtle.left(90)
        self.trapezbal()

    def rightemrightup(self):
        self.turtle.right(90)
        self.emerald()
        self.turtle.right(90)
        self.turtle.penup()
    def upforhosszdown(self):
        self.turtle.penup()
        self.turtle.forward(hosszuvonal)
        self.turtle.pendown()
    def lefttrapez902xtrapezbal(self):
        self.lefttrapezbal90()
        self.trapezbal()
        self.lefttrapezbal90()

    def nulla(self):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        for i in range(2):
            self.lefttrapez902xtrapezbal()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def egy(self):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.turtle.left(90)
        for i in range(2):
            self.trapezbal()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def ketto(self):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        for x in range(2):
            self.trapezjobb()
            self.turtle.left(90)
        self.emerald()
        self.turtle.right(90)
        self.turtle.penup()
        self.turtle.forward(100)
        self.turtle.pendown()
        for x in range(2):
            self.lefttrapezbal90()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def harom(self):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.trapezbal()
        self.lefttrapezbal90()
        self.turtle.right(90)
        self.emerald()
        self.turtle.left(180)
        self.trapezbal()
        self.lefttrapezbal90()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def negy(self):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.lefttrapezbal90()
        self.trapezbal()
        self.turtle.left(180)
        self.upforhosszdown()
        self.turtle.pendown()
        self.turtle.left(90)
        self.emerald()
        self.turtle.right(90)
        self.upforhosszdown()
        self.turtle.left(90)
        self.trapezjobb()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def ot(self):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.trapezbal()
        self.lefttrapezbal90()
        self.rightemrightup()
        self.turtle.forward(98)
        self.turtle.pendown()
        for x in range(2):
            self.turtle.left(90)
            self.trapezjobb()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def hat(self):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.trapezbal()
        self.lefttrapezbal90()
        self.rightemrightup()
        self.turtle.forward(98)
        self.turtle.pendown()
        self.lefttrapezbal90()
        self.turtle.left(180)
        self.turtle.penup()
        self.turtle.forward(98)
        self.turtle.pendown()
        self.turtle.right(180)
        self.trapezjobb()
        self.turtle.left(90)
        self.trapezjobb()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)
    def het(self):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.lefttrapez902xtrapezbal()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def nyolc(self):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        for i in range(2):
            self.het()
        self.turtle.left(90)
        self.turtle.penup()
        self.turtle.forward(101)
        self.turtle.right(90)
        self.turtle.pendown()
        self.emerald()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def kilenc(self):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.lefttrapez902xtrapezbal()
        for x in range(2):
            self.lefttrapezbal90()
        self.turtle.right(90)
        self.emerald()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def __init__(self):
        self.turtle = Turtle()
        self.turtle.speed(0)
