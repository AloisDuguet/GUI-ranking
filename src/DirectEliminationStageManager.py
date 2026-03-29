import numpy.random
import math

from MatchWindow import *
from ListToRank import *

class DirectEliminationStageManager:
    def __init__(self, root, listToRank):
        self.root = root
        self.listToRank = listToRank
        self.n = len(self.listToRank.competitors)

        # the matches of the stage are organised via a modified FIFO list
        self.modifiedFIFO = self.listToRank.competitors
        # random initiation
        numpy.random.shuffle(self.modifiedFIFO)

    def getTitleWindow(self, matchNumber):
        if self.numberQualified == 1:
            return f"Direct elimination stage: final"
        elif self.numberQualified == 2:
            return f"Direct elimination stage: semifinal, match {matchNumber+1} / {self.numberOfMatches}"
        else:
            return f"Direct elimination stage: 1/{self.numberQualified}-th of final, match {matchNumber+1} / {self.numberOfMatches}"

    def manageOneMatch(self, key, i):
        competitors = [self.modifiedFIFO.pop(0)]
        competitors.append(self.modifiedFIFO.pop(0))
        nameWindow = self.getTitleWindow(i)
        groupToRank = ListToRank(competitors, "", self.listToRank.criterion)
        window = MatchWindow(self.root, groupToRank, nameWindow)
        winner,loser = window.classify()
        print(f"{winner} won against {loser}")
        self.modifiedFIFO.append(winner)
        self.listToRank.ranking[key].append(loser)
        print(f"{loser} should be added with rank {key}")

    def manageOneRound(self):
        # compute number of matches so that 
        # a power of 2 is qualified to the next round

        numberRemaining = len(self.modifiedFIFO)

        # number of qualified is the power of 2 immediately strictly inferior
        exponentQualified = math.floor(math.log2(numberRemaining-1))
        self.numberQualified = pow(2, exponentQualified)
        
        self.numberOfMatches = numberRemaining - self.numberQualified
        numberWithFreePass = numberRemaining - 2*self.numberOfMatches
        key = self.listToRank.produceKey(self.numberQualified+1,numberRemaining)
        self.listToRank.ranking[key] = []
        for i in range(self.numberOfMatches):
            self.manageOneMatch(key, i)
        # show free passes for logs
        if numberWithFreePass > 0:
            print("free pass for this round:")
            for i in range(numberWithFreePass):
                print(self.modifiedFIFO[i])
        else:
            print("no free pass this round")

    def manageCompetition(self):
        while len(self.modifiedFIFO) > 1:
            self.manageOneRound()
            print(f"remaining competitor after round: {self.modifiedFIFO}")
            print(f"current ranking: {self.listToRank.ranking}")

        # when only one competitor is in self.modifiedFIFO:
        self.listToRank.ranking['1'] = [self.modifiedFIFO.pop(0)]
        
        # show ranking or range of ranking for everyone 
        # via self.listToRank
        self.listToRank.printRanking()
        self.listToRank.fillCompetitorsFromRanking()
        print("list to rank at the end of direct elimination stage:")
        self.listToRank.describe()
        return self.listToRank
