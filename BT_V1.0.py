from Tkinter import *
from random import randint
from time import sleep, time
from math import *

worldTime = 0
step = 0

HEIGHT = 800
WIDTH = 1000
window = Tk()
window.title("Ampelsimulater")
c = Canvas(window, width=WIDTH, height=HEIGHT, bg ="white")
c.pack()


Ampelliste = list()
Autoliste = list()


# adjusting for the direction with the size
def directionally(xv, yv, s):
    d = atan2(xv, yv)
    if   d == 0    : 
        return (xv - s /2, yv)
    elif d == pi/2 : 
        return (xv, yv + s /2)
    elif d == pi   : 
        return (xv + s /2, yv)
    elif d == -pi  : 
        return (xv + s /2, yv) 
    elif d == -pi/2: 
        return (xv, yv - s /2)
    else: return (xv, yv)



class Auto(object):

    # local variables of the car
    size = 30
    xord = 0
    yord = 0
    xvel = 0
    yvel = 0
    gfx  = None
    dire = None
    driv = True

    # initiating with the upper left coordinate and the canvas
    def __init__(self, x, y, c, color="blue"):
        self.xord = x
        self.yord = y
        self.gfx  = c.create_rectangle(x, y, x + self.size, y + self.size, fill=color)

    # returns the current position of the car
    def getPosition(self):
        return (xord, yord)

    # accelerating the car in this direction
    def accelerate(self, x, y):
        self.xvel += x
        self.yvel += y

    # absolutely stops the car
    def stop(self):
        self.driv = False
        self.dire = (self.xvel, self.yvel)
        self.xvel = 0
        self.yvel = 0

    def go(self):
        self.driv = True
        self.xvel, self.yvel = self.dire

    # letting the car drive
    def drive(self):
        self.xord += self.xvel
        self.yord += self.yvel

    # drawing the car on the canvas
    def draw(self, c):
        if self.driv:
            (xa, ya) = directionally(self.xvel, self.yvel, self.size)
            nxord = self.xord + xa
            nyord = self.yord + ya
            c.coords(self.gfx, nxord, nyord, nxord + self.size, nyord + self.size)

"""
    def setColor(self, color, canv):
        self.setInv(canv)
        self.gfx = canv.create_rectangle(x, y, x + self.size, y + self.size, fill=color)
    def setInv(self, c):
        self.driv = True
        self = Auto(- 3000, -3000, c)
        self.draw(c)
        self.driv = False
"""


# creates a car, in possibly one of the four directions:
#   "oben", "rechts", "unten", "links"
def erstelleAuto(x, y, Richtung, color="blue"):
    a  = Auto(x,y,c, color)
    if Richtung == "oben":
        a.accelerate(0, 0.5)
    elif Richtung == "rechts":
        a.accelerate(-0.5, 0)
    elif Richtung == "unten":
        a.accelerate(0, -0.5)
    elif Richtung == "links":
        a.accelerate(0.5, 0)
    Autoliste.append(a)
    window.update()
    return Autoliste[len(Autoliste) -1]


def createUp():
    return erstelleAuto(485, 0, "oben")

def createRight():
    return erstelleAuto(970, 385, "rechts")

def createLeft():
    return erstelleAuto(0, 385, "links")

def createDown():
    return erstelleAuto(485, 770, "unten")

def createUpNSF():
    return erstelleAuto(485, 0, "oben", "yellow")

def createRightNSF():
    return erstelleAuto(970, 385, "rechts", "yellow")

def createLeftNSF():
    return erstelleAuto(0, 385, "links", "yellow")

def createDownNSF():
    return erstelleAuto(485, 770, "unten", "yellow")



class Ampel(object):
    size = 30
    xord = 0
    yord = 0
    farb = "rot"
    circ = None

    # initializing the Ampel at given coordinates with fill (=f) on the canvas (=c)
    def __init__(self, x, y, f, c):
        self.xord = x
        self.yord = y
        self.circ = c.create_oval(x - (self.size / 2), y - (self.size / 2), x + (self.size / 2), y + (self.size / 2), fill = f)

    # setting the color of the Ampel and drawing it on the canvas
    def setAmpelfarbe(self, farbe, c):
        c.itemconfig(self.circ, fill=farbe)
        self.farb = farbe

    # returns the current state or color of the Ampel
    def getAmpelfarbe(self):
        return self.farb

    def change(self, c):
        if self.farb == "green":
            self.setAmpelfarbe("red", c)
        if self.farb == "red":
            self.setAmpelfarbe("green", c)


# debugging world
Strasse1 = c.create_line(500, 0, 500, 800)
Strasse2 = c.create_line(0, 400, 1000, 400)

Ampel1 = Ampel(515, 470, "red", c)
Ampelliste.append(Ampel1)

Ampel4 = Ampel(570, 385, "red", c)
Ampelliste.append(Ampel4)

Ampel3 = Ampel(430, 415, "red", c)
Ampelliste.append(Ampel3)

Ampel2 = Ampel(485, 330, "red", c)
Ampelliste.append(Ampel2)



window.update()


CreateCarButton = Button(window, text = "Create", command = createRight)
CreateCarButton.place(x = 25, y = 50, width = 75, height = 25)



# moving all the prior created cars and redraws them, as well as redraws the Ampels ... ?
def loop(tick):
    for auto in Autoliste:
        auto.drive()
        auto.draw(c)
#    for ampel in Ampelliste:
#        ampel.draw(c)
    window.update()

def nothing():
    pass

def nextStep():
    global step
    if step == 0 :
        StepButton.config(command = nothing)
        Animation1()
        StepButton.config(command = nextStep)
    elif step == 1  :
        StepButton.config(command = nothing)
        Animation2()
        StepButton.config(command = nextStep)
    elif step == 2 :
        StepButton.config(command = nothing)
        Animation3()
        StepButton.config(command = nextStep)

tickLabel = Label(window, text = str(worldTime))
tickLabel.place(x = 25, y = 100, width = 75, height = 25)

stepLabel = Label(window, text = str(step))
stepLabel.place(x = 25, y = 150, width = 75, height = 25)

StepButton = Button(window, text = "Next", command = nextStep)
StepButton.place(x = 25, y = 50, width = 75, height = 25)

def Animation1():
    global worldTime
    global step
    worldTime = worldTime * 0
    step += 1
    createLeft()
    for i in range(0, 2016):
        loop(i)
        sleep(0.0042)
        if i == 600:
            Ampel3.setAmpelfarbe("green", c)
        if i == 1008:
            Ampel3.setAmpelfarbe("red", c)
        worldTime += 1
        tickLabel.config(text = str(worldTime))
        stepLabel.config(text = str(step))
    Autoliste = list()


def Animation2():
    global worldTime
    global step
    worldTime = worldTime * 0
    step += 1
    begin2 = 230
    r = createRight()
    for i in range(0, 2800):
        if i == begin2 + 30:
            createDown()
        if i == begin2 + 120:
            createDown()
        if i == begin2 + 210:
            createDown()
        if i == 700:
            r.stop()
            Ampel1.setAmpelfarbe("green", c)
        if i == 1200:
            Ampel1.setAmpelfarbe("red", c)
            Ampel4.setAmpelfarbe("green", c)
            r.go()
        if i == 1500:
            Ampel4.setAmpelfarbe("red", c)
        loop(i)
        sleep(0.0042)
        worldTime += 1
        tickLabel.config(text = str(worldTime))
        stepLabel.config(text = str(step))
    Autoliste = list()


def Animation3():
    global worldTime
    global step
    worldTime = worldTime * 0
    step += 1
    begin3 = 230
    r = createRightNSF()
    for i in range(0, 2700):
        if i == begin3:
            createUp()
        if i == 700:
            r.stop()
            Ampel2.setAmpelfarbe("green", c)
        if i == 1200:
            r.go()
            Ampel2.setAmpelfarbe("red", c)
            Ampel4.setAmpelfarbe("green", c)
        if i == 1500:
            Ampel4.setAmpelfarbe("red", c)
        loop(i)
        sleep(0.0042)
        worldTime += 1
        tickLabel.config(text = str(worldTime))
        stepLabel.config(text = str(step))
    Autoliste = list()
    pass
window.mainloop()
