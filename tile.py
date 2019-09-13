from tkinter import *
import tkinter as tk

class Tile(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super(Tile, self).__init__()


        Label(self, text="RBG").pack()

        # RGB value entries
        self.r = Entry(self)
        self.r.pack()
        self.r.insert(END, '255')

        self.g = Entry(self)
        self.g.pack()
        self.g.insert(END, '255')

        self.b = Entry(self)
        self.b.pack()
        self.b.insert(END, '255')

    
        # height entry
        Label(self, text="Maximum Height").pack()
        self.h = Entry(self)
        self.h.pack()
        self.h.insert(END, '0')

        # close button
        self.close = Button(self, text="[X]")
        self.close.pack()
        self.close.bind("<Button-1>", self.remove)

    # deletes this tile
    def remove(self, Event):
        self.destroy()

    # returns the RGB color as a 3x1 list for this tile
    def getColor(self):
        color = [0,0,0]
        color[0] = int(self.r.get())
        color[1] = int(self.g.get())
        color[2] = int(self.b.get())

        return color

    def getHeight(self):
        return float(self.h.get())
        