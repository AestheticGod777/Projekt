from turtle import *
from j_clock import *
from szamok import *
import time

class SampleClock:

    scr = Screen()


    secondleft : Szamok
    secondright : Szamok
    minuteleft : Szamok
    minuteright : Szamok
    hourleft : Szamok
    hourright : Szamok
    clk = Clock(scr)
    isUpdated = False


    def __init__(self):
        turtle = Turtle()
        self.minuteleft = Szamok()
        self.minuteright = Szamok()
        self.hourleft = Szamok()
        self.hourright = Szamok()
        self.hourleft.turtle.backward(325)
        self.hourright.turtle.backward(175)
        self.minuteleft.turtle.forward(60)
        self.minuteright.turtle.forward(210)
        self.clk.setOnSecondChangeListener(self.writeSec)
        for i in range(360):
            turtle.forward(1)
            turtle.left(1)
        self.scr.mainloop()
    def teszt(self):
        self.hourright.turtle.clear()
        self.hourleft.turtle.clear()

        if (self.clk.leftNumber(self.clk.hour24())) == 1:
            self.hourleft.turtle.speed(0)
            self.hourleft.egy(self.hourleft.turtle)
            self.hourleft.turtle.speed(0)
            delay(0)

        if (self.clk.leftNumber(self.clk.hour24())) == 2:
            self.hourleft.turtle.speed(0)
            self.hourleft.ketto(self.hourleft.turtle)
            self.hourleft.turtle.speed(0)
            delay(0)

    def teszt2(self):
        if (self.clk.rightNumber(self.clk.hour24())) == 0:
            self.hourright.turtle.speed(0)
            self.hourright.nulla(self.hourright.turtle)
            self.hourright.turtle.speed(0)
            delay(0)

        if (self.clk.rightNumber(self.clk.hour24())) == 1:
            self.hourright.turtle.speed(0)
            self.hourright.egy(self.hourright.turtle)
            self.hourright.turtle.speed(0)
            delay(0)

        if (self.clk.rightNumber(self.clk.hour24())) == 2:
            self.hourright.turtle.speed(0)
            self.hourright.ketto(self.hourright.turtle)
            self.hourright.turtle.speed(0)
            delay(0)

        if (self.clk.rightNumber(self.clk.hour24())) == 3:
            self.hourright.turtle.speed(0)
            self.hourright.harom(self.hourright.turtle)
            self.hourright.turtle.speed(0)
            delay(0)

        if (self.clk.rightNumber(self.clk.hour24())) == 4:
            self.hourright.turtle.speed(0)
            self.hourright.negy(self.hourright.turtle)
            self.hourright.turtle.speed(0)
            delay(0)

        if (self.clk.rightNumber(self.clk.hour24())) == 5:
            self.hourright.turtle.speed(0)
            self.hourright.ot(self.hourright.turtle)
            self.hourright.turtle.speed(0)
            delay(0)

        if (self.clk.rightNumber(self.clk.hour24())) == 6:
            self.hourright.turtle.speed(0)
            self.hourright.hat(self.hourright.turtle)
            self.hourright.turtle.speed(0)
            delay(0)

        if (self.clk.rightNumber(self.clk.hour24())) == 7:
            self.hourright.turtle.speed(0)
            self.hourright.het(self.hourright.turtle)
            self.hourright.turtle.speed(0)
            delay(0)

        if (self.clk.rightNumber(self.clk.hour24())) == 8:
            self.hourright.turtle.speed(0)
            self.hourright.nyolc(self.hourright.turtle)
            self.hourright.turtle.speed(0)
            delay(0)

        if (self.clk.rightNumber(self.clk.hour24())) == 9:
            self.hourright.turtle.speed(0)
            self.hourright.kilenc(self.hourright.turtle)
            self.hourright.turtle.speed(0)
            delay(0)


    def teszt3(self):
        self.minuteright.turtle.clear()
        self.minuteleft.turtle.clear()
        if (self.clk.leftNumber(self.clk.min())) == 0:
            self.minuteleft.turtle.clear()
            self.minuteleft.turtle.speed(0)
            self.minuteleft.nulla(self.minuteleft.turtle)
            self.minuteleft.turtle.speed(0)
            delay(0)

        if (self.clk.leftNumber(self.clk.min())) == 1:
            self.minuteleft.turtle.speed(0)
            self.minuteleft.egy(self.minuteleft.turtle)
            self.minuteleft.turtle.speed(0)
            delay(0)

        if (self.clk.leftNumber(self.clk.min())) == 2:
            self.minuteleft.turtle.speed(0)
            self.minuteleft.ketto(self.minuteleft.turtle)
            self.minuteleft.turtle.speed(0)
            delay(0)

        if (self.clk.leftNumber(self.clk.min())) == 3:
            self.minuteleft.turtle.clear()
            self.minuteleft.turtle.speed(0)
            self.minuteleft.harom(self.minuteleft.turtle)
            self.minuteleft.turtle.speed(0)
            delay(0)

        if (self.clk.leftNumber(self.clk.min())) == 4:
            self.minuteleft.turtle.speed(0)
            self.minuteleft.negy(self.minuteleft.turtle)
            self.minuteleft.turtle.speed(0)
            delay(0)

        if (self.clk.leftNumber(self.clk.min())) == 5:
            self.minuteleft.turtle.speed(0)
            self.minuteleft.ot(self.minuteleft.turtle)
            self.minuteleft.turtle.speed(0)
            delay(0)

        if (self.clk.rightNumber(self.clk.min())) == 6:
            self.minuteleft.turtle.speed(0)
            self.minuteleft.hat(self.minuteleft.turtle)
            self.minuteleft.turtle.speed(0)
            delay(0)

        if (self.clk.leftNumber(self.clk.min())) == 7:
            self.minuteleft.turtle.clear()
            self.minuteleft.turtle.speed(0)
            self.minuteleft.het(self.minuteleft.turtle)
            self.minuteleft.turtle.speed(0)
            delay(0)

        if (self.clk.leftNumber(self.clk.min())) == 8:
            self.minuteleft.turtle.speed(0)
            self.minuteleft.nyolc(self.minuteleft.turtle)
            self.minuteleft.turtle.speed(0)
            delay(0)

        if (self.clk.leftNumber(self.clk.min())) == 9:
            self.minuteleft.turtle.speed(0)
            self.minuteleft.kilenc(self.minuteleft.turtle)
            self.minuteleft.turtle.speed(0)
            delay(0)

    def teszt4(self):
        if (self.clk.rightNumber(self.clk.min())) == 0:
            self.minuteright.turtle.speed(0)
            self.minuteright.nulla(self.minuteright.turtle)
            self.minuteright.turtle.speed(0)
            delay(0)

        if (self.clk.rightNumber(self.clk.min())) == 1:
            self.minuteright.turtle.speed(0)
            self.minuteright.egy(self.minuteright.turtle)
            self.minuteright.turtle.speed(0)
            delay(0)

        if (self.clk.rightNumber(self.clk.min())) == 2:
            self.minuteright.turtle.speed(0)
            self.minuteright.ketto(self.minuteright.turtle)
            self.minuteright.turtle.speed(0)
            delay(0)

        if (self.clk.rightNumber(self.clk.min())) == 3:
            self.minuteright.turtle.speed(0)
            self.minuteright.harom(self.minuteright.turtle)
            self.minuteright.turtle.speed(0)
            delay(0)

        if (self.clk.rightNumber(self.clk.min())) == 4:
            self.minuteright.turtle.speed(0)
            self.minuteright.negy(self.minuteright.turtle)
            self.minuteright.turtle.speed(0)
            delay(0)

        if (self.clk.rightNumber(self.clk.min())) == 5:
            self.minuteright.turtle.speed(0)
            self.minuteright.ot(self.minuteright.turtle)
            self.minuteright.turtle.speed(0)
            delay(0)

        if (self.clk.rightNumber(self.clk.min())) == 6:
            self.minuteright.turtle.speed(0)
            self.minuteright.hat(self.minuteright.turtle)
            self.minuteright.turtle.speed(0)
            delay(0)

        if (self.clk.rightNumber(self.clk.min())) == 7:
            self.minuteright.turtle.speed(0)
            self.minuteright.het(self.minuteright.turtle)
            self.minuteright.turtle.speed(0)
            delay(0)

        if (self.clk.rightNumber(self.clk.min())) == 8:
            self.minuteright.turtle.speed(0)
            self.minuteright.nyolc(self.minuteright.turtle)
            self.minuteright.turtle.speed(0)
            delay(0)

        if (self.clk.rightNumber(self.clk.min())) == 9:
            self.minuteright.turtle.speed(0)
            self.minuteright.kilenc(self.minuteright.turtle)
            self.minuteright.turtle.speed(0)
            delay(0)



    def printToConsole(self):
        print(str(self.clk.leftNumber(self.clk.hour24())) + str(self.clk.rightNumber(self.clk.hour24())) + ":" + (str(self.clk.leftNumber(self.clk.min())) + str(self.clk.rightNumber(self.clk.min()))) + ":" + (str(self.clk.leftNumber(self.clk.sec())) + str(self.clk.rightNumber(self.clk.sec()))))
        pass

    def writeSec(self):
        self.printToConsole()
        self.teszt()
        self.teszt2()
        self.teszt3()
        self.teszt4()


