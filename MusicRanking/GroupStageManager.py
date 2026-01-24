import tkinter as tk
from tkinter import ttk
import numpy.random

from GroupWindow import *

# when other stage managers will be coded, create 
# a mother class AbstractStageManager with all common methods

class GroupStageManager:
    def __init__(self, participants, nGroups):
        self.participants = participants
        self.nGroups = nGroups
        self.groups = []
        for i in range(nGroups):
            self.groups.append([])
    
    def printParticipants(self, with_ranking=False):
        for i in range(len(self.participants)):
            if with_ranking:
                print(f"{i+1}: {self.participants[i]}")
            else:
                print(self.participants[i])
    
    def printRanking(self):
        self.printParticipants(with_ranking=True)

    def makeGroups(self):
        # make random groups with approximately
        # the same number of players
        numpy.random.shuffle(self.participants)
        indexGroup = 0
        for el in self.participants:
            self.groups[indexGroup].append(el)
            indexGroup = (indexGroup+1)%self.nGroups
        print("Groups at the start of group phase:")
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
        window = GroupWindow(self.groups[i])
        self.groups[i] = window.classify()
        window.root.destroy()

    def classifyGroups(self):
        for i in range(self.nGroups):
            self.classifyGroup(i)
        print("ranking of groups after group phase:")
        self.printGroups(with_ranking=True)
    
    def reorderParticipants(self):
        # reorder participants in this way:
        # first the winner of each group
        # then second of each group
        # ...
        newOrder = []
        # the first groups can have one more participant
        for i in range(len(self.groups[0])):
            for group in self.groups:
                if i < len(group):
                    newOrder.append(group[i])
        self.participants = newOrder
        self.printRanking()
    
    def manageCompetition(self):
        self.makeGroups()
        self.classifyGroups()
        self.reorderParticipants()
        


if __name__ == "__main__":
    nameList = ["comme un boomerang", "la marseillaise", "grand pianola music", "wor"]
    manager = GroupStageManager(nameList, 2)
    manager.manageCompetition()