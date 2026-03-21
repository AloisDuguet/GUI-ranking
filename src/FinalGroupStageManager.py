from GroupStageManager import *
from GroupWindow import *

class FinalGroupStageManager(GroupStageManager):
    def __init__(self, root, participants):
        # there is only one group
        GroupStageManager.__init__(self, root, participants, 1)
    
    def manageCompetition(self):
        # there is only one group
        self.groups[0] = self.participants
        self.classifyGroups()
        self.reorderParticipants()
        return self.participants