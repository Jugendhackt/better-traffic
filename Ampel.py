from Tkinter import *
from random import randint
from time import sleep, time
from math import pi, atan2


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
def directionallyv(xv, yv, s):
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



class Auto:

    # local variables of the car
    size = 30
    xord = 0
    yord = 0
    xvel = 0
    yvel = 0
    gfx  = None

    # initiating with the upper left coordinate and the canvas
    def __init__(self, x, y, c):
        self.xord = x
        self.yord = y
        self.gfx  = c.create_rectangle(x, y, x + self.size, y + self.size, fill="blue")

    # accelerating the car in this direction
    def accelerate(self, x, y):
        self.xvel += x
        self.yvel += y

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
def erstelleAuto(Richtung):
    if Richtung == "oben":
        a = Auto(485, 0, c)
        a.accelerate(0, 0.5)
        Autoliste.append(a)
    elif Richtung == "rechts":
        a = Auto(970, 385, c)
        a.accelerate(-0.5, 0)
        Autoliste.append(a)
    elif Richtung == "unten":
        a = Auto(485, 770, c)
        a.accelerate(0, -0.5)
        Autoliste.append(a)
    elif Richtung == "links":
        a = Auto(0, 385, c)
        a.accelerate(0.5, 0)
        Autoliste.append(a)
    window.update()
    Autorichtung.append(Richtung)

# moving all the prior created cars and redraws them
def bewegeAutos():
    for i in range(len(Autoliste)):
        Autoliste[i].drive()
        Autoliste[i].draw(c)
    window.update()


class Ampel:
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

    def setAmpelfarbe(self, farbe, c):
        c.itemconfig(circ, fill=farbe)
        self.farb = farbe

    def getAmpelfarbe(self):
        return self.farb


# debugging world
Strasse1 = c.create_line(500, 0, 500, 800)
Strasse2 = c.create_line(0, 400, 1000, 400)

erstelleAuto("oben")
erstelleAuto("unten")
erstelleAuto("rechts")
erstelleAuto("links")

Ampelliste.append(Ampel(600, 500, "green", c))
Ampelliste.append(Ampel(600, 300, "green", c))
Ampelliste.append(Ampel(400, 500, "green", c))
Ampelliste.append(Ampel(400, 300, "green", c))


window.update()

for i in range(0, 1500, 1):
    bewegeAutos()
    sleep(0.02)







