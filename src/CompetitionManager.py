import os
import tkinter as tk
from tkinter import font

from GroupStageManager import *
from SeasonStageManager import *
from FinalGroupStageManager import *
from ResultWindow import *
from ChooseListWindow import *
from ListToRank import *
from Helpers import *
from Parsers import *

def isPositiveInteger(what):
    try:
        if int(what) > 0:
            return True
        else:
            return False
    except:
        return False

class CompetitionManager:
    def __init__(self, 
                 competitorsList):
        self.root = tk.Tk()
        self.listToRank = ListToRank(competitorsList, [], [])
        if competitorsList == []:
            #competitorsList = getListFromFolder(self.root)
            self.chooseListWindow = ChooseListWindow(self.root)
            self.listToRank = self.chooseListWindow.chooseList()
        # for now, no name and criterion given to listToRank
        self.listToRank.describe()
        self.n = len(self.listToRank.competitors)

        self.doGroupStage = False
        self.doSeasonStage = False
        self.doFinalGroupStage = False
        self.nGroupGroupStage = 3
        self.nGroupSeasonStage = 3
        self.nSeasons = 1
        self.chooseCompetitionSetup()

    def chooseCompetitionSetup(self):
        # TODO: transform this function into a class
        
        self.styleButtonPressed = ttk.Style()
        self.styleButtonPressed.theme_use('alt')
        self.styleButtonPressed.configure("Pressed.TButton", background='green')
        self.styleButtonPressed.configure('TButton', background = 'grey', foreground = 'white')
        self.styleButtonPressed.map('TButton', background=[('active','darkgrey')])

        # explanation of the setup screen
        explanation = tk.Message(self.root,
            text="Select the stages you want in the competition by clicking the corresponding 'add stage'.\n" \
            "Some stages have options on the right of the 'add stage' button. " \
            "Complete them if you added the stage.\n" \
            "After fulfilling what you need, click 'confirm choices' to start the competition.\n\n" \
            "Explanation of the different stages:\n" \
            "Initial group stage: all competitors are randomly split into n groups, and you will decide for each group the ranking.\n" \
            "Multiple season demote/promote stage: competitors are split into n groups of same level according to (potential) previous ranking. " \
            "Each season, you decide which competitors of the group should be promoted to the immediately stronger group, and which competitors should be demoted to the immediately weaker group. " \
            "At the start of the next season, the competitors promoted or demoted are put in the corresponding group.\n" \
            "Final one-group stage: all competitors are put in the same group, with an initial ranking according to (potential) previous ranking. You will decide the exact ranking of this group.",
            width=800,
            font=(tk.font.nametofont("TkTextFont").actual()["family"],10))
        explanation.pack()

        # the setup of the competition is in a frame
        self.frame = ttk.Frame(self.root,
                               relief='raised')
        
        # get the screen dimension
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        
        # fix the size and position of the window in the middle of the screen
        windowWidth = screenWidth
        windowHeight = screenHeight

        # find the center point
        centerX = int(screenWidth/2 - windowWidth / 2)
        centerY = int(screenHeight/2 - windowHeight / 2)

        # set the position of the window to the center of the screen
        self.root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')

        self.root.title("Setup of the competition")
        # column 0 for label proposing a specific stage
        self.frame.columnconfigure(0, weight=3)
        # column 1 for button to accept the stage 
        self.frame.columnconfigure(1, weight=1)
        # column 2 for Entry to select the possible int parameters
        self.frame.columnconfigure(2, weight=4)
        # column 3 only to validate choice
        self.frame.columnconfigure(3, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)

        # create widgets of the grid
        self.stageProposals = []
        self.stageProposals.append(ttk.Label(self.frame, text="Do an initial group stage?"))
        self.stageProposals.append(ttk.Label(self.frame, text="Do a multiple season promote/demote stage?"))
        self.stageProposals.append(ttk.Label(self.frame, text="Do a final one-group stage?"))
        self.buttons = []
        self.buttons.append(ttk.Button(self.frame, text="add stage", command= lambda *args: self.confirmStage(self.buttons[0])))
        self.buttons.append(ttk.Button(self.frame, text="add stage", command= lambda *args: self.confirmStage(self.buttons[1])))
        self.buttons.append(ttk.Button(self.frame, text="add stage", command= lambda *args: self.confirmStage(self.buttons[2])))
        self.frameEntries = []
        self.frameEntries.append(ttk.Frame(self.frame))
        self.frameEntries.append(ttk.Frame(self.frame))
        self.entries = []
        positiveIntegerCommand = self.frame.register(isPositiveInteger)
        self.entries.append(ttk.Entry(self.frameEntries[0], validate='all', validatecommand=(positiveIntegerCommand,'%P')))
        self.entries.append(ttk.Entry(self.frameEntries[1], validate='all', validatecommand=(positiveIntegerCommand,'%P')))
        self.entries.append(ttk.Entry(self.frameEntries[1], validate='all', validatecommand=(positiveIntegerCommand,'%P')))
        self.labelEntries = []
        self.labelEntries.append(ttk.Label(self.frameEntries[0], text="number of groups:"))
        self.labelEntries.append(ttk.Label(self.frameEntries[1], text="number of groups:"))
        self.labelEntries.append(ttk.Label(self.frameEntries[1], text="number of seasons:"))
        self.confirmButton = ttk.Button(self.frame, text="confirm choices", command = self.root.quit)

        # fill in the grid
        # two first columns
        for i in range(3):
            self.stageProposals[i].grid(column=0, row=i)
            self.buttons[i].grid(column=1, row=i)
        # third column
        # first row
        self.frameEntries[0].columnconfigure(0)
        self.frameEntries[0].rowconfigure(0)
        self.frameEntries[0].rowconfigure(1)
        self.labelEntries[0].grid(column=0, row=0)
        self.entries[0].grid(column=0, row=1)
        self.frameEntries[0].grid(column=2, row=0)
        # second row
        self.frameEntries[1].columnconfigure(0)
        self.frameEntries[1].columnconfigure(1)
        self.frameEntries[1].rowconfigure(0)
        self.frameEntries[1].rowconfigure(1)
        self.labelEntries[1].grid(column=0, row=0)
        self.entries[1].grid(column=0, row=1)
        self.labelEntries[2].grid(column=1, row=0)
        self.entries[2].grid(column=1, row=1)
        self.frameEntries[1].grid(column=2, row=1)
        # fourth column
        self.confirmButton.grid(column=3, row=0, rowspan=3, sticky=tk.N+tk.S+tk.W+tk.E)

        self.frame.pack(ipadx=5,ipady=5)

        # launch window
        self.root.mainloop()

        # retrieve entry values when window is closed
        if self.doGroupStage:
            # TODO: add safeguards that the entry is int 
            # and that it is strictly positive
            # cf https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/entry-validation.html
            if int(self.entries[0].get()) > 0:
                self.nGroupGroupStage = int(self.entries[0].get())
        if self.doSeasonStage:
            if int(self.entries[1].get()) > 0:
                self.nGroupSeasonStage = int(self.entries[1].get())
            if int(self.entries[2].get()) > 0:
                self.nSeasons = int(self.entries[2].get())
        
        # destroy window
        explanation.destroy()
        self.frame.destroy()

    def confirmStage(self, button):
        # define style for button pressed
        buttonNumber = self.buttons.index(button)
        if buttonNumber == 0:
            self.doGroupStage = True
            self.buttons[0].config(style="Pressed.TButton")
        if buttonNumber == 1:
            self.doSeasonStage = True
            self.buttons[1].config(style="Pressed.TButton")
        if buttonNumber == 2:
            self.doFinalGroupStage = True
            self.buttons[2].config(style="Pressed.TButton")
    
    def writeRanking(self):
        filename = inputPath("Enter filename to write the ranking", self.root)
        with open(filename, "w") as file:
            for i in range(self.n):
                file.write(f"{i+1}: {self.listToRank.competitors[i]}\n")

    def manageCompetition(self):
        if self.doGroupStage:
            manager = GroupStageManager(self.root,
                                        self.listToRank, 
                                        self.nGroupGroupStage)
            self.listToRank.competitors = manager.manageCompetition()
        if self.doSeasonStage:
            manager = SeasonStageManager(self.root,
                                         self.listToRank, 
                                         self.nGroupSeasonStage, 
                                         self.nSeasons)
            self.listToRank.competitors = manager.manageCompetition()
        if self.doFinalGroupStage:
            # one group to sort everything
            manager = FinalGroupStageManager(self.root,
                                             self.listToRank)
            self.listToRank.competitors = manager.manageCompetition()
        print("Final ranking of the competition:")
        GroupStageManager.printParticipants(self, with_ranking=True)
        manager = ResultWindow(self.root, self.listToRank)
        manager.showResults()
        self.writeRanking()

def main():
    competitorsList = []
    #competitorsList = getListFromFolder(tk.Tk())
    #competitorsList = parseListFromTxt("listsToSort/mangas.txt")
    
    print("defining competition")
    manager = CompetitionManager(competitorsList)
    print("starting competition")
    manager.manageCompetition()
    
if __name__ == "__main__":
    main()

# TODOs
#when two windows are open, maybe the style is not applied properly (it happened when I used getListFromFolder with its own root)
#in the same situation, when elements are too long the buttons disappear to the right of the grid element
