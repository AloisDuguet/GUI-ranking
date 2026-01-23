import tkinter as tk
from tkinter import ttk

from slideElement import *

class GroupWindow:
    def __init__(self, n):
        self.nSlideElements = n # number of slideElements
        self.root = tk.Tk()
        self.slideElements = []
        for i in range(n):
            self.slideElements.append(SlideElement(self.root, i))
            self.slideElements[-1].frame.pack()
        
        # position elements from top to bottom

window = GroupWindow(3)
window.root.mainloop()