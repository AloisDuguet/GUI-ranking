import tkinter as tk
from tkinter import ttk

from SlideElement import *

class MatchElement(SlideElement):
    def __init__(self, master, name, callbackQualify):
        self.frame = ttk.Frame(master,
                               borderwidth=3,
                               relief='raised')
        self.frame.rowconfigure(0, weight=2)
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(0, weight=1)

        self.name = ttk.Label(self.frame, text=name, anchor='center')
        self.name.grid(row=0, sticky='news')

        self.qualify = ttk.Button(self.frame, text="qualify", command=lambda *args: callbackQualify(self))
        self.qualify.grid(row=1, sticky='news')