from j_clock import *
from szamok import *

class SampleClock:

    scr = Screen()
    secondleft : Szamok
    secondright : Szamok
    minuteleft : Szamok
    minuteright : Szamok
    hourleft : Szamok
    hourright : Szamok
    pontrajzoloegy : Szamok
    pontrajzoloketto: Szamok
    clk = Clock(scr)


    def __init__(self):
        self.secondleft = Szamok()
        self.secondright = Szamok()
        self.minuteleft = Szamok()
        self.minuteright = Szamok()
        self.hourleft = Szamok()
        self.hourright = Szamok()
        self.pontrajzoloegy = Szamok()
        self.pontrajzoloketto = Szamok()
        self.pontrajzoloegy.turtle.left(90)
        self.pontrajzoloketto.turtle.left(90)
        self.pontrajzoloketto.turtle.forward(80)
        self.pontrajzoloegy.turtle.forward(75)
        self.pontrajzoloketto.turtle.forward(75)
        self.pontrajzoloegy.turtle.left(90)
        self.pontrajzoloketto.turtle.left(90)
        self.pontrajzoloegy.turtle.forward(100)
        self.pontrajzoloketto.turtle.forward(100)
        self.pontrajzoloegy.turtle.right(90)
        self.pontrajzoloketto.turtle.right(90)
        self.hourleft.turtle.backward(400)
        self.hourright.turtle.backward(280)
        self.minuteleft.turtle.backward(50)
        self.minuteright.turtle.forward(70)
        self.secondleft.turtle.forward(190)
        self.secondright.turtle.forward(270)
        self.clk.setOnSecondChangeListener(self.writeSec)
        self.scr.mainloop()

    def emeraldka(self):
        self.pontrajzoloegy.turtle.hideturtle()
        self.pontrajzoloegy.turtle.clear()
        self.pontrajzoloegy.kotojel()
        delay(0)

    def emeraldkaketto(self):
        self.pontrajzoloketto.turtle.hideturtle()
        self.pontrajzoloketto.turtle.clear()
        self.pontrajzoloketto.kotojel()
        delay(0)

    def oraelso(self):
        self.secondleft.turtle.hideturtle()
        self.secondright.turtle.hideturtle()
        self.minuteleft.turtle.hideturtle()
        self.minuteright.turtle.hideturtle()
        self.hourleft.turtle.hideturtle()
        self.hourright.turtle.hideturtle()
        self.hourright.turtle.clear()
        self.hourleft.turtle.clear()

        if (self.clk.leftNumber(self.clk.hour24())) == 1:
            self.hourleft.egy(self.hourleft.turtle)

        if (self.clk.leftNumber(self.clk.hour24())) == 2:
            self.hourleft.ketto(self.hourleft.turtle)

    def orautolso(self):
        if (self.clk.rightNumber(self.clk.hour24())) == 0:
            self.hourright.nulla(self.hourright.turtle)

        if (self.clk.rightNumber(self.clk.hour24())) == 1:
            self.hourright.egy(self.hourright.turtle)

        if (self.clk.rightNumber(self.clk.hour24())) == 2:
            self.hourright.ketto(self.hourright.turtle)

        if (self.clk.rightNumber(self.clk.hour24())) == 3:
            self.hourright.harom(self.hourright.turtle)

        if (self.clk.rightNumber(self.clk.hour24())) == 4:
            self.hourright.negy(self.hourright.turtle)

        if (self.clk.rightNumber(self.clk.hour24())) == 5:
            self.hourright.ot(self.hourright.turtle)

        if (self.clk.rightNumber(self.clk.hour24())) == 6:
            self.hourright.hat(self.hourright.turtle)

        if (self.clk.rightNumber(self.clk.hour24())) == 7:
            self.hourright.het(self.hourright.turtle)

        if (self.clk.rightNumber(self.clk.hour24())) == 8:
            self.hourright.nyolc(self.hourright.turtle)

        if (self.clk.rightNumber(self.clk.hour24())) == 9:
            self.hourright.kilenc(self.hourright.turtle)


    def percelso(self):
        self.minuteright.turtle.clear()
        self.minuteleft.turtle.clear()
        if (self.clk.leftNumber(self.clk.min())) == 0:
            self.minuteleft.turtle.clear()
            self.minuteleft.nulla(self.minuteleft.turtle)

        if (self.clk.leftNumber(self.clk.min())) == 1:
            self.minuteleft.egy(self.minuteleft.turtle)

        if (self.clk.leftNumber(self.clk.min())) == 2:
            self.minuteleft.ketto(self.minuteleft.turtle)

        if (self.clk.leftNumber(self.clk.min())) == 3:
            self.minuteleft.turtle.clear()
            self.minuteleft.harom(self.minuteleft.turtle)

        if (self.clk.leftNumber(self.clk.min())) == 4:
            self.minuteleft.negy(self.minuteleft.turtle)

        if (self.clk.leftNumber(self.clk.min())) == 5:
            self.minuteleft.ot(self.minuteleft.turtle)

        if (self.clk.leftNumber(self.clk.min())) == 6:
            self.minuteleft.hat(self.minuteleft.turtle)

        if (self.clk.leftNumber(self.clk.min())) == 7:
            self.minuteleft.turtle.clear()
            self.minuteleft.het(self.minuteleft.turtle)

        if (self.clk.leftNumber(self.clk.min())) == 8:
            self.minuteleft.nyolc(self.minuteleft.turtle)

        if (self.clk.leftNumber(self.clk.min())) == 9:
            self.minuteleft.kilenc(self.minuteleft.turtle)

    def percutolso(self):
        if (self.clk.rightNumber(self.clk.min())) == 0:
            self.minuteright.nulla(self.minuteright.turtle)

        if (self.clk.rightNumber(self.clk.min())) == 1:
            self.minuteright.turtle.speed(0)
            self.minuteright.egy(self.minuteright.turtle)

        if (self.clk.rightNumber(self.clk.min())) == 2:
            self.minuteright.ketto(self.minuteright.turtle)

        if (self.clk.rightNumber(self.clk.min())) == 3:
            self.minuteright.harom(self.minuteright.turtle)

        if (self.clk.rightNumber(self.clk.min())) == 4:
            self.minuteright.negy(self.minuteright.turtle)

        if (self.clk.rightNumber(self.clk.min())) == 5:
            self.minuteright.ot(self.minuteright.turtle)

        if (self.clk.rightNumber(self.clk.min())) == 6:
            self.minuteright.hat(self.minuteright.turtle)

        if (self.clk.rightNumber(self.clk.min())) == 7:
            self.minuteright.het(self.minuteright.turtle)

        if (self.clk.rightNumber(self.clk.min())) == 8:
            self.minuteright.nyolc(self.minuteright.turtle)

        if (self.clk.rightNumber(self.clk.min())) == 9:
            self.minuteright.kilenc(self.minuteright.turtle)

    def masodpercelso(self):
        self.secondright.turtle.clear()
        self.secondleft.turtle.clear()
        if (self.clk.rightNumber(self.clk.sec())) == 0:
            self.secondright.kisnulla(self.secondright.turtle)

        if (self.clk.rightNumber(self.clk.sec())) == 1:
            self.secondright.kisegy(self.secondright.turtle)

        if (self.clk.rightNumber(self.clk.sec())) == 2:
            self.secondright.kisketto(self.secondright.turtle)

        if (self.clk.rightNumber(self.clk.sec())) == 3:
            self.secondright.kisharom(self.secondright.turtle)

        if (self.clk.rightNumber(self.clk.sec())) == 4:
            self.secondright.kisnegy(self.secondright.turtle)

        if (self.clk.rightNumber(self.clk.sec())) == 5:
            self.secondright.kisot(self.secondright.turtle)

        if (self.clk.rightNumber(self.clk.sec())) == 6:
            self.secondright.kishat(self.secondright.turtle)

        if (self.clk.rightNumber(self.clk.sec())) == 7:
            self.secondright.kishet(self.secondright.turtle)

        if (self.clk.rightNumber(self.clk.sec())) == 8:
            self.secondright.kisnyolc(self.secondright.turtle)

        if (self.clk.rightNumber(self.clk.sec())) == 9:
            self.secondright.kiskilenc(self.secondright.turtle)

    def masodpercutolso(self):
        if (self.clk.leftNumber(self.clk.sec())) == 0:
            self.secondleft.kisnulla(self.secondleft.turtle)

        if (self.clk.leftNumber(self.clk.sec())) == 1:
            self.secondleft.kisegy(self.secondleft.turtle)

        if (self.clk.leftNumber(self.clk.sec())) == 2:
            self.secondleft.kisketto(self.secondleft.turtle)

        if (self.clk.leftNumber(self.clk.sec())) == 3:
            self.secondleft.kisharom(self.secondleft.turtle)

        if (self.clk.leftNumber(self.clk.sec())) == 4:
            self.secondleft.kisnegy(self.secondleft.turtle)

        if (self.clk.leftNumber(self.clk.sec())) == 5:
            self.secondleft.kisot(self.secondleft.turtle)

        if (self.clk.leftNumber(self.clk.sec())) == 6:
            self.secondleft.kishat(self.secondleft.turtle)

        if (self.clk.leftNumber(self.clk.sec())) == 7:
            self.secondleft.kishet(self.secondleft.turtle)

        if (self.clk.leftNumber(self.clk.sec())) == 8:
            self.secondleft.kisnyolc(self.secondleft.turtle)

        if (self.clk.leftNumber(self.clk.sec())) == 9:
            self.secondleft.kiskilenc(self.secondleft.turtle)



    def printToConsole(self):
        print(str(self.clk.leftNumber(self.clk.hour24())) + str(self.clk.rightNumber(self.clk.hour24())) + ":" + (str(self.clk.leftNumber(self.clk.min())) + str(self.clk.rightNumber(self.clk.min()))) + ":" + (str(self.clk.leftNumber(self.clk.sec())) + str(self.clk.rightNumber(self.clk.sec()))))
        pass

    def writeSec(self):
        self.printToConsole()
        self.emeraldka()
        self.emeraldkaketto()
        self.oraelso()
        self.orautolso()
        self.percelso()
        self.percutolso()
        self.masodpercelso()
        self.masodpercutolso()


