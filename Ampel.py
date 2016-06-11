from Tkinter import *
from random import randint
from time import sleep, time
from math import *


DEBUG = False


HEIGHT = 800
WIDTH = 1000
window = Tk()
window.title("Ampelsimulater")
c = Canvas(window, width=WIDTH, height=HEIGHT, bg ="white")
c.pack()

Ampelliste = list()
Autoliste = list()
Autorichtung = list()

magicEvents = list()
magicPoints = list()

class Events:
    TurnRight, TurnLeft, LightStop, LightGo, StopCar, GoCar = range(6)

class MagicEvent(object):
    size  = 30
    xord  = 0
    yord  = 0
    event = None

    # initializing the derived object
    def __init__(self):
        magicEvents.append(self)

    def getEvent(self):
        return event

    def setEvent(self, e):
        self.event = e

    def getPos(self):
        return (self.xord, self.yord)

    # basically a simply virtual function
    def eventHappening(self, event):
        pass


class MagicPoint(object):
    xloc = 0
    yloc = 0
    aref = None


    def __init__(self, ref):
        magicPoints.append(self)
        self.aref = ref

    def eventHappening(self, event):
        self.aref.eventHappening(event)

    # moving this MagicPoint
    def move(self, x, y):
        self.xloc += x
        self.yloc += y

    # setting the location of this MagicPoint
    def setPosition(self, x, y):
        if DEBUG: print "set position of MP to %d %d" % (x, y)
        self.xloc = x
        self.yloc = y

    # returns the current position of the MagicPoint
    def getPosition(self):
        return (self.xloc, self.yloc)

    # checking if the point is within an event-trigger
    def checkForEvent(self):
        if DEBUG: print "-- -- Magic Point at x:" + str(self.xloc) + " y:" + str(self.yloc)
        for e in magicEvents:
            (ex, ey) = e.getPos()
            if DEBUG: print "Magic Event at x:" + str(ex) + " y:" + str(ey)
            if  (self.xloc + 8  >= ex) \
              & (self.xloc - 8  <= ex) \
              & (self.yloc + 8  >= ey) \
              & (self.yloc - 8  <= ey):
                  if DEBUG: print "Event triggered"
                  self.eventHappening(e.getEvent())
                  pass
        self.eventHappening(Events.GoCar)



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

    # local variables of the car
    size = 30
    xord = 0
    yord = 0
    xvel = 0
    yvel = 0
    gfx  = None
    mpoi = None
    dire = None
    leve = Events.GoCar

    # initiating with the upper left coordinate and the canvas
    def __init__(self, x, y, c):
        super(Auto, self).__init__()
        self.xord = x
        self.yord = y
        self.gfx  = c.create_rectangle(x, y, x + self.size, y + self.size, fill="blue")
        self.setEvent(Events.StopCar)
        self.mpoi = MagicPoint(self)

    # returns the current position of the car
    def getPosition(self):
        return (self.xord, self.yord)

    # accelerating the car in this direction
    def accelerate(self, x, y):
        self.xvel += x
        self.yvel += y

    # absolutely stops the car and saves previous speed
    def stop(self):
        if DEBUG: print "Stopping Car."
        self.dire = (self.xvel, self.yvel)
        self.xvel = 0
        self.yvel = 0

    def go(self):
        if DEBUG: print "restarted Car."
        self.xvel, self.yvel = self.dire

    # letting the car drive
    def drive(self):
        if (self.leve == Events.LightStop) | (self.leve == Events.StopCar):
            pass
        else:
            self.xord += self.xvel
            self.yord += self.yvel
            if (self.xvel != 0) | (self.yvel != 0):
                self.mpoi.setPosition(self.xord + 3 * self.xvel, self.yord + 3 * self.yvel)
                if DEBUG: print "New MP-Position: %d %d" % (self.xord + 3 * self.xvel, self.yord + 3 * self.yvel)

    # drawing the car on the canvas
    def draw(self, c):
        (xa, ya) = directionally(self.xvel, self.yvel, self.size)
        nxord = self.xord + xa
        nyord = self.yord + ya
        c.coords(self.gfx, nxord, nyord, nxord + self.size, nyord + self.size)

    # In case an event got triggered
    def eventHappening(self, event):
        if (event == Events.LightStop) | (event == Events.StopCar):
            if DEBUG: print "gotta stop car"
            self.stop()
        elif event == Events.LightGo:
            if DEBUG: print "gotta restart car"
            self.go()
        elif event == Events.TurnLeft:
            pass
        elif event == Events.TurnRight:
            pass
        elif event == Events.GoCar:
            pass
        # else:
        #     event = Events.GoCar
        self.leve = event
        if DEBUG: print "Event happened: " + str(event)


    def getEvent(self):
        return Events.StopCar



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
    Autorichtung.append(Richtung)


def create():
    if DEBUG: print "create car on the right side"
    erstelleAuto(970, 385, "rechts")




class Ampel(MagicEvent):
    size = 30
    xord = 0
    yord = 0
    farb = "rot"
    circ = None

    # initializing the Ampel at given coordinates with fill (=f) on the canvas (=c)
    def __init__(self, x, y, f, c):
        super(Ampel, self).__init__()
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

    def draw(self, c):
        c.move(self.circ, 0, 0)
        window.update()

    # returns the event currently being triggered from this light
    def getEvent(self):
        return Events.LightStop + self.isPassable()


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


Ampelliste.append(Ampel(515, 500, "green", c))
Ampelliste.append(Ampel(600, 385, "green", c))
Ampelliste.append(Ampel(400, 415, "green", c))
Ampelliste.append(Ampel(485, 300, "green", c))
"""

Strasse1 = c.create_line(0, HEIGHT/2, WIDTH/4, HEIGHT/2)
Strasse2 = c.create_line(WIDTH/4, HEIGHT*1/4, WIDTH/4, HEIGHT*3/4)
Strasse3 = c.create_line(WIDTH/4, HEIGHT*1/4, WIDTH*3/4, HEIGHT*1/4)
Strasse4 = c.create_line(WIDTH/4, HEIGHT*3/4, WIDTH*3/4, HEIGHT*3/4)
Strasse5 = c.create_line(WIDTH*3/4, HEIGHT*1/4, WIDTH*3/4, HEIGHT*3/4)
Strasse6 = c.create_line(WIDTH*3/4, HEIGHT/2, WIDTH, HEIGHT/2)



window.update()

CreateCarButton = Button(window, text = "Create", command = create)
CreateCarButton.place(x = 25, y = 50, width = 75, height = 25)


# moving all the prior created cars and redraws them, as well as redraws the Ampels ... ?
def loop(tick):
    if DEBUG: print "--- --- ---   --- ---- Tick " + str(tick)
    for auto in Autoliste:
        auto.drive()
        auto.draw(c)
    for ampel in Ampelliste:
        ampel.draw(c)
    if DEBUG: print "amount of magic points: " + str(len(magicPoints))
    if DEBUG: print "amount of magic events: " + str(len(magicEvents))
    for point in magicPoints:
        point.checkForEvent()
    window.update()




for i in range(0, 1500, 1):
    loop(i)
    sleep(0.04)










