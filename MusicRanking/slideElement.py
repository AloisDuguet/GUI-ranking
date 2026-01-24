import tkinter as tk
from tkinter import ttk

class SlideElement:
    def __init__(self, master, position, callback):
        self.frame = ttk.Frame(master, 
                               height=60, 
                               width=200, 
                               borderwidth=3,
                               relief='raised')
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0,weight=1)
        self.frame.rowconfigure(1,weight=1)

        self.position = tk.IntVar(master, value=position)
        self.position.trace_add("write", lambda *args: callback(self))
        self.textVar = tk.StringVar()
        self.textVar.set(f"element {self.position.get()}")
        self.name = ttk.Label(self.frame, textvariable=self.textVar)
        self.name.grid(column=0, row=0)

        self.up = ttk.Button(self.frame, text="places up", command=self.goUp)
        self.down = ttk.Button(self.frame, text="places down", command=self.goDown)
        self.up.grid(column=1, row=0)
        self.down.grid(column=1, row=1)
        #self.index? goUp decreases it and goDown decreases it?

    
    def goUp(self):
        self.position.set(self.position.get()-1)
        print(f"goes in position {self.position.get()}")
        self.textVar.set(f"element {self.position.get()}")

    def goDown(self):
        self.position.set(self.position.get()+1)
        print(f"goes in position {self.position.get()}")
        self.textVar.set(f"element {self.position.get()}")

    def getPosition(self):
        return self.position.get()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('400x400')
    root.title("test slideElement")

    slide = SlideElement(root, 1)
    slide.frame.pack(side='top')

    root.mainloop()