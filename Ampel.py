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
def erstelleAuto(x, y):
    Autografik = c.create_rectangle(x-15, y-15, x+15, y+15, fill="blue")
    Autoliste.append(Autografik)
def bewegeAuto(Auto):
    pass
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
erstelleAuto(300, 300)
window.update()


        






