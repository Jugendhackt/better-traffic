from Tkinter import *
from random import randint
from time import sleep, time
        
global Flag
Flag = 1


def ChangeDirection():
    global Flag
    if Flag == 1:
        DirectionCarShow.config(text="B zu A")
    else:
        DirectionCarShow.config(text="A zu B")
    Flag = -Flag
    
ControlPanel = Tk()
ControlPanel.geometry("300x200")
ControlPanel.title("Control Panel")

CarHeadline = Label(ControlPanel, justify = "center", text = "Create a Car:")
CarHeadline.place(x = 10, y =20, width = 75, height = 25)

HumanHeadline = Label(ControlPanel, justify = "center", text = "Create a Human:")
HumanHeadline.place(x = 190, y = 20, width = 100, height = 25)

DirectionCar = Label(ControlPanel, justify = "center", text = "Direction:")
DirectionCar.place(x = 15, y = 75, width = 50, height = 25)

DirectionHuman= Label(ControlPanel, justify = "center", text = "Direction: Random")
DirectionHuman.place(x = 190, y = 75, width = 100, height = 25)

CarGroup= Label(ControlPanel, justify = "center", text = "Group:")
CarGroup.place(x = 15, y = 130, width = 50, height = 25)

HumanGroup= Label(ControlPanel, justify = "center", text = "Group:")
HumanGroup.place(x = 180, y = 130, width = 50, height = 25)

DirectionCarShow = Label(ControlPanel, justify = "center", text="A zu B")
DirectionCarShow.place(x = 70, y = 75, width = 50, height = 25)




CarGroupSelect = Entry(ControlPanel)
CarGroupSelect.place(x = 75, y = 130, width = 25, height = 25)

HumanGroupSelect = Entry(ControlPanel)
HumanGroupSelect.place(x = 245, y = 130, width = 25, height = 25)





CreateCarButton = Button(ControlPanel, text = "Create", command = <ERSTELLE AUTO>)
CreateCarButton.place(x = 25, y = 50, width = 75, height = 25)

CreateHumanButton = Button(ControlPanel, text = "Create", command = <ERSTELLE MENSCH>)
CreateHumanButton.place(x = 200, y =50, width = 75, height = 25)

ChangeCarDirectionButton = Button(ControlPanel, text = "Change", command = ChangeDirection)
ChangeCarDirectionButton.place(x = 25, y = 100, width = 75, height = 25)



ControlPanel.mainloop()
