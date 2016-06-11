from Tkinter import *
from random import randint
from time import sleep, time
from math import *


HEIGHT = 800
WIDTH = 1000
window = Tk()
window.title("Ampelsimulater")
c = Canvas(window, width=WIDTH, height=HEIGHT, bg ="white")
c.pack()


Ampelliste = list()
Autoliste = list()
Autorichtung = list()


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

    # initiating with the upper left coordinate and the canvas
    def __init__(self, x, y, c):
        self.xord = x
        self.yord = y
        self.gfx  = c.create_rectangle(x, y, x + self.size, y + self.size, fill="blue")

    # returns the current position of the car
    def getPosition(self):
        return (xord, yord)

    # accelerating the car in this direction
    def accelerate(self, x, y):
        self.xvel += x
        self.yvel += y

    # absolutely stops the car
    def stop(self):
        self.dire = (self.xvel, self.yvel)
        self.xvel = 0
        self.yvel = 0

    def go(self):
        self.xvel, self.yvel = self.dire

    # letting the car drive
    def drive(self):
        self.xord += self.xvel
        self.yord += self.yvel

    # drawing the car on the canvas
    def draw(self, c):
        (xa, ya) = directionally(self.xvel, self.yvel, self.size)
        nxord = self.xord + xa
        nyord = self.yord + ya
        c.coords(self.gfx, nxord, nyord, nxord + self.size, nyord + self.size)


# creates a car, in possibly one of the four directions:
#   "oben", "rechts", "unten", "links"
def erstelleAuto(x, y, Richtung):
    a  = Auto(x,y,c)
    if Richtung == "oben":
        a.accelerate(0, 5)
    elif Richtung == "rechts":
        a.accelerate(-5, 0)
    elif Richtung == "unten":
        a.accelerate(0, -5)
    elif Richtung == "links":
        a.accelerate(5, 0)
    Autoliste.append(a)
    window.update()


def createUp():
    erstelleAuto(485, 0, "oben")

def createRight():
    erstelleAuto(970, 385, "rechts")

def createLeft():
    erstelleAuto(0, 385, "links")

def createDown():
    erstelleAuto(485, 770, "unten")


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
def loop():
    for auto in Autoliste:
        auto.drive()
        auto.draw(c)
#    for ampel in Ampelliste:
#        ampel.draw(c)
    window.update()


Ampel4.setAmpelfarbe("green", c)

createRight()



for i in range(0, 1500, 1):
    loop()
    sleep(0.05)

def nextStep():
    if step == 0:

    if step == 1:

    if step == 2:

def Animation1():
    
    pass
def Animation2():
    pass
def Animation3():
    pass
                
    
    
