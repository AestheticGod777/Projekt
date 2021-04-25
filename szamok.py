from turtle import *

hosszuvonal = 98
rovidvonal = 20
kozepesvonal = 70

class Szamok:

    screen = Screen()

    def rovidcucc(self):
        self.turtle.right(45)
        self.turtle.forward(70)
        self.turtle.right(45)
        self.turtle.forward(20)

    def trapezbal(self):
        self.turtle.fillcolor('aqua')
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

    def emerald(self):
        self.turtle.fillcolor('aqua')
        self.turtle.begin_fill()
        self.turtle.left(225)
        self.turtle.forward(20)
        self.rovidcucc()
        self.turtle.right(90)
        self.turtle.forward(20)
        self.rovidcucc()
        self.turtle.right(45)
        self.turtle.end_fill()

    def nulla(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        for i in range(2):
            self.trapezbal()
            turtle.left(90)
        for i in range(2):
            self.trapezbal()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def egy(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        for i in range(2):
            self.trapezbal()
        turtle.penup()
        self.turtle.goto(x, y)
        turtle.pendown()
        self.turtle.setheading(rot)

    def ketto(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.trapezbal()
        turtle.left(90)
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.pendown()
        turtle.right(90)
        self.emerald()
        turtle.left(180)
        for i in range(2):
            self.trapezbal()
            turtle.left(90)
        turtle.penup()
        turtle.forward(hosszuvonal + 1)
        turtle.pendown()
        self.trapezbal()
        turtle.left(90)
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def harom(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        turtle.right(90)
        self.emerald()
        turtle.left(180)
        for i in range(2):
            self.trapezbal()
            turtle.left(90)
        turtle.penup()
        for i in range(2):
            turtle.forward(hosszuvonal + 1)
        turtle.left(90)
        turtle.pendown()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def negy(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.pendown()
        self.trapezbal()
        turtle.right(90)
        self.emerald()
        turtle.left(180)
        self.trapezbal()
        turtle.left(90)
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.pendown()
        self.trapezbal()
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.pendown()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def ot(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        turtle.right(90)
        self.emerald()
        turtle.left(180)
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.pendown()
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.pendown()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def hat(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        turtle.right(90)
        self.emerald()
        turtle.penup()
        turtle.right(180)
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.pendown()
        self.trapezbal()
        turtle.left(90)
        for i in range(2):
            self.trapezbal()
        turtle.left(90)
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def het(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        for e in range(2):
            self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        turtle.penup()
        turtle.left(90)
        for i in range(2):
            turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def nyolc(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        for w in range(2):
            self.trapezbal()
            turtle.left(90)
        for r in range(2):
            self.trapezbal()
        turtle.backward(hosszuvonal)
        turtle.right(90)
        self.emerald()
        turtle.backward(hosszuvonal)
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def kilenc(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        turtle.right(90)
        self.emerald()
        turtle.left(180)
        self.trapezbal()
        for i in range(2):
            turtle.left(90)
            self.trapezbal()
        turtle.penup()
        turtle.forward(hosszuvonal + 1)
        turtle.left(90)
        turtle.pendown()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def kistrapezbal(self):
        self.turtle.fillcolor('aqua')
        self.turtle.begin_fill()
        self.turtle.forward(hosszuvonal / 2)
        self.turtle.left(135)
        self.turtle.forward(rovidvonal / 2)
        self.turtle.left(45)
        self.turtle.forward(kozepesvonal / 2)
        self.turtle.left(45)
        self.turtle.forward(rovidvonal / 2)
        self.turtle.left(135)
        self.turtle.penup()
        self.turtle.forward(50)
        self.turtle.pendown()
        self.turtle.end_fill()


    def kisrovidcucc(self):
        self.turtle.right(45)
        self.turtle.forward(35)
        self.turtle.right(45)
        self.turtle.forward(10)

    def kisemerald(self):
        self.turtle.fillcolor('aqua')
        self.turtle.begin_fill()
        self.turtle.left(225)
        self.turtle.forward(10)
        self.kisrovidcucc()
        self.turtle.right(90)
        self.turtle.forward(10)
        self.kisrovidcucc()
        self.turtle.right(45)
        self.turtle.end_fill()

    def kotojel(self):
        self.turtle.fillcolor('aqua')
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.turtle.begin_fill()
        self.turtle.left(225)
        self.turtle.forward(10)
        self.kisrovidcucc()
        self.turtle.right(90)
        self.turtle.forward(10)
        self.kisrovidcucc()
        self.turtle.right(45)
        self.turtle.end_fill()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def kisnulla(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.kistrapezbal()
        turtle.left(90)
        self.kistrapezbal()
        for i in range(2):
            self.kistrapezbal()
            turtle.left(90)
        for i in range(2):
            self.kistrapezbal()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def kisegy(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        turtle.penup()
        turtle.forward(hosszuvonal / 2)
        turtle.left(90)
        for i in range(2):
            self.kistrapezbal()
        turtle.penup()
        self.turtle.goto(x, y)
        turtle.pendown()
        self.turtle.setheading(rot)

    def kisketto(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.kistrapezbal()
        turtle.left(90)
        turtle.penup()
        turtle.forward(hosszuvonal / 2)
        turtle.pendown()
        turtle.right(90)
        self.kisemerald()
        turtle.left(180)
        for i in range(2):
            self.kistrapezbal()
            turtle.left(90)
        turtle.penup()
        turtle.forward(hosszuvonal / 2 + 0.5)
        turtle.pendown()
        self.kistrapezbal()
        turtle.left(90)
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def kisharom(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.kistrapezbal()
        turtle.left(90)
        self.kistrapezbal()
        turtle.right(90)
        self.kisemerald()
        turtle.left(180)
        for i in range(2):
            self.kistrapezbal()
            turtle.left(90)
        turtle.penup()
        for i in range(2):
            turtle.forward(hosszuvonal / 2 + 0.5)
        turtle.left(90)
        turtle.pendown()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def kisnegy(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        turtle.penup()
        turtle.forward(hosszuvonal / 2)
        turtle.left(90)
        turtle.pendown()
        self.kistrapezbal()
        turtle.right(90)
        self.kisemerald()
        turtle.left(180)
        self.kistrapezbal()
        turtle.left(90)
        turtle.penup()
        turtle.forward(hosszuvonal / 2)
        turtle.left(90)
        turtle.pendown()
        self.kistrapezbal()
        turtle.penup()
        turtle.forward(hosszuvonal / 2)
        turtle.left(90)
        turtle.pendown()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def kisot(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.kistrapezbal()
        turtle.left(90)
        self.kistrapezbal()
        turtle.right(90)
        self.kisemerald()
        turtle.left(180)
        turtle.penup()
        turtle.forward(hosszuvonal / 2)
        turtle.left(90)
        turtle.pendown()
        self.kistrapezbal()
        turtle.left(90)
        self.kistrapezbal()
        turtle.penup()
        turtle.forward(hosszuvonal / 2)
        turtle.left(90)
        turtle.pendown()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def kishat(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.kistrapezbal()
        turtle.left(90)
        self.kistrapezbal()
        turtle.right(90)
        self.kisemerald()
        turtle.penup()
        turtle.right(180)
        turtle.forward(hosszuvonal / 2)
        turtle.left(90)
        turtle.pendown()
        self.kistrapezbal()
        turtle.left(90)
        for i in range(2):
            self.kistrapezbal()
        turtle.left(90)
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def kishet(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        turtle.penup()
        turtle.forward(hosszuvonal / 2)
        turtle.left(90)
        for e in range(2):
            self.kistrapezbal()
        turtle.left(90)
        self.kistrapezbal()
        turtle.penup()
        turtle.left(90)
        for i in range(2):
            turtle.forward(hosszuvonal / 2)
        turtle.left(90)
        turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def kisnyolc(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.kistrapezbal()
        turtle.left(90)
        self.kistrapezbal()
        for w in range(2):
            self.kistrapezbal()
            turtle.left(90)
        for r in range(2):
            self.kistrapezbal()
        turtle.backward(hosszuvonal / 2)
        turtle.right(90)
        self.kisemerald()
        turtle.backward(hosszuvonal / 2)
        turtle.setheading(0)
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def kiskilenc(self, turtle):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.kistrapezbal()
        turtle.left(90)
        self.kistrapezbal()
        turtle.right(90)
        self.kisemerald()
        turtle.left(180)
        for i in range(2):
            self.kistrapezbal()
            turtle.left(90)
        self.kistrapezbal()
        turtle.penup()
        turtle.forward(hosszuvonal / 2 + 0.5)
        turtle.left(90)
        turtle.pendown()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def __init__(self):
        self.turtle = Turtle()
        self.turtle.speed(0)
