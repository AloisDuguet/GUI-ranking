import tkinter as tk
from tkinter import ttk

class SlideElement:
    def __init__(self, master, name, callbackUp, callbackDown, ranking):
        self.frame = ttk.Frame(master, 
                               borderwidth=3,
                               relief='raised')
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=5)
        self.frame.columnconfigure(2, weight=2)
        self.frame.rowconfigure(0)
        self.frame.rowconfigure(1)

        self.ranking = ranking
        self.rankingLabel = ttk.Label(self.frame, text="{} - ".format(self.ranking))
        self.rankingLabel.grid(column=0, row=0, rowspan=2, sticky=tk.W)

        self.name = ttk.Label(self.frame, text=name)
        self.name.grid(column=1, row=0, rowspan=2)

        self.up = ttk.Button(self.frame, text="go up", command= lambda *args: callbackUp(self))
        self.down = ttk.Button(self.frame, text="go down", command=lambda *args: callbackDown(self))
        self.up.grid(column=2, row=0, sticky=tk.E)
        self.down.grid(column=2, row=1, sticky=tk.E)

    def getName(self):
        return self.name.cget("text")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('400x400')
    root.title("test slideElement")

    slide = SlideElement(root, 1)
    slide.frame.pack(side='top')

    root.mainloop()