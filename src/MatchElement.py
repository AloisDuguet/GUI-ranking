import tkinter as tk
from tkinter import ttk

from SlideElement import *

class MatchElement(SlideElement):
    def __init__(self, master, name, callbackQualify):
        self.frame = ttk.Frame(master,
                               borderwidth=3,
                               relief='raised')
        self.frame.columnconfigure(0, weight=5)
        self.frame.columnconfigure(1, weight=2)
        self.frame.rowconfigure(0)

        self.name = ttk.Label(self.frame, text=name)
        self.name.grid(column=0, row=0)

        self.qualify = ttk.Button(self.frame, text="qualify", command=lambda *args: callbackQualify(self))
        self.qualify.grid(column=1, row=0, sticky=tk.E)