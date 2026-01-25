import os
from GroupStageManager import *
from SeasonStageManager import *
from FinalGroupStageManager import *

class CompetitionManager:
    def __init__(self, 
                 nameList,
                 doGroupStage=True, 
                 doSeasonStage=True,
                 doFinalGroupStage=True,
                 nGroupGroupStage=3, 
                 nGroupSeasonStage=3, 
                 nSeasons=3):
        # TODO: choose all arguments in a GUI
        self.participants = nameList
        self.n = len(self.participants)
        self.doGroupStage = doGroupStage
        self.doSeasonStage = doSeasonStage
        self.doFinalGroupStage = doFinalGroupStage
        self.nGroupGroupStage = nGroupGroupStage
        self.nGroupSeasonStage = nGroupSeasonStage
        self.nSeasons = nSeasons

    def confirmPressed(self):
        self.root.quit()

    def getFilename(self):
        self.root = tk.Tk()
        message = "Enter filename to write the ranking"
        label = ttk.Label(self.root, text=message)
        label.pack()
        message2 = f"current directory: {os.getcwd()}"
        label2 = ttk.Label(self.root, text=message2)
        label2.pack()
        entry = ttk.Entry(self.root)
        entry.pack()
        entry.focus()
        button = ttk.Button(self.root, text="confirm", command=self.confirmPressed)
        button.pack()
        self.root.mainloop()
        self.filename = entry.get()
        self.root.destroy()
    
    def writeRanking(self):
        self.getFilename()
        with open(self.filename, "w") as file:
            for i in range(self.n):
                file.write(f"{i+1}: {self.participants[i]}\n")

    def manageCompetition(self):
        if self.doGroupStage:
            manager = GroupStageManager(self.participants, 
                                        self.nGroupGroupStage)
            self.participants = manager.manageCompetition()
        if self.doSeasonStage:
            manager = SeasonStageManager(self.participants, 
                                         self.nGroupSeasonStage, 
                                         self.nSeasons)
            self.participants = manager.manageCompetition()
        if self.doFinalGroupStage:
            # one group to sort everything
            manager = FinalGroupStageManager(self.participants)
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
    #nameList = ["Naruto", "Full Metal Alchemist", 
    #            "Frieren", "One Punch Man"]
    manager = CompetitionManager(nameList, False, False, True, 4, 4, 2)
    # TODO: create function returning a list with all files in a folder to automatically get the proper participants' list
    manager.manageCompetition()
    # TODO: only one window is open the whole execution, instead of having a window per group