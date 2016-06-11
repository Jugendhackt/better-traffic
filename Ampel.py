from Tkinter import *
from random import randint
from time import sleep, time
from math import *

global WorldTime;
WorldTime = 0;

HEIGHT = 800
WIDTH = 1000
window = Tk()
window.title("Ampelsimulater")
c = Canvas(window, width=WIDTH, height=HEIGHT, bg ="white")
c.pack()

Ampelliste = list()
Autoliste = list()
Autorichtung = list()
Ampel1 = list()
Ampel2 = list()

magicEvents = list()

class Events:
    TurnRight, TurnLeft, LightStop, LightGo, StopCar, GoCar = range(6)

class MagicEvent:
    size  = 30
    xord  = 0
    yord  = 0
    event = None

    def __init__(self):
        magicEvents.append(self)
        pass

    def getEvent(self):
        return event

    def setEvent(self, e):
        self.event = e

    def getPos(self):
        return (xord, yord)


class MagicPoint:
    xloc = 0
    yloc = 0

    def __init__(self):
        pass

    def eventHappening(event):
        pass

    # moving this MagicPoint
    def move(self, x, y):
        self.xloc += x
        self.yloc += y

    # setting the location of this MagicPoint
    def setPoint(self, x, y):
        self.xloc = x
        self.yloc = y

    # returns the current position of the MagicPoint
    def getPosition(self):
        return (self.xloc, self.yloc)

    # checking if the point is within an event-trigger
    def checkForEvent(self):
        for e in magicEvents:
            (ex, ey) = e.getPos()
            if  self.xloc + 7  >= ex \
              & self.xloc - 7  <= ex \
              & self.yloc + 7  >= ey \
              & self.yloc - 7  <= ey:
                eventHappening(e.getEvent())



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



class Auto(MagicEvent):

    global WorldTime

    # local variables of the car
    size = 30
    xord = 0
    yord = 0
    xvel = 0
    yvel = 0
    way = 1
    ctime = WorldTime
    atime = ctime + 400
    gfx  = None
    mpoi = list()
    dire = None

    # initiating with the upper left coordinate and the canvas
    def __init__(self, x, y, c):
        self.xord = x
        self.yord = y
        self.gfx  = c.create_rectangle(x, y, x + self.size, y + self.size, fill="blue")
        self.setEvent(Events.StopCar)
        p = MagicPoint()
        self.mpoi.append(p)

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

    # In case an event got triggered
    def eventHappening(event):
        if event == Events.LightStop | event == Events.StopCar:
            self.stop()
        if event == Events.LightGo:
            self.accelerate(0,-5)

    def searchWay(self):
        aaa1 = 0
        aaa2 = 0
        for auto in Ampel1:
            if auto.ctime == self.ctime  & auto.ctime == self.ctime :
                aaa1 += 1
        for auto in Ampel2:
             if auto.ctime == self.ctime - 10 & auto.ctime == self.ctime + 10:
                aaa2 += 1
                
        if aaa1 == 0:
            self.way = 1
        elif aaa2 == 0:
            self.way = 2
        elif aaa1 < aaa2:
            self.way = 1
        elif aaa1 > aaa2:
            self.way = 2
        elif aaa1 == aaa2:
            self.way = 1

# creates a car, in possibly one of the four directions:
#   "oben", "rechts", "unten", "links"
def erstelleAuto(x, y, Richtung):
    a  = Auto(x,y,c)
    a.searchWay()
    if a.way == 1:
        Ampel1.append(a)
    else:
        Ampel2.append(a)
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
    Autorichtung.append(Richtung)


# moving all the prior created cars and redraws them, as well as redraws the Ampels ... ?
def bewegeAutos():
    for auto in Autoliste:
        auto.drive()
        auto.draw(c)
    """
    for ampel in Ampelliste:
        ampel.draw(c)
    """
    window.update()



class Ampel(MagicEvent):
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

    def isPassable(self):
        return self.farb == "green"
    """
    def draw(self, c):
        c.move(self.circ, 0, 0)
        window.update()
    """

    # returns the event currently being triggered from this light
    def getEvent(self):
        return Events.LightStop + self.isPassable()

def aendereAmpelFarbe():
    for Ampel in Ampelliste:
        if Ampel.xord == 515:
            if Ampel.getAmpelfarbe() == "green":
                Ampel.setAmpelfarbe("red", c)
            else:
                Ampel.setAmpelfarbe("green", c)


"""
# debugging world
Strasse1 = c.create_line(500, 0, 500, 800)
Strasse2 = c.create_line(0, 400, 1000, 400)
"""

"""
erstelleAuto("oben")
erstelleAuto("unten")
erstelleAuto("rechts")
erstelleAuto("links")
"""

global clockCreate
clockCreate = 0

def create():
    global clockCreate
    if clockCreate == 0:
        erstelleAuto(50 ,300,"links")
        clockCreate = 10

Ampelliste.append(Ampel(515, 500, "green", c))
Ampelliste.append(Ampel(600, 385, "green", c))
Ampelliste.append(Ampel(400, 415, "green", c))
Ampelliste.append(Ampel(485, 300, "green", c))


Strasse1 = c.create_line(0, HEIGHT/2, WIDTH/4, HEIGHT/2)
Strasse2 = c.create_line(WIDTH/4, HEIGHT*1/4, WIDTH/4, HEIGHT*3/4)
Strasse3 = c.create_line(WIDTH/4, HEIGHT*1/4, WIDTH*3/4, HEIGHT*1/4)
Strasse4 = c.create_line(WIDTH/4, HEIGHT*3/4, WIDTH*3/4, HEIGHT*3/4)
Strasse5 = c.create_line(WIDTH*3/4, HEIGHT*1/4, WIDTH*3/4, HEIGHT*3/4)
Strasse6 = c.create_line(WIDTH*3/4, HEIGHT/2, WIDTH, HEIGHT/2)



window.update()

CreateCarButton = Button(window, text = "Create", command = create)
CreateCarButton.place(x = 25, y = 50, width = 75, height = 25)

clockAmpel = 0;

for i in range(0, 1500, 1):
    global clockCreate
    global WorldTime
    bewegeAutos()
    
    if clockAmpel == 50:
        aendereAmpelFarbe()
        clockAmpel = 0

    else:
        clockAmpel += 1
    if clockCreate >= 1:
        clockCreate -= 1
    for auto in Autoliste:
        if auto.xord == 200:
            if auto.way == 1:
                auto.stop()
                auto.accelerate(0, 5)
            else:
                auto.stop()
                auto.accelerate(0, -5)
  
    WorldTime += 1
    sleep(0.04)


                

    
