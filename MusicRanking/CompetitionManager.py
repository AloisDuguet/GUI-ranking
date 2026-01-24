from GroupStageManager import *
from SeasonStageManager import *

class CompetitionManager:
    def __init__(self, 
                 nameList,
                 doGroupStage=True, 
                 doSeasonStage=True, 
                 nGroupGroupStage=3, 
                 nGroupSeasonStage=3, 
                 nSeasons=3):
        # TODO: choose all arguments in a GUI
        self.participants = nameList
        self.n = len(self.participants)
        self.doGroupStage = doGroupStage
        self.doSeasonStage = doSeasonStage
        self.nGroupGroupStage = nGroupGroupStage
        self.nGroupSeasonStage = nGroupSeasonStage
        self.nSeasons = nSeasons

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
        print("Final ranking of the competition:")
        GroupStageManager.printParticipants(self, with_ranking=True)

if __name__ == "__main__":
    nameList = ["Naruto", "Full Metal Alchemist", 
                "Frieren", "One Punch Man", 
                "Devilman: crybaby", "Hunter x Hunter",
                "Dragon Ball", "Jujutsu Kaisen",
                "L'Attaque des Titans", "Bleach"]
    manager = CompetitionManager(nameList, True, True, 3, 3, 2)
    manager.manageCompetition()