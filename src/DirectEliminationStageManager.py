import numpy.random
import math

from MatchWindow import *

class DirectEliminationStageManager:
    def __init__(self, root, listToRank):
        self.root = root
        self.listToRank = listToRank
        self.n = len(self.listToRank.competitors)

        # the matches of the stage are organised via a modified FIFO list
        self.modifiedFIFO = self.listToRank.competitors
        # random initiation
        numpy.random.shuffle(self.modifiedFIFO)

        # initialize rankings: 
        # a dictionary with key a ranking or range of ranking ('5-8') and value the set of competitors with this ranking
        self.rankings = dict()

    def orderRankingKeys(self):
        # get all keys
        keys = self.rankings.keys()
        # order keys in increasing order
        tempDict = dict()
        listKeys = []
        for key in keys:
            parsedKey = int(key.split('-')[0])
            tempDict[parsedKey] = key
            listKeys.append(parsedKey)
        listKeys.sort()
        orderedKeys = []
        for key in listKeys:
            orderedKeys.append(tempDict[key])
        return orderedKeys

    def showRankings(self):
        orderedKeys = self.orderRankingKeys()
        # print values of each key in increasing order
        for key in orderedKeys:
            values = self.rankings[key]
            if len(values) == 1:
                print("{}: {}".format(key, values))
            else:
                for value in values:
                    print("{}: {}".format(key, value))
    
    def produceRankingList(self):
        orderedKeys = self.orderRankingKeys()
        # print values of each key in increasing order of the key
        self.finalRanking = []
        for key in orderedKeys:
            values = self.rankings[key]
            self.finalRanking.extend(values)
        return self.finalRanking
    
    def getTitleWindow(self, matchNumber):
        if self.numberQualified == 1:
            return f"Direct elimination stage: final"
        elif self.numberQualified == 2:
            return f"Direct elimination stage: semifinal, match {i+1} / {self.numberOfMatches}"
        else:
            return f"Direct elimination stage: 1/{self.numberQualified}-th of final, match {i+1} / {self.numberOfMatches}"

    def manageOneMatch(self, key, i):
        competitors = [self.modifiedFIFO.pop(0)]
        competitors.append(self.modifiedFIFO.pop(0))
        nameWindow = self.getTitleWindow(i)
        window = MatchWindow(self.root, competitors, nameWindow, self.listToRank)
        winner,loser = window.classify()
        print(f"{winner} won against {loser}")
        self.modifiedFIFO.append(winner)
        self.rankings[key].append(loser)

    def manageOneRound(self):
        # compute number of matches so that 
        # a power of 2 is qualified to the next round

        numberRemaining = len(self.modifiedFIFO)

        # number of qualified is the power of 2 immediately strictly inferior
        exponentQualified = math.floor(math.log2(numberRemaining-1))
        self.numberQualified = pow(2, exponentQualified)
        
        self.numberOfMatches = numberRemaining - self.numberQualified
        numberWithFreePass = numberRemaining - 2*self.numberOfMatches
        key = ""
        if self.numberQualified+1 < numberRemaining:
            key = "{}-{}".format(self.numberQualified+1,numberRemaining)
            self.rankings[key] = []
        else:
            key = "{}".format(numberRemaining)
            self.rankings[key] = []
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

        # when only one competitor is in self.modifiedFIFO:
        self.rankings['1'] = [self.modifiedFIFO.pop(0)]
        
        # show ranking or range of ranking for everyone 
        # via self.rankings
        self.showRankings()
        return self.produceRankingList()
