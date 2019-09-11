import terrainGen
from tkinter import *
from PIL import Image, ImageTk

image = None

root = Tk()
root.title("Terrain Generator")
controls = Frame(root, height = 400, width = 300)
controls.grid(row=0, column=0, sticky=NW)

display = Label(root)
display.grid(row=0, column=1, sticky=NW)

button = Button(controls, text="Create Terrain")
button.grid(row=0, column=0, sticky=NW)

def updateImage(terrain):
    img = ImageTk.PhotoImage(image=Image.fromarray(terrain))
    global image
    image = img
    display.config(image=image)

def regenerateTerrain(Event):
    updateImage(terrainGen.generateTerrain(300, 300, 100, 25, 0.5, 2))

regenerateTerrain(None) # create initial terrain

button.bind("<Button-1>", regenerateTerrain)


root.mainloop()