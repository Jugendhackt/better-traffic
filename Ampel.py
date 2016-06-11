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
def erstelleAuto(Richtung):
    if Richtung == "oben":
        Autografik = c.create_rectangle(485, 0, 515, 30, fill="blue")
        Autoliste.append(Autografik)
    elif Richtung == "rechts":
        Autografik = c.create_rectangle(970, 385, 1000, 415, fill="blue")
        Autoliste.append(Autografik)
    elif Richtung == "unten":
        Autografik = c.create_rectangle(485, 770, 515, 800, fill="blue")
        Autoliste.append(Autografik)
    elif Richtung == "links":
        Autografik = c.create_rectangle(0, 385, 30, 415, fill="blue")
        Autoliste.append(Autografik)
    window.update()
    Autorichtung.append(Richtung)
def bewegeAutos():
    for i in range(len(Autoliste)):
        if Autorichtung[i] == "oben":
            c.move(Autoliste[i], 0, 5)
        elif Autorichtung[i] == "rechts":
            c.move(Autoliste[i], -5, 0)
        elif Autorichtung[i] == "unten":
            c.move(Autoliste[i], 0, -5)
        elif Autorichtung[i] == "links":
            c.move(Autoliste[i], 5, 0)
        window.update()
def erstelleAmpel(x, y):
    Ampelgrafik = c.create_oval(x-15, y-15, x+15, y+15, fill="red")
    Ampelliste.append(Ampelgrafik)
def aenderAmpel(Farbe, Ampelgrafik):
    c.itemconfig(Ampelgrafik, fill = Farbe)

Strasse1 = c.create_line(500, 0, 500, 800)
Strasse2 = c.create_line(0, 400, 1000, 400)
erstelleAmpel(600, 500)
erstelleAmpel(600, 300)
erstelleAmpel(400, 500)
erstelleAmpel(400, 300)
window.update()

erstelleAuto("oben")
erstelleAuto("unten")
erstelleAuto("rechts")
erstelleAuto("links")

for i in range(0, 100, 1):
    bewegeAutos()
    sleep(0.1)



        






