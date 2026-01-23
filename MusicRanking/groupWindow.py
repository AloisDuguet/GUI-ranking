import tkinter as tk
from tkinter import ttk

from slideElement import *

class GroupWindow:
    def __init__(self, n):
        self.nSlideElements = n # number of slideElements
        self.slideElements = []
        for i in range(n):
            self.slideElements.append(SlideElement())
        
        # position elements from top to bottom
        