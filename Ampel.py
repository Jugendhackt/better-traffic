from tkinter import *
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

    size = 30
    xord = 0
    yord = 0
    xvel = 0
    yvel = 0
    gfx  = None

    def __init__(self, x, y, c):
        self.xord = x
        self.yord = y
        self.gfx  = c.create_rectangle(x, y, x + self.size, y + self.size, fill="blue")

    def accelerate(self, x, y):
        self.xvel += x
        self.yvel += y

    def drive(self):
        self.xord += self.xvel
        self.yord += self.yvel

    def draw(self, c):
        c.coords(self.gfx, self.xord, self.yord, self.xord + self.size, self.yord + self.size)

class Ampel:
    size = 30
    xord = 0
    yord = 0
    circle = None

    def __init__(self, x, y, f, c):
        self.xord = x
        self.yord = y
        self.circle = c.create_oval(x - (self.size / 2), y - (self.size / 2), x + (self.size / 2), y + (self.size / 2), fill = f)
        

    def Ampelfarbe(self, farbe):
        pass
        
    
    
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

def bewegeAutos():
    for i in range(len(Autoliste)):
        Autoliste[i].drive()
        Autoliste[i].draw(c)
    window.update()

def aenderAmpel(Farbe, Ampelgrafik):
    c.itemconfig(Ampelgrafik, fill = Farbe)

Strasse1 = c.create_line(500, 0, 500, 800)
Strasse2 = c.create_line(0, 400, 1000, 400)

A = Ampel(600, 500, "green", c)
Ampelliste.append(A)
A = Ampel(600, 300, "green", c)
Ampelliste.append(A)
A = Ampel(400, 500, "green", c)
Ampelliste.append(A)
A = Ampel(400, 300, "green", c)
Ampelliste.append(A)

erstelleAuto("oben")
erstelleAuto("unten")
erstelleAuto("rechts")
erstelleAuto("links")

window.update()

for i in range(0, 100, 1):
    bewegeAutos()
    sleep(0.05)




        






