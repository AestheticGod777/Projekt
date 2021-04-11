from turtle import *
from j_clock import *


class SampleClock:

    scr = Screen()
    clk = Clock(scr)

    secturtle = Turtle(shape="turtle")
    minturtle = Turtle(shape="turtle")
    hourturtle = Turtle(shape="turtle")



    def __init__(self):
        self.secturtle._delay(0)
        self.secturtle.speed(0)
        self.minturtle._delay(0)
        self.minturtle.speed(0)
        self.hourturtle._delay(0)
        self.hourturtle.speed(0)
        self.clk.setOnSecondChangeListener(self.writeSec)
        self.clk.setOnMinuteChangeListener(self.writeMin)
        self.clk.setOnHourChangeListener(self.writeHour)

        self.scr.mainloop()


    def teszt(self):
        if (self.clk.leftNumber(self.clk.sec())) == 0:
            print("Nulla")



    def printToConsole(self):
        print(str(self.clk.leftNumber(self.clk.hour24())) + str(self.clk.rightNumber(self.clk.hour24())) + ":" + (str(self.clk.leftNumber(self.clk.min())) + str(self.clk.rightNumber(self.clk.min()))) + ":" + (str(self.clk.leftNumber(self.clk.sec())) + str(self.clk.rightNumber(self.clk.sec()))))
        pass

    def writeSec(self):
        self.printToConsole()
        self.teszt()
        self.secturtle.clear()
        self.secturtle.reset()



    def writeMin(self):
        self.minturtle.clear()
        self.minturtle.reset()


    def writeHour(self):
        self.hourturtle.clear()
        self.hourturtle.reset()