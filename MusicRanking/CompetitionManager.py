import os

from GroupStageManager import *
from SeasonStageManager import *
from FinalGroupStageManager import *
from Helpers import *

class CompetitionManager:
    def __init__(self, 
                 nameList,
                 doGroupStage=True, 
                 doSeasonStage=True,
                 doFinalGroupStage=True,
                 nGroupGroupStage=3, 
                 nGroupSeasonStage=3, 
                 nSeasons=3):
        self.participants = nameList
        self.n = len(self.participants)

        self.doGroupStage = False
        self.doSeasonStage = False
        self.doFinalGroupStage = False
        self.nGroupGroupStage = 3
        self.nGroupSeasonStage = 3
        self.nSeasons = 1
        self.root = tk.Tk()
        self.chooseCompetitionSetup()

    def chooseCompetitionSetup(self):
        # TODO: transform this function into a class
        
        self.styleButtonPressed = ttk.Style()
        self.styleButtonPressed.theme_use('alt')
        self.styleButtonPressed.configure("Pressed.TButton", background='green')

        self.frame = ttk.Frame(self.root, 
                               height=900,
                               width=1440,
                               relief='raised')
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
        self.stageProposals.append(ttk.Label(self.frame, text="Do an multiple season promote/demote stage?"))
        self.stageProposals.append(ttk.Label(self.frame, text="Do a final one-group stage?"))
        self.buttons = []
        self.buttons.append(ttk.Button(self.frame, text="add stage", command= lambda *args: self.confirmStage(self.buttons[0])))
        self.buttons.append(ttk.Button(self.frame, text="add stage", command= lambda *args: self.confirmStage(self.buttons[1])))
        self.buttons.append(ttk.Button(self.frame, text="add stage", command= lambda *args: self.confirmStage(self.buttons[2])))
        self.frameEntries = []
        self.frameEntries.append(ttk.Frame(self.frame))
        self.frameEntries.append(ttk.Frame(self.frame))
        self.entries = []
        self.entries.append(ttk.Entry(self.frameEntries[0]))
        self.entries.append(ttk.Entry(self.frameEntries[1]))
        self.entries.append(ttk.Entry(self.frameEntries[1]))
        self.labelEntries = []
        self.labelEntries.append(ttk.Label(self.frameEntries[0], text="number of groups:"))
        self.labelEntries.append(ttk.Label(self.frameEntries[1], text="number of groups:"))
        self.labelEntries.append(ttk.Label(self.frameEntries[1], text="number of seasons:"))
        self.confirmButton = ttk.Button(self.frame, text="Confirm choices", command = self.root.quit)

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
        self.confirmButton.grid(column=3, row=0)

        self.frame.pack()

        # launch window
        self.root.mainloop()

        # retrieve entry values when window is closed
        if self.doGroupStage:
            # TODO: add safeguards that the entry is int 
            # and that it is strictly positive
            if int(self.entries[0].get()) > 0:
                self.nGroupGroupStage = int(self.entries[0].get())
        if self.doSeasonStage:
            if int(self.entries[1].get()) > 0:
                self.nGroupSeasonStage = int(self.entries[1].get())
            if int(self.entries[2].get()) > 0:
                self.nSeasons = int(self.entries[2].get())
        
        # destroy window
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
                file.write(f"{i+1}: {self.participants[i]}\n")

    def manageCompetition(self):
        if self.doGroupStage:
            manager = GroupStageManager(self.root,
                                        self.participants, 
                                        self.nGroupGroupStage)
            self.participants = manager.manageCompetition()
        if self.doSeasonStage:
            manager = SeasonStageManager(self.root,
                                         self.participants, 
                                         self.nGroupSeasonStage, 
                                         self.nSeasons)
            self.participants = manager.manageCompetition()
        if self.doFinalGroupStage:
            # one group to sort everything
            manager = FinalGroupStageManager(self.root,
                                             self.participants)
            self.participants = manager.manageCompetition()
        print("Final ranking of the competition:")
        GroupStageManager.printParticipants(self, with_ranking=True)
        self.writeRanking()

if __name__ == "__main__":
    nameList = ["Naruto", "Full Metal Alchemist", 
                "Frieren", "One Punch Man", 
                "Devilman: crybaby", "Hunter x Hunter",
                "Dragon Ball", "Jujutsu Kaisen",
                "L'Attaque des Titans", "Bleach",
                "SaikiK", "One Piece",
                "Uncle from Another World", "Mob Psycho 100",
                "Alice in Wonderland", "Solo Leveling",
                "My Hero Academia", "Detective Conan",
                "Vinland Saga", "Golden Kamui"]
    nameList = ["Naruto", "Full Metal Alchemist", 
                "Frieren", "One Punch Man"]
    
    #nameList = getListFromFolder()
    #print(f"list: {nameList}")
    
    print("defining competition")
    manager = CompetitionManager(nameList, True, True, True, 6, 6, 3)
    print("starting competition")
    manager.manageCompetition()
    # TODO: only one window is open the whole execution, instead of having a window per group