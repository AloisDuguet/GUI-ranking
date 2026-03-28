import tkinter as tk
from tkinter import ttk
import math

from SlideElement import *

class GroupWindow:
    def __init__(self, root, competitors, nameWindow, listToRank):
        explanationMessage = "Rank all competitors of this group.\n" \
            "Top position is the best position.\n" \
            "The button 'go up' exchanges the ranking of the corresponding competitor " \
            "with the competitor immediately stronger, while" \
            "the button 'go down' exchanges the ranking of the corresponding competitor " \
            "with the competitor immediately weaker. " \
            "Thus, the current strongest competitor of the group can not go up " \
            "and the current worst competitor of the group can not go down.\n" \
            "When done, click the 'validate ranking' to confirm this ranking."
        self.initUpperFrame(root, nameWindow, explanationMessage, listToRank)
        self.initLowerFrame(root, competitors, SlideElement, self.goUp, self.goDown)

    def initUpperFrame(self, root, nameWindow, explanationMessage, listToRank):
        self.listToRank = listToRank

        self.root = root
        self.root.title(nameWindow)

        self.upperFrame = ttk.Frame(self.root, 
                                    relief='raised')
        self.upperFrame.pack()

        # display explanationMessage as the first element of the window
        self.explanation = tk.Message(self.upperFrame, text=explanationMessage, width = 800, font=(tk.font.nametofont("TkTextFont").actual()["family"],10))
        self.explanation.pack()

        # separate with a horizontal line
        self.separator = ttk.Separator(self.upperFrame, orient='horizontal')
        self.separator.pack(fill='x', padx=200, pady=10)

        # write criterion for ranking if any
        if self.listToRank.criterion != "":
            self.criterionLabel = ttk.Label(self.upperFrame,
                                            text=self.listToRank.criterion)
            self.criterionLabel.pack()

    def initLowerFrame(self, root, competitors, Element, callbackButtonUp, callbackButtonDown):
        # setup of canvas inside overall frame
        self.lowerFrame = ttk.Frame(self.root,
                               relief='raised')
        self.canvas = tk.Canvas(self.lowerFrame,
                                width=50,
                                height=50)
        
        # setup of horizontal scrollbar with the overall frame, scrolling the canvas
        self.scrollbar = ttk.Scrollbar(self.lowerFrame, 
                                       orient=tk.HORIZONTAL)

        # setup of the inner frame containing the slideElements inside the canvas
        self.frameWithElements = ttk.Frame(self.canvas,
                                relief='raised')
        
        self.nSlideElements = len(competitors) # number of slideElements
        self.ranking = []
        self.elementPerColumn = 3
        self.slideElements = []
        for i in range(self.nSlideElements):
            self.slideElements.append(Element(self.frameWithElements, competitors[i], callbackButtonUp, callbackButtonDown, i+1))
        # add button validating current ranking
        self.validRankingButton = ttk.Button(self.frameWithElements, 
                                             text="validate ranking", 
                                             command=self.validateRanking)
        self.initElementsOnWindow()
        self.disableButtons()
        self.widgetStyles()
        
        self.scrollbar.pack(side=tk.TOP, fill=tk.X)
        self.scrollbar.config(command=self.canvas.xview)
        self.canvas['xscrollcommand'] = self.scrollbar.set
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.lowerFrame.pack(fill=tk.BOTH, expand=True)

        # compute correct position for frame in canvas
        # creation of window inside canvas;
        self.canvas.create_window(0, 0, window=self.frameWithElements)

        # update size of canvas with size of frameWithElements
        self.updateScrollbarSize()

        screenWidth = self.root.winfo_screenwidth()
        frameWidth = self.frameWithElements.winfo_width()
        print("screen width: {}\nframe width: {}".format(screenWidth, frameWidth))
        self.canvas.create_window(max(0,screenWidth/2-frameWidth/2), 
                                0, 
                                window=self.frameWithElements, 
                                anchor='nw')

    def updateScrollbarSize(self):
        # update frame inside to get the right size
        self.frameWithElements.update()

        # get the size
        self.canvasHeight = self.frameWithElements.winfo_height()
        self.canvasWidth = self.frameWithElements.winfo_width()
        print("width of inner frame: {}".format(self.canvasWidth))
        print("height of inner frame: {}".format(self.canvasHeight))

        # resize the scrollable region
        self.canvas.config(scrollregion=(0,0,self.canvasWidth,self.canvasHeight))
    
    def initElementsOnWindow(self):
        if self.nSlideElements <= self.elementPerColumn:
            self.frameWithElements.columnconfigure(0)
            self.frameWithElements.columnconfigure(1)
            for i in range(self.nSlideElements):
                self.frameWithElements.rowconfigure(i)
                self.slideElements[i].frame.grid(column=0, row=i, sticky='news')
            self.validRankingButton.grid(column=1,row=0,sticky='news',rowspan=max(self.nSlideElements,1))
        else:
            self.nColumnWithElements = int(math.ceil(self.nSlideElements/self.elementPerColumn))
            # build columns
            for i in range(self.nColumnWithElements):
                print(f"making column {i}")
                self.frameWithElements.columnconfigure(i)
            self.frameWithElements.columnconfigure(self.nColumnWithElements)
            # build rows
            for i in range(self.elementPerColumn):
                print(f"making row {i}")
                self.frameWithElements.rowconfigure(i)
            # assign Elements to grid
            for indexColumn in range(self.nColumnWithElements):
                for indexRow in range(self.elementPerColumn):
                    indexElement = self.elementPerColumn*indexColumn+indexRow
                    if indexElement < self.nSlideElements:
                        self.slideElements[indexElement].frame.grid(column=indexColumn, row=indexRow, sticky='news')
            self.validRankingButton.grid(column=self.nColumnWithElements,row=0,sticky='news',rowspan=self.elementPerColumn)

    def disableButtons(self):
        # disable interdicted buttons
        self.slideElements[0].up.state(['disabled'])
        self.slideElements[self.nSlideElements-1].down.state(['disabled'])
        
    def widgetStyles(self):
        # change Button style
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton', background = 'grey', foreground = 'white')
        style.map('TButton', background=[('active','darkgrey')])
    
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
        # exchange ranking of the two slide elements
        self.slideElements[indexClick].ranking, self.slideElements[indexClick-1].ranking = self.slideElements[indexClick-1].ranking, self.slideElements[indexClick].ranking
        # update text of the label for the ranking
        self.slideElements[indexClick].rankingLabel.config(text="{} - ".format(self.slideElements[indexClick].ranking))
        self.slideElements[indexClick-1].rankingLabel.config(text="{} - ".format(self.slideElements[indexClick-1].ranking))
        if indexClick == 1:
            # disable new button up of element 0 and enable the one of element 1
            self.slideElements[0].up.state(['disabled'])
            self.slideElements[1].up.state(['!disabled'])
        if indexClick == self.nSlideElements-1:
            # disable new button down of last element and enable the one of other element
            self.slideElements[self.nSlideElements-1].down.state(['disabled'])
            self.slideElements[self.nSlideElements-2].down.state(['!disabled'])
        
        self.updateScrollbarSize()
        
    def goDown(self, slideElement):
        indexClick = self.slideElements.index(slideElement)
        # exchange place of the two slide elements on the window
        col,row = self.getGridPosition(indexClick+1)
        self.slideElements[indexClick].frame.grid(column=col, row=row)
        col,row = self.getGridPosition(indexClick)
        self.slideElements[indexClick+1].frame.grid(column=col, row=row)
        # exchange place of the two slide elements in the list
        self.slideElements[indexClick], self.slideElements[indexClick+1] = self.slideElements[indexClick+1], self.slideElements[indexClick]
        # exchange ranking of the two slide elements
        self.slideElements[indexClick].ranking, self.slideElements[indexClick+1].ranking = self.slideElements[indexClick+1].ranking, self.slideElements[indexClick].ranking
        # update text of the label for the ranking
        self.slideElements[indexClick].rankingLabel.config(text="{} - ".format(self.slideElements[indexClick].ranking))
        self.slideElements[indexClick+1].rankingLabel.config(text="{} - ".format(self.slideElements[indexClick+1].ranking))
        if indexClick == 0: 
            # disable new button up of element 0 and enable the one of element 1
            self.slideElements[0].up.state(['disabled'])
            self.slideElements[1].up.state(['!disabled'])
        if indexClick == self.nSlideElements-2:
            # disable new button down of last element and enable the one of other element
            self.slideElements[self.nSlideElements-1].down.state(['disabled'])
            self.slideElements[self.nSlideElements-2].down.state(['!disabled'])
        
        self.updateScrollbarSize()
        
    def validateRanking(self):
        for i in range(self.nSlideElements):
            self.ranking.append(self.slideElements[i].getName())
            print(f"{i+1}: {self.ranking[-1]}")
        self.root.quit()

    def classify(self):
        self.root.mainloop()
        self.upperFrame.destroy()
        self.lowerFrame.destroy()
        return self.ranking
