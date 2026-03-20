import tkinter as tk
from tkinter import ttk

class ResultWindow:
    def __init__(self, root, participants):
        self.root = root
        self.participants = participants
        self.frame = ttk.Frame(self.root,
                               relief='raised')

        # fill in participants with corresponding ranking
        self.elements = []
        self.rankings = []
        for i in range(len(self.participants)):
            self.frame.rowconfigure(i)
            self.elements.append(ttk.Label(self.frame, text="{} - {}".format(i+1,self.participants[i]), anchor='center', width=400))
            self.elements[i].pack()
        
        # add button to close this window
        self.closeButton = ttk.Button(self.frame,
                                      text="close ranking",
                                      command=self.root.quit)
        
    def showResults(self):
        self.frame.pack()
        self.closeButton.pack()
        self.root.mainloop()
        self.frame.destroy()
        return 0
