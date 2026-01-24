import tkinter as tk
from tkinter import ttk

from slideElement import *

class GroupWindow:
    def __init__(self, nameList):
        self.nSlideElements = len(nameList) # number of slideElements
        self.root = tk.Tk()
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(self.nSlideElements, weight=1)
        self.slideElements = []
        for i in range(self.nSlideElements):
            self.slideElements.append(SlideElement(self.root, nameList[i], self.goUp, self.goDown))
            self.slideElements[-1].frame.grid(column=0, row=i)
    
    def goUp(self, slideElement):
        indexClick = self.slideElements.index(slideElement)
        print(f"index of slide element with position to move up once: {indexClick}")
        if indexClick >= 1: # not the first of the list
            print(f"slide element {indexClick} is allowed to "
                  "go up once")
            # exchange place of the two slide elements on the window
            self.slideElements[indexClick].frame.grid(column=0, row=indexClick-1)
            self.slideElements[indexClick-1].frame.grid(column=0, row=indexClick)
            # exchange place of the two slide elements in the list
            self.slideElements[indexClick], self.slideElements[indexClick-1] = self.slideElements[indexClick-1], self.slideElements[indexClick]
        else:
            print(f"slide element {indexClick} is not allowed to "
                  "go up once")
        
    def goDown(self, slideElement):
        indexClick = self.slideElements.index(slideElement)
        print(f"index of slide element with position to move down once: {indexClick}")
        if indexClick < self.nSlideElements-1: # not the last of the list
            print(f"slide element {indexClick} is allowed to "
                  "go down once")
            # exchange place of the two slide elements on the window
            self.slideElements[indexClick].frame.grid(column=0, row=indexClick+1)
            self.slideElements[indexClick+1].frame.grid(column=0, row=indexClick)
            # exchange place of the two slide elements in the list
            self.slideElements[indexClick], self.slideElements[indexClick+1] = self.slideElements[indexClick+1], self.slideElements[indexClick]
        else:
            print(f"slide element {indexClick} is not allowed to "
                  "go down once")


nameList = ["comme un boomerang", "la marseillaise", "grand pianola music"]
window = GroupWindow(nameList)
window.root.mainloop()