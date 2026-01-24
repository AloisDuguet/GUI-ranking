from GroupStageManager import *
from DemotePromoteWindow import *

class SeasonStageManager(GroupStageManager):
    def __init__(self, participants, nGroups, nSeasons):
        GroupStageManager.__init__(self, participants, nGroups)
        self.nSeasons = nSeasons

    def classifyGroup(self, i):
        window = DemotePromoteWindow(self.groups[i])
        if i == 0:
            # no promotion allowed from best group
            window.noPromotion()
        elif i == self.nGroups-1:
            # no demotion allowed from worst group
            window.noDemotion()
        resSeason = window.classify()
        window.root.destroy()
        print(f"resSeason:\n{resSeason}")
        return resSeason

    def manageSeason(self):
        resSeason = []
        for i in range(self.nGroups):
            resSeason.append(self.classifyGroup(i))
        # create new groups at the end of the season
        # resSeason[i][j]: group i, 
        # j=0 demotion; j=1 stay; j=2 promotion
        # best group first
        self.groups[0] = resSeason[0][1]
        self.groups[0].extend(resSeason[1][2])
        for i in range(1,self.nGroups-1):
            self.groups[i] = resSeason[i-1][0]
            self.groups[i].extend(resSeason[i][1])
            self.groups[i].extend(resSeason[i+1][2])
        self.groups[self.nGroups-1] = resSeason[self.nGroups-2][0]
        self.groups[self.nGroups-1].extend(resSeason[self.nGroups-1][1])

    def reorderParticipants(self):
        # reorder them from first group to last group
        self.participants = []
        for group in self.groups:
            self.participants.extend(group)
        self.printRanking()
    
    def manageCompetition(self):
        self.makeEqualLevelGroups()
        print(f"")
        for indexSeason in range(self.nSeasons):
            self.manageSeason()
            print(f"Groups at the end of season {indexSeason+1}")
            print(self.groups)
            self.printGroups()
        self.reorderParticipants()
        
if __name__ == "__main__":
    nameList = ["comme un boomerang", "la marseillaise", "grand pianola music", "wor"]
    manager = SeasonStageManager(nameList, 2, 3)
    manager.manageCompetition()