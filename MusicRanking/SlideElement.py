import tkinter as tk
from tkinter import ttk

class SlideElement:
    def __init__(self, master, name, callbackUp, callbackDown, ranking):
        self.frame = ttk.Frame(master, 
                               height=60, 
                               width=200, 
                               borderwidth=3,
                               relief='raised')
        self.frame.columnconfigure(0, weight=0)
        self.frame.columnconfigure(1, weight=0)
        self.frame.columnconfigure(2, weight=0)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)

        self.ranking = ranking
        self.rankingLabel = ttk.Label(self.frame, text="{} - ".format(self.ranking), justify='center', anchor='center', width=10)
        self.rankingLabel.grid(column=0, row=0, rowspan=2)

        self.name = ttk.Label(self.frame, text=name, justify='center', anchor='center', width=150)
        self.name.grid(column=1, row=0, rowspan=2)

        self.up = ttk.Button(self.frame, text="go up", command= lambda *args: callbackUp(self), width=40)
        self.down = ttk.Button(self.frame, text="go down", command=lambda *args: callbackDown(self), width=40)
        self.up.grid(column=2, row=0)
        self.down.grid(column=2, row=1)

    def getName(self):
        return self.name.cget("text")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('400x400')
    root.title("test slideElement")

    slide = SlideElement(root, 1)
    slide.frame.pack(side='top')

    root.mainloop()