import tkinter as tk
from tkinter import ttk

class SlideElement:
    def __init__(self, master, name, callbackUp, callbackDown):
        self.frame = ttk.Frame(master, 
                               height=60, 
                               width=200, 
                               borderwidth=3,
                               relief='raised')
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0,weight=1)
        self.frame.rowconfigure(1,weight=1)

        self.name = ttk.Label(self.frame, text=name)
        self.name.grid(column=0, row=0)

        self.up = ttk.Button(self.frame, text="places up", command= lambda *args: callbackUp(self))
        self.down = ttk.Button(self.frame, text="places down", command=lambda *args: callbackDown(self))
        self.up.grid(column=1, row=0)
        self.down.grid(column=1, row=1)

    def getName(self):
        return self.name.cget("text")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('400x400')
    root.title("test slideElement")

    slide = SlideElement(root, 1)
    slide.frame.pack(side='top')

    root.mainloop()