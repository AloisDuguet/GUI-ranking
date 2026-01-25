import tkinter as tk
from tkinter import ttk
import math

from SlideElement import *

class GroupWindow:
    def __init__(self, nameList, nameWindow):
        self.init(nameList, nameWindow, SlideElement, self.goUp, self.goDown)

    def init(self, nameList, nameWindow, Element, callbackButtonUp, callbackButtonDown):
        self.nSlideElements = len(nameList) # number of slideElements
        self.ranking = []
        self.root = tk.Tk()
        self.root.title(nameWindow)
        self.elementPerColumn = 12
        self.slideElements = []
        for i in range(self.nSlideElements):
            self.slideElements.append(Element(self.root, nameList[i], callbackButtonUp, callbackButtonDown))
        # add button validating current ranking
        self.validRankingButton = ttk.Button(self.root, 
                                             text="validate ranking", 
                                             command=self.validateRanking)
        self.initElementsOnWindow(Element, callbackButtonUp, callbackButtonDown)
        self.disableButtons()
        self.widgetStyles()
    
    def initElementsOnWindow(self, Element, callbackButtonUp, callbackButtonDown):
        if self.nSlideElements <= self.elementPerColumn:
            self.root.columnconfigure(0, weight=5)
            self.root.columnconfigure(1, weight=1)
            for i in range(self.nSlideElements):
                self.root.rowconfigure(i, weight=1)
                self.slideElements[i].frame.grid(column=0, row=i)
            self.validRankingButton.grid(column=1,row=0)
        else:
            self.nColumnWithElements = int(math.ceil(self.nSlideElements/self.elementPerColumn))
            # build columns
            for i in range(self.nColumnWithElements):
                print(f"making column {i}")
                self.root.columnconfigure(i, weight=5)
            self.root.columnconfigure(self.nColumnWithElements, weight=1)
            # build rows
            for i in range(self.elementPerColumn):
                print(f"making row {i}")
                self.root.rowconfigure(i, weight=1)
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
        return self.ranking


if __name__ == "__main__":
    nameList = ["comme un boomerang", "la marseillaise", "grand pianola music"]
    window = GroupWindow(nameList)
    window.root.mainloop()