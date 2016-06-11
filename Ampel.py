from tkinter import *
from random import randint
from time import sleep, time
from math import pi, atan2


HEIGHT = 800
WIDTH = 1200
window = Tk()
window.title("Ampelsimulator")
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
def erstelleAuto(x, y, Richtung):
    a = Auto(x, y, c)
    
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
Strasse1 = c.create_line(0, HEIGHT/2, WIDTH/4, HEIGHT/2)
Strasse2 = c.create_line(WIDTH/4, HEIGHT*1/4, WIDTH/4, HEIGHT*3/4)
Strasse3 = c.create_line(WIDTH/4, HEIGHT*1/4, WIDTH*3/4, HEIGHT*1/4)
Strasse4 = c.create_line(WIDTH/4, HEIGHT*3/4, WIDTH*3/4, HEIGHT*3/4)
Strasse5 = c.create_line(WIDTH*3/4, HEIGHT*1/4, WIDTH*3/4, HEIGHT*3/4)
Strasse1 = c.create_line(WIDTH*3/4, HEIGHT/2, WIDTH, HEIGHT/2)


#Ampelliste.append(Ampel(515, 500, "green", c))
#Ampelliste.append(Ampel(600, 385, "green", c))
#Ampelliste.append(Ampel(400, 415, "green", c))
#Ampelliste.append(Ampel(485, 300, "green", c))


window.update()

for i in range(0, 1500, 1):
    bewegeAutos()
    sleep(0.02)




        






