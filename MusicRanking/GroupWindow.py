import tkinter as tk
from tkinter import ttk
import math

from SlideElement import *

class GroupWindow:
    def __init__(self, root, nameList, nameWindow):
        explanationMessage = "Rank all competitors of this group.\n" \
            "Top position is the best position.\n" \
            "The button 'go up' exchanges the ranking of the corresponding competitor " \
            "with the competitor immediately stronger, while" \
            "the button 'go down' exchanges the ranking of the corresponding competitor " \
            "with the competitor immediately weaker. " \
            "Thus, the current strongest competitor of the group can not go up " \
            "and the current worst competitor of the group can not go down.\n" \
            "When done, click the 'validate ranking' to confirm this ranking."
        self.init(root, nameList, nameWindow, explanationMessage, SlideElement, self.goUp, self.goDown)

    def init(self, root, nameList, nameWindow, explanationMessage, Element, callbackButtonUp, callbackButtonDown):
        self.root = root
        self.root.title(nameWindow)

        # display explanationMessage as the first element of the window
        self.explanation = tk.Message(self.root, text=explanationMessage, width = 800)
        self.explanation.pack()

        self.frame = ttk.Frame(self.root,
                               relief='raised')
        self.frame.pack()
        self.nSlideElements = len(nameList) # number of slideElements
        self.ranking = []
        self.elementPerColumn = 12
        self.slideElements = []
        for i in range(self.nSlideElements):
            self.slideElements.append(Element(self.frame, nameList[i], callbackButtonUp, callbackButtonDown))
        # add button validating current ranking
        self.validRankingButton = ttk.Button(self.frame, 
                                             text="validate ranking", 
                                             command=self.validateRanking)
        self.initElementsOnWindow(Element, callbackButtonUp, callbackButtonDown)
        self.disableButtons()
        self.widgetStyles()
    
    def initElementsOnWindow(self, Element, callbackButtonUp, callbackButtonDown):
        if self.nSlideElements <= self.elementPerColumn:
            self.frame.columnconfigure(0, weight=5)
            self.frame.columnconfigure(1, weight=1)
            for i in range(self.nSlideElements):
                self.frame.rowconfigure(i, weight=1)
                self.slideElements[i].frame.grid(column=0, row=i)
            self.validRankingButton.grid(column=1,row=0)
        else:
            self.nColumnWithElements = int(math.ceil(self.nSlideElements/self.elementPerColumn))
            # build columns
            for i in range(self.nColumnWithElements):
                print(f"making column {i}")
                self.frame.columnconfigure(i, weight=5)
            self.frame.columnconfigure(self.nColumnWithElements, weight=1)
            # build rows
            for i in range(self.elementPerColumn):
                print(f"making row {i}")
                self.frame.rowconfigure(i, weight=1)
            # assign Elements to grid
            for indexColumn in range(self.nColumnWithElements):
                for indexRow in range(self.elementPerColumn):
                    indexElement = self.elementPerColumn*indexColumn+indexRow
                    if indexElement < self.nSlideElements:
                        self.slideElements[indexElement].frame.grid(column=indexColumn, row=indexRow)
            self.validRankingButton.grid(column=self.nColumnWithElements,row=0)

    def disableButtons(self):
        # disable interdicted buttons
        self.slideElements[0].up.state(['disabled'])
        self.slideElements[self.nSlideElements-1].down.state(['disabled'])
        
    def widgetStyles(self):
        # change Button style
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton', background = 'grey', foreground = 'white')
        style.map('TButton', background=[('active','blue')])
        # change Label style
        style.configure('TLabel', width = 40)
    
    def getGridPosition(self, position):
        indexColumn = int(position/self.elementPerColumn)
        indexRow = position%self.elementPerColumn
        return [indexColumn,indexRow]
    
    def goUp(self, slideElement):
        indexClick = self.slideElements.index(slideElement)
        # exchange place of the two slide elements on the window
        col,row = self.getGridPosition(indexClick-1)
        self.slideElements[indexClick].frame.grid(column=col, row=row)
        col,row = self.getGridPosition(indexClick)
        self.slideElements[indexClick-1].frame.grid(column=col, row=row)
        # exchange place of the two slide elements in the list
        self.slideElements[indexClick], self.slideElements[indexClick-1] = self.slideElements[indexClick-1], self.slideElements[indexClick]
        if indexClick == 1:
            # disable new button up of element 0 and enable the one of element 1
            self.slideElements[0].up.state(['disabled'])
            self.slideElements[1].up.state(['!disabled'])
        if indexClick == self.nSlideElements-1:
            # disable new button down of last element and enable the one of other element
            self.slideElements[self.nSlideElements-1].down.state(['disabled'])
            self.slideElements[self.nSlideElements-2].down.state(['!disabled'])
        
    def goDown(self, slideElement):
        indexClick = self.slideElements.index(slideElement)
        # exchange place of the two slide elements on the window
        col,row = self.getGridPosition(indexClick+1)
        self.slideElements[indexClick].frame.grid(column=col, row=row)
        col,row = self.getGridPosition(indexClick)
        self.slideElements[indexClick+1].frame.grid(column=col, row=row)
        # exchange place of the two slide elements in the list
        self.slideElements[indexClick], self.slideElements[indexClick+1] = self.slideElements[indexClick+1], self.slideElements[indexClick]
        if indexClick == 0: 
            # disable new button up of element 0 and enable the one of element 1
            self.slideElements[0].up.state(['disabled'])
            self.slideElements[1].up.state(['!disabled'])
        if indexClick == self.nSlideElements-2:
            # disable new button down of last element and enable the one of other element
            self.slideElements[self.nSlideElements-1].down.state(['disabled'])
            self.slideElements[self.nSlideElements-2].down.state(['!disabled'])
        
    def validateRanking(self):
        for i in range(self.nSlideElements):
            self.ranking.append(self.slideElements[i].getName())
            print(f"{i+1}: {self.ranking[-1]}")
        self.root.quit()

    def classify(self):
        self.root.mainloop()
        self.explanation.destroy()
        self.frame.destroy()
        return self.ranking


if __name__ == "__main__":
    # outdated
    nameList = ["comme un boomerang", "la marseillaise", "grand pianola music"]
    window = GroupWindow(nameList)
    window.root.mainloop()