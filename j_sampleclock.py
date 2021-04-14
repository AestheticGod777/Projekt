from turtle import *
from j_clock import *
from szamok import *

class SampleClock:

    scr = Screen()


    secondleft : Szamok
    secondright : Szamok
    clk = Clock(scr)


    def __init__(self):
        self.secondleft = Szamok()
        self.secondright = Szamok()
        self.clk.setOnSecondChangeListener(self.writeSec)
        ##self.clk.setOnMinuteChangeListener(self.writeMin)
        ##self.clk.setOnHourChangeListener(self.writeHour)
        self.scr.mainloop()
        self.secondleft.turtle.speed(100)

    def teszt(self):

        if (self.clk.leftNumber(self.clk.hour24())) == 0:
            print("egy.nulla")

        if (self.clk.leftNumber(self.clk.hour24())) == 1:
            self.secondleft.turtle.speed(10000000000)
            print("egy.egy")
            self.secondleft.egy()
            self.secondleft.turtle.reset()
            self.secondleft.turtle.speed(10000000000)

        if (self.clk.leftNumber(self.clk.hour24())) == 2:
            print("egy.ketto")

        if (self.clk.rightNumber(self.clk.hour24())) == 0:
            print("ketto.nulla")

        if (self.clk.rightNumber(self.clk.hour24())) == 1:
            print("ketto.egy")

        if (self.clk.rightNumber(self.clk.hour24())) == 2:
            print("ketto.ketto")

        if (self.clk.rightNumber(self.clk.hour24())) == 3:
            print("ketto.harom")

        if (self.clk.rightNumber(self.clk.hour24())) == 4:
            print("ketto.negy")

        if (self.clk.rightNumber(self.clk.hour24())) == 5:
            print("ketto.ot")

        if (self.clk.rightNumber(self.clk.hour24())) == 6:
            print("ketto.hat")

        if (self.clk.rightNumber(self.clk.hour24())) == 7:
            print("ketto.het")

        if (self.clk.rightNumber(self.clk.hour24())) == 8:
            print("ketto.nyolc")




    def printToConsole(self):
        print(str(self.clk.leftNumber(self.clk.hour24())) + str(self.clk.rightNumber(self.clk.hour24())) + ":" + (str(self.clk.leftNumber(self.clk.min())) + str(self.clk.rightNumber(self.clk.min()))) + ":" + (str(self.clk.leftNumber(self.clk.sec())) + str(self.clk.rightNumber(self.clk.sec()))))
        pass

    def writeSec(self):
        self.printToConsole()
        self.teszt()



