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
            self.slideElements.append(SlideElement(self.root, i, self.switchPlace))
            self.slideElements[-1].frame.grid(column=0, row=i)
        #print(self.slideElements[-1].configure().keys())

    def switchPlace(self, slideElement):
        indexClick = self.slideElements.index(slideElement)
        print(f"index of slide element with position modified: {indexClick}")
        # I want to access the position but I don't know how
        newPositionClick = self.slideElements[indexClick].getPosition()
        if newPositionClick >= 0 and newPositionClick < len(self.slideElements):
            print(f"slide element {indexClick} is allowed to "
                  f"exchange with slide element {newPositionClick}")
        #self.slideElements[positionClick].frame.grid(column=0, row = positionClick-1)
        #self.slideElements[indexElementAbove].frame.grid(column=0, row = positionClick)

    def getElementToExchange(self, position):
        for i in range(n):
            pos = self.slideElements[i].getPosition()
            if pos == position:
                return pos
        print(f"element cannot move to position {position}, " 
              "it is out of the valid positions. Put his value to the old one.")

window = GroupWindow(3)
window.root.mainloop()