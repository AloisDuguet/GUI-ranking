import tkinter as tk
from tkinter import ttk
import numpy.random

from GroupWindow import *

# when other stage managers will be coded, create 
# a mother class AbstractStageManager with all common methods

class GroupStageManager:
    def __init__(self, root, listToRank, nGroups):
        self.root = root
        self.listToRank = listToRank
        self.n = len(self.listToRank.competitors)
        self.nGroups = nGroups
        self.groups = []
        for i in range(nGroups):
            self.groups.append([])
        self.filename = ""
    
    def printParticipants(self, with_ranking=False):
        for i in range(self.n):
            if with_ranking:
                print(f"{i+1}: {self.listToRank.competitors[i]}")
            else:
                print(self.listToRank.competitors[i])
    
    def printRanking(self):
        self.printParticipants(with_ranking=True)

    def makeUnequalLevelGroups(self):
        # make random groups with approximately
        # the same number of players
        numpy.random.shuffle(self.listToRank.competitors)
        indexGroup = 0
        for el in self.listToRank.competitors:
            self.groups[indexGroup].append(el)
            indexGroup = (indexGroup+1)%self.nGroups
        print("Groups built:")
        self.printGroups()

    def makeEqualLevelGroups(self):
        indexGroup = 0
        elementPerGroup = int(numpy.floor(self.n / self.nGroups))
        biggerGroups = self.n % self.nGroups # the first few groups are bigger by one
        cpt = 0
        for indexGroup in range(self.nGroups):
            bonus = 0
            if indexGroup < biggerGroups:
                bonus = 1
            for i in range(elementPerGroup+bonus):
                self.groups[indexGroup].append(self.listToRank.competitors[cpt])
                cpt += 1
        print("Groups built:")
        self.printGroups()

    def printGroup(self, i, with_ranking=False):
        for j in range(len(self.groups[i])):
            if with_ranking:
                print(f"\t{j+1}: {self.groups[i][j]}")
            else:
                print(f"\t{self.groups[i][j]}")
    
    def printGroups(self, with_ranking=False):
        for i in range(self.nGroups):
            print(f"group {i}:")
            if with_ranking:
                self.printGroup(i, with_ranking=True)
            else:
                self.printGroup(i)

    def classifyGroup(self, i):
        nameGroup = f"Group Stage: group {i+1} / {self.nGroups}"
        window = GroupWindow(self.root, self.groups[i], nameGroup, self.listToRank)
        self.groups[i] = window.classify()

    def classifyGroups(self):
        for i in range(self.nGroups):
            self.classifyGroup(i)
        print("ranking of groups after group phase:")
        self.printGroups(with_ranking=True)
    
    def reorderParticipants(self):
        # reorder competitors in this way:
        # first the winner of each group
        # then second of each group
        # ...
        newOrder = []
        # the first groups can have one more competitor
        for i in range(len(self.groups[0])):
            for group in self.groups:
                if i < len(group):
                    newOrder.append(group[i])
        self.listToRank.competitors = newOrder
        self.printRanking()
    
    def manageCompetition(self):
        self.makeUnequalLevelGroups()
        self.classifyGroups()
        self.reorderParticipants()
        return self.listToRank.competitors
        


if __name__ == "__main__":
    nameList = ["comme un boomerang", "la marseillaise", "grand pianola music", "wor"]
    manager = GroupStageManager(nameList, 2)
    manager.manageCompetition()