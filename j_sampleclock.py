from turtle import *
from j_clock import *
from szamok import *

class SampleClock:

    scr = Screen()


    secondleft : Szamok
    secondright : Szamok
    hourleft : Szamok
    hourright : Szamok
    clk = Clock(scr)




    def __init__(self):
        self.secondleft = Szamok()
        self.secondright = Szamok()
        self.hourleft = Szamok()
        self.hourright = Szamok()
        self.hourright.turtle.penup()
        self.hourright.turtle.forward(150)
        self.hourright.turtle.pendown()
        self.clk.setOnSecondChangeListener(self.writeSec)
        ##self.clk.setOnMinuteChangeListener(self.writeMin)
        ##self.clk.setOnHourChangeListener(self.writeHour)
        self.scr.mainloop()

    def teszt(self):
        self.hourright.turtle.clear()
        self.hourleft.turtle.clear()
        if (self.clk.leftNumber(self.clk.hour24())) == 0:
            self.hourleft.turtle.speed(0)
            self.hourleft.nulla()
            self.hourleft.turtle.speed(0)

        if (self.clk.leftNumber(self.clk.hour24())) == 1:
            self.hourleft.turtle.speed(0)
            self.hourleft.egy()
            self.hourleft.turtle.speed(0)

        if (self.clk.leftNumber(self.clk.hour24())) == 2:
            self.hourleft.turtle.speed(0)
            self.hourleft.ketto()
            self.hourleft.turtle.speed(0)

        if (self.clk.rightNumber(self.clk.hour24())) == 0:
            self.hourright.turtle.speed(0)
            self.hourright.nulla()
            self.hourright.turtle.speed(0)

        if (self.clk.rightNumber(self.clk.hour24())) == 1:
            self.hourright.turtle.speed(0)
            self.hourright.egy()
            self.hourright.turtle.speed(0)

        if (self.clk.rightNumber(self.clk.hour24())) == 2:
            self.hourright.turtle.speed(0)
            self.hourright.ketto()
            self.hourright.turtle.speed(0)

        if (self.clk.rightNumber(self.clk.hour24())) == 3:
            self.hourright.turtle.speed(0)
            self.hourright.harom()
            self.hourright.turtle.speed(0)

        if (self.clk.rightNumber(self.clk.hour24())) == 4:
            self.hourright.turtle.speed(0)
            self.hourright.negy()
            self.hourright.turtle.speed(0)

        if (self.clk.rightNumber(self.clk.hour24())) == 5:
            self.hourright.turtle.speed(0)
            self.hourright.ot()
            self.hourright.turtle.speed(0)

        if (self.clk.rightNumber(self.clk.hour24())) == 6:
            self.hourright.turtle.speed(0)
            self.hourright.hat()
            self.hourright.turtle.speed(0)

        if (self.clk.rightNumber(self.clk.hour24())) == 7:
            self.hourright.turtle.speed(0)
            self.hourright.het()
            self.hourright.turtle.speed(0)

        if (self.clk.rightNumber(self.clk.hour24())) == 8:
            self.hourright.turtle.speed(0)
            self.hourright.nyolc()
            self.hourright.turtle.speed(0)

        if (self.clk.rightNumber(self.clk.hour24())) == 9:
            self.hourright.turtle.speed(0)
            self.hourright.kilenc()
            self.hourright.turtle.speed(0)




    def printToConsole(self):
        print(str(self.clk.leftNumber(self.clk.hour24())) + str(self.clk.rightNumber(self.clk.hour24())) + ":" + (str(self.clk.leftNumber(self.clk.min())) + str(self.clk.rightNumber(self.clk.min()))) + ":" + (str(self.clk.leftNumber(self.clk.sec())) + str(self.clk.rightNumber(self.clk.sec()))))
        pass

    def writeSec(self):
        self.printToConsole()
        self.teszt()



