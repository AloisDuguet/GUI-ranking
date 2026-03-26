from GroupStageManager import *
from GroupWindow import *

class FinalGroupStageManager(GroupStageManager):
    def __init__(self, root, listToRank):
        # there is only one group
        GroupStageManager.__init__(self, root, listToRank, 1)
    
    def manageCompetition(self):
        # there is only one group
        self.groups[0] = self.listToRank.competitors
        self.classifyGroups()
        self.reorderParticipants()
        return self.listToRank.competitors