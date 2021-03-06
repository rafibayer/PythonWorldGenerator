from tkinter import *
import tkinter as tk

class Tile(tk.Frame):

    # Tile object, frame with child widgets
    # Inherits from tk.Frame
    # requires parent (master)
    def __init__(self, parent, *args, **kwargs):
        super(Tile, self).__init__(parent)

        # Label 
        Label(self, text="Name:").grid(row=0, column=0)
        self.name = Entry(self)
        self.name.grid(row=0, column=1)
        self.name.insert(END, 'Name')


        # RGB value entries
        Label(self, text="RGB").grid(row=2, column=0)

        self.r = Entry(self)
        self.r.grid(row=2, column=1)
        self.r.insert(END, '255')

        self.g = Entry(self)
        self.g.grid(row=2, column=2)
        self.g.insert(END, '255')

        self.b = Entry(self)
        self.b.grid(row=2, column=3)
        self.b.insert(END, '255')

    
        # height entry
        Label(self, text="Maximum Height").grid(row=3, column=0)
        self.h = Entry(self)
        self.h.grid(row=3, column=1)
        self.h.insert(END, '0')

        # close button
        self.close = Button(self, text="[X]")
        self.close.grid(row=3, column=2)
        self.close.bind("<Button-1>", self.remove)

    # deletes this tile
    def remove(self, Event):
        self.destroy()

    # returns the RGB color as a 3x1 list for this tile
    def getColor(self):
        color = []
        color.append(int(self.r.get()))
        color.append(int(self.g.get()))
        color.append(int(self.b.get()))
        return color

    # returns the max height for this tile
    def getHeight(self):
        return float(self.h.get())
        