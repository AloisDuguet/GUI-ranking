from GroupStageManager import *
from DemotePromoteWindow import *

# TODO: display at the same time as the current group being organized 
# for promotion and demotion the groups in which the elements 
# can be promoted to the left and demoted to the right

class SeasonStageManager(GroupStageManager):
    def __init__(self, root, listToRank, nGroups, nSeasons):
        GroupStageManager.__init__(self, root, listToRank, nGroups)
        self.nSeasons = nSeasons
        self.currentSeason = 0

    def classifyGroup(self, i):
        nameGroup = f"Season {self.currentSeason} / {self.nSeasons} of Season Stage: Division {i+1} / {self.nGroups}"
        groupToRank = ListToRank(self.groups[i], "", self.listToRank.criterion)
        window = DemotePromoteWindow(self.root, groupToRank, nameGroup)
        if i == 0:
            # no promotion allowed from best group
            window.noPromotion()
        if i == self.nGroups-1:
            # no demotion allowed from worst group
            window.noDemotion()
        resSeasonForGroup = window.classify()
        return resSeasonForGroup

    def manageSeason(self):
        resSeason = []
        for i in range(self.nGroups):
            resSeason.append(self.classifyGroup(i))
        # create new groups at the end of the season
        # resSeason[i][j]: group i, 
        # j=0 demotion; j=1 stay; j=2 promotion
        # best group first
        if self.nGroups > 1: # no changes if only one group
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
        self.listToRank.resetRanking()
        rankCounter = 1
        for group in self.groups:
            for competitor in group:
                key = self.listToRank.produceKey(rankCounter)
                self.listToRank.ranking[key] = competitor
                rankCounter += 1
        self.listToRank.fillCompetitorsFromRanking()
        self.listToRank.printRanking()
    
    def manageCompetition(self):
        self.makeEqualLevelGroups()
        for indexSeason in range(self.nSeasons):
            self.currentSeason += 1
            self.manageSeason()
            print(f"Groups at the end of season {self.currentSeason}")
            print(self.groups)
            self.printGroups()
        self.reorderParticipants()
        return self.listToRank
        
if __name__ == "__main__":
    nameList = ["comme un boomerang", "la marseillaise", "grand pianola music", "wor"]
    manager = SeasonStageManager(nameList, 2, 3)
    manager.manageCompetition()