from turtle import *


class Kattintgato:

    turtle = Turtle()

    def trapezbal(self):
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

    def trapezjobb(self):
        hosszuvonal = 98
        rovidvonal = 20
        kozepesvonal = 70
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

    def emerald(self):
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
        self.turtle.forward(100)
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
        self.turtle.forward(98)
        self.turtle.pendown()
        self.turtle.left(90)
        self.emerald()
        self.turtle.right(90)
        self.turtle.penup()
        self.turtle.forward(98)
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
        self.turtle.forward(98)
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
        self.turtle.forward(98)
        self.turtle.pendown()
        self.turtle.left(90)
        self.trapezbal()
        self.turtle.left(180)
        self.turtle.penup()
        self.turtle.forward(98)
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
        self.turtle.forward(101)
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

        self.turtle.speed(0)

        #self.kilenc()
screen = Screen()
szam0 = Kattintgato()
szam0.nulla()
szam1 = Kattintgato()
szam1.egy()
szam2 = Kattintgato()
szam2.ketto()
szam3 = Kattintgato()
szam3.harom()
szam4 = Kattintgato()
szam4.negy()
szam5 = Kattintgato()
szam5.ot()
szam6 = Kattintgato()
szam6.hat()
szam7 = Kattintgato()
szam7.het()
szam8 = Kattintgato()
szam8.nyolc()
screen.mainloop()
