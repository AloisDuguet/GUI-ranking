import tkinter as tk
from tkinter import ttk

from SlideElement import *
from MatchElement import *
from GroupWindow import *

class MatchWindow(GroupWindow):
    def __init__(self, root, competitors, nameWindow, listToRank):
        explanationMessage = "select which of the two competitors should " \
            "be qualified for the next round. The other is eliminated."
        self.initUpperFrame(root, nameWindow, explanationMessage, listToRank)
        self.initLowerFrame(competitors, MatchElement)

    def initLowerFrame(self, competitors, element):
        self.competitors = competitors
        self.lowerFrame = ttk.Frame(self.root,
                                    relief='raised')
        self.nElements = len(competitors)
        self.elements = []

        if len(competitors) != 2:
            raise("MatchWindow was coded for 1v1 matches, "
            "cf self.winner, self.loser, self.qualifyButton...")

        for i in range(self.nElements):
            self.elements.append(element(self.lowerFrame, self.competitors[i], self.qualifyButton))
        
        self.initElementsOnWindow()
        self.widgetStyles()

        self.lowerFrame.pack(fill=tk.BOTH, expand=True)
        
    def qualifyButton(self, matchElement):
        indexClick = self.elements.index(matchElement)
        self.winner = self.competitors[indexClick]
        if indexClick == 0:
            self.loser = self.competitors[1]
        else:
            self.loser = self.competitors[0]
        self.root.quit()
    
    def initElementsOnWindow(self):
        # we assume there will be less than 10 competitors
        if self.nElements > 10:
            raise("scroll bar needs to be implemented " \
            "because the lowerFrame does not fit the screen")
        self.lowerFrame.columnconfigure(0)
        for i in range(self.nElements):
            self.lowerFrame.rowconfigure(i)
            self.elements[i].frame.grid(column=0, row=i, sticky='news')
    
    def classify(self):
        self.root.mainloop()
        self.upperFrame.destroy()
        self.lowerFrame.destroy()
        print(self.winner)
        print(self.loser)
        return self.winner, self.loser