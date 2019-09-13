import terrainGen
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from tile import Tile
image = None
image_data = None

# root
root = Tk()
root.title("Terrain Generator")

# tiles
def presetTile(height, color, name):
    t = Tile(tiles)
    t.r.delete(0, 'end')
    t.g.delete(0, 'end')
    t.b.delete(0, 'end')

    t.r.insert(END, color[0])
    t.g.insert(END, color[1])
    t.b.insert(END, color[2])

    t.h.delete(0, 'end')
    t.h.insert(0, height)

    t.name.delete(0, 'end')
    t.name.insert(0, name)
    return t

tiles = Frame(root, width = 500, height=250)
tiles.grid(row = 1, column=0, rowspan=1)
addTileButton = Button(tiles, width = 20, text="Create Tile")
addTileButton.grid()

# default tiles
presetTile(-0.2, [0, 0, 153], "Deep Sea").grid() # deep sea
presetTile(-0.05, [0, 102, 255], "Sea").grid() # sea
presetTile(0, [0, 120, 255],"Shallow water").grid() # shallows
presetTile(0.04, [237, 201, 175],"Beach").grid() # beach
presetTile(0.25, [96, 128, 56],"Grasslands").grid() # grass
presetTile(0.3, [70, 105, 56],"Jungle").grid() # jung;e
presetTile(0.4, [102, 102, 102],"Rocks").grid() # rocks
presetTile(2, [255, 255, 255],"Snow").grid() # snow


# App Controls
controls = Frame(root)
controls.grid(row=0, column=0, sticky=NW)


genButton = Button(controls, width = 20, text="Create Terrain")
genButton.grid(row=0, column=0, columnspan = 2, sticky=NW)

saveButton = Button(controls, width = 20, text="Save Image")
saveButton.grid(row=1, column=0, columnspan = 2, sticky=NW)

# Terrain Controls
widthLabel = Label(controls, width=10, text="Width: ")
widthLabel.grid(row=2, column=0)
widthEntry = Entry(controls, width=10)
widthEntry.grid(row=2, column=1)
widthEntry.insert(END, '100')

heightLabel = Label(controls, width=10, text="Height: ")
heightLabel.grid(row=3, column=0)
heightEntry = Entry(controls, width=10)
heightEntry.grid(row=3, column=1)
heightEntry.insert(END, '100')

scaleLabel = Label(controls, width=10, text="World Scale: ")
scaleLabel.grid(row=4, column=0)
scaleEntry = Entry(controls, width=10)
scaleEntry.grid(row=4, column=1)
scaleEntry.insert(END, '100')

octaveLabel = Label(controls, width=10, text="Octaves: ")
octaveLabel.grid(row=5, column=0)
octaveEntry = Entry(controls, width=10)
octaveEntry.grid(row=5, column=1)
octaveEntry.insert(END, '25')

persistenceLabel = Label(controls, width=10, text="Persistence: ")
persistenceLabel.grid(row=6, column=0)
persistenceEntry = Entry(controls, width=10)
persistenceEntry.grid(row=6, column=1)
persistenceEntry.insert(END, '0.5')

lacunarityLabel = Label(controls, width=10, text="Lacunarity: ")
lacunarityLabel.grid(row=7, column=0)
lacunarityEntry = Entry(controls, width=10)
lacunarityEntry.grid(row=7, column=1)
lacunarityEntry.insert(END, '2')

# Display controls
zoomLabel = Label(controls, width=10, text="Image Zoom: ")
zoomLabel.grid(row=8, column=0)
zoomEntry = Entry(controls, width=10)
zoomEntry.grid(row=8, column=1)
zoomEntry.insert(END, '5')

# image display
display = Label(root)
display.grid(row=0, column=2, rowspan=4, columnspan=10, sticky=NW)

# functions

# generate new terrain with parameters from controls and display the new image
def updateImage(terrain):
    global image_data
    image_data = terrain
    size = tuple(int(s * float(zoomEntry.get())) for s in (int(widthEntry.get()), int(heightEntry.get())))
    img = ImageTk.PhotoImage(image=Image.fromarray(terrain).resize(size))
    global image
    image = img
    display.config(image=image)

# gets parameters from controls and calls update image on button press
def regenerateTerrain(Event):
    height = int(heightEntry.get())
    width = int(widthEntry.get())
    scale = float(scaleEntry.get())
    octaves = int(octaveEntry.get())
    persistence = float(persistenceEntry.get())
    lacunarity = float(lacunarityEntry.get())

    updateImage(terrainGen.generateTerrain(height, width, scale, octaves, persistence, lacunarity))

regenerateTerrain(None) # create initial terrain

# opens save prompt and saves the current terrain as a png image
def saveImage(Event):
    global image_data
    img = Image.fromarray(image_data)
    path = filedialog.asksaveasfilename(initialdir = os.getcwd() + "TerrainGenerator", title="save terrain", filetypes=(("PNG files", "*.png"),))
    if path == None:
        return
    if str.lower(path[-4:]) != ".png":
        path += ".png"
    img.save(path, "PNG")


def addTile(Event):
    t = Tile(tiles)
    t.grid()

def tilesToDict(Event):
    allTiles = tiles.winfo_children()
    for t in allTiles[1:]:
        print(t.getHeight())
        print()

tilesToDict(Event)

# bindings
genButton.bind("<Button-1>", regenerateTerrain)
saveButton.bind("<Button-1>", saveImage)
addTileButton.bind("<Button-1>", addTile)

root.mainloop()