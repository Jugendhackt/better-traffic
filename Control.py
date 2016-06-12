worldTime = 0
step = 0


def nothing():
    pass

def nextStep():
    global step
    if step == 0 :
        StepButton.config(command = nothing)
        Animation1()
        StepButton.config(command = nextStep)
    elif step == 1  :
        StepButton.config(command = nothing)
        Animation2()
        StepButton.config(command = nextStep)
    elif step == 2 :
        StepButton.config(command = nothing)
        Animation3()
        StepButton.config(command = nextStep)

tickLabel = Label(window, text = str(step))
tickLabel.place(x = 25, y = 100, width = 75, height = 25)

StepButton = Button(window, text = "Next", command = nextStep)
StepButton.place(x = 25, y = 50, width = 75, height = 25)





    
def Animation1():
    global worldTime
    global step
    worldTime = worldTime * 0
    step += 1
    for i in range(0, 600, 1):
        worldTime += 1
        tickLabel.config(text = str(worldTime))
    Autoliste = list()
    
def Animation2():
    global worldTime
    global step
    worldTime = worldTime * 0
    tickLabel.config(text = str(worldTime))
    step += 1
    for i in range(0, 3016, 1):
        worldTime += 1
        tickLabel.config(text = str(worldTime))      
    
window.mainloop()
