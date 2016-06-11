from Tkinter import *
from random import randint
from time import sleep, time
        
HEIGHT = 800
WIDTH = 1000
window = Tk()
window.title("Ampelsimulater")
c = Canvas(window, width=WIDTH, height=HEIGHT, bg ="white")
c.pack()

Ampelliste = list()
Autoliste = list()
Autorichtung = list()


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
        c.coords(self.gfx, self.xord, self.yord, self.xord + self.size, self.yord + self.size)


# creates a car, in possibly one of the four directions:
#   "oben", "rechts", "unten", "links"
def erstelleAuto(Richtung):
    if Richtung == "oben":
        a = Auto(485, 0, c)
        a.accelerate(0, 5)
        Autoliste.append(a)
    elif Richtung == "rechts":
        a = Auto(970, 385, c)
        a.accelerate(-5, 0)
        Autoliste.append(a)
    elif Richtung == "unten":
        a = Auto(485, 770, c)
        a.accelerate(0, -5)
        Autoliste.append(a)
    elif Richtung == "links":
        a = Auto(0, 385, c)
        a.accelerate(5, 0)
        Autoliste.append(a)
    window.update()
    Autorichtung.append(Richtung)

# moving all the prior created cars and redraws them
def bewegeAutos():
    for i in range(len(Autoliste)):
        Autoliste[i].drive()
        Autoliste[i].draw(c)
    window.update()

def erstelleAmpel(x, y):
    Ampelgrafik = c.create_oval(x-15, y-15, x+15, y+15, fill="red")
    Ampelliste.append(Ampelgrafik)

def aenderAmpel(Farbe, Ampelgrafik):
    c.itemconfig(Ampelgrafik, fill = Farbe)



# debugging world
Strasse1 = c.create_line(500, 0, 500, 800)
Strasse2 = c.create_line(0, 400, 1000, 400)
erstelleAmpel(600, 500)
erstelleAmpel(600, 300)
erstelleAmpel(400, 500)
erstelleAmpel(400, 300)

erstelleAuto("oben")
erstelleAuto("unten")
erstelleAuto("rechts")
erstelleAuto("links")

window.update()

for i in range(0, 100, 1):
    bewegeAutos()
    sleep(0.01)







