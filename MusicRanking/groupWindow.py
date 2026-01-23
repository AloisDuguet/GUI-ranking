import tkinter as tk
from tkinter import ttk

from slideElement import *

class GroupWindow:
    def __init__(self, n):
        self.nSlideElements = n # number of slideElements
        self.root = tk.Tk()
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(n, weight=1)
        self.slideElements = []
        for i in range(n):
            self.slideElements.append(SlideElement(self.root, i))
            self.slideElements[-1].frame.grid(column=0, row=i)
            self.slideElements[-1].position.trace_add('write', self.switchPlace)

    def switchPlace(self, varName, index, mode):
        positionClick = varName.get() # does not work, it is just a name (string?) 
        # I want to access the position but I don't know how
        indexElementAbove = self.getElementAbove(positionClick)
        self.slideElements[positionClick].frame.grid(column=0, row = positionClick-1)
        self.slideElements[indexElementAbove].frame.grid(column=0, row = positionClick)

    def getElementAbove(self, position):
        for i in range(n):
            pos = self.slideElements[i].getPosition()
            if pos == position-1:
                return pos
        print("top element cannot go up again")

window = GroupWindow(3)
window.root.mainloop()