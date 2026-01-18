# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:20:30 2019

@author: alois
"""

"""# on copie la liste dans le dossier et on donne son chemin à empliste


# on crée un dossier contenant le pivot 
# on crée deux listes qui s'appellent mieux et pas mieux, qui vont être remplies
# par les trucs mieux et pas mieux que le pivot
os.makedirs(newroot + '/pivot ' + pivot)
os.makedirs(newroot + '/pivot ' + pivot + '/mieux')
os.makedirs(newroot + '/pivot ' + pivot + '/pas mieux')
#print("source :\n{}\ndestination :\n{}".format(root + '/' + pivot, newroot + '/pivot ' + pivot + '/' + pivot))
shutil.move(root  + '/liste/' + pivot, newroot + '/pivot ' + pivot + '/' + pivot)"""

"""# on crée un dossier dans lequel sera fait le classement
t = time.localtime()
current_time = time.strftime("%d_%m_%Y_%Hh%Mmin%S", t)
os.makedirs(root + '/classement {}'.format(current_time))"""
# os.listdir('path') renvoie les fichiers et dossiers de path dans une liste
# os.path.isfile(path) renvoie True si path désigne un fichier existant
# Pour supprimer un fichier, il suffit d'utiliser la fonction os.remove(path)
# os.renames(src, dst) permet de renommer le fichier src en dst tout en créant
# si nécessaire les répertoires contenant le fichier de destination

print("work in conda environment python311 in anaconda prompt")

import os
import sys
import numpy.random
import time

def match(el1,el2):
    choice = 0
    while choice not in ["1","2"]:
        choice = input("qui gagne? 1 pour premier, 2 pour second:\n\t{}\n\t{}\n".format(el1,el2))
    return int(choice)

def matchMatrix(m, l, i, j):
    choice = match(l[i],l[j])
    if choice == 1:
        m[i,j] = 1
        m[j,i] = 0
    else:
        m[i,j] = 0
        m[j,i] = 1
    return 0

def pivotage(l):
    taille = len(l)
    alea = numpy.random.randint(0,taille)
    pivot = l[alea]    
    # on crée deux listes l1 et l2 qui vont contenir les éléments mieux et
    # pas mieux que le pivot
    l1 = []
    l2 = []
    # on fait les comparaisons avec le pivot
    l.remove(pivot)
    for el in l:
        choice = match(el,pivot)
        if choice == 1:
            l1.append(el)
        else:
            l2.append(el)
    if len(l1) >= 2:
        l1 = pivotage(l1)
    if len(l2) >= 2:
        l2 = pivotage(l2)
    l = l1 + [pivot] + l2
    return l

def makeEqualLevelGroups(l, nGroups):
    n = len(l)
    groups = []
    for i in range(nGroups):
        groups.append([])
    indexGroup = 0
    elementPerGroup = int(numpy.floor(n / nGroups))
    biggerGroups = n % nGroups # the first few groups are bigger by one
    cpt = 0
    for indexGroup in range(nGroups):
        bonus = 0
        if indexGroup < biggerGroups:
            bonus = 1
        for i in range(elementPerGroup+bonus):
            groups[indexGroup].append(l[cpt])
            cpt += 1
    return groups

def makeUnequalLevelGroups(l, nGroups):
    groups = []
    for i in range(nGroups):
        groups.append([])
    indexGroup = 0
    for el in l:
        groups[indexGroup].append(el)
        indexGroup = (indexGroup+1)%nGroups
    return groups

def handleTies(matrix, equalScores, ranking):
    # handle ties in equalScores with direct confrontation in matrix and update ranking
    # if not sufficient, decide at random

    # I don't want to code it now, so it just do as in the initial order
    for el in equalScores:
        ranking.append(el)
    return 0

def allRound(l):
    # all-round, tie decided with direct confrontation (not implemented right now)
    n = len(l)
    m = numpy.zeros([n,n])
    # make all the matches
    for i in range(n):
        for j in range(i+1,n):
            matchMatrix(m,l,i,j)
    # compute points
    points = []
    for i in range(len(l)):
        points.append(sum(m[i,:]))
    # handle ties
    ranking = []
    for i in range(n-1,-1,-1):
        equalScores = []
        for index in range(len(points)):
            if points[index] == i:
                equalScores.append(index)
        if len(equalScores) == 1:
            ranking.append(equalScores[0])
        else:
            handleTies(m,equalScores,ranking)
    # rebuild l with ranking
    newL = []
    for el in ranking:
        newL.append(l[el])
    return newL

def showGroups(groups):
    for i in range(len(groups)):
        print("group ", i, ":\n", groups[i])

def preliminaryGroupStage(l,nGroups):
    # make random groups
    numpy.random.shuffle(l)
    groups = makeUnequalLevelGroups(l, nGroups) # equal or unequal groups do not matter since we just shuffled
    print("initial groups:\n")
    showGroups(groups)
    # make an all-round tournament with each group
    for i in range(nGroups):
        groups[i] = allRound(groups[i])
    print("groups after all-round:\n")
    showGroups(groups)
    # rebuild list with first all winners, then all seconds, ...
    newL = []
    for i in range(len(groups[0])):
        for j in range(nGroups):
            if len(groups[j]) > 0:
                newL.append(groups[j].pop(0))
    print("end of preliminary stage:\n", newL)
    return newL

def demotion(groups, groupNumber, loser):
    indexLoser = groups[groupNumber].index(loser)
    demotedTeam = groups[groupNumber].pop(indexLoser)
    groups[groupNumber+1].insert(0,demotedTeam)
    return 0

def promotion(groups, groupNumber, winner):
    indexWinner = groups[groupNumber].index(winner)
    promotedTeam = groups[groupNumber].pop(indexWinner)
    groups[groupNumber-1].append(promotedTeam)
    return 0

def selectLeagueLoserAndWinner(group, noLoser = False, noWinner = False):
    print()
    for i in range(len(group)):
        print("{}:\t".format(i+1), group[i])
    loser,winner = "fake item","fake item"
    if not(noLoser):
        indexLoser = -1
        while indexLoser < 0 or indexLoser > len(group)-1:
            c = input("who is demoted ? ") # add safety guards so that only numbers from 1 to n are allowed. If I miss one time, it errors...
            try:
                indexLoser = int(c)-1
            except:
                indexLoser = -1
                print("only integers between 0 and", len(group), "authorized")
        loser = group[indexLoser]
    if not(noWinner):
        indexWinner = -1
        while indexWinner < 0 or indexWinner > len(group)-1:
            c = input("who is promoted ? ") # add safety guards so that only numbers from 1 to n are allowed. If I miss one time, it errors...
            try:
                indexWinner = int(c)-1
            except:
                indexWinner = -1
                print("only integers between 0 and", len(group), "authorized")
        winner = group[indexWinner]
    return loser,winner

def simulSeason(groups):
    # select one team promoted and one team demoted for each league except the highest and lowest ones
    nGroups = len(groups)
    losers = []
    winners = []
    # get winners and losers for all leagues, starting from the worse-ranked league
    _,winner = selectLeagueLoserAndWinner(groups[nGroups-1], True, False)
    losers.append(-1)
    winners.append(winner)
    for leagueRank in range(nGroups-2,0,-1):
        loser,winner = selectLeagueLoserAndWinner(groups[leagueRank])
        losers.append(loser)
        winners.append(winner)
    loser,_ = selectLeagueLoserAndWinner(groups[0], False, True)
    losers.append(loser)
    winners.append(-1)
    # apply promotions and demotions, starting from the worse-ranked league
    promotion(groups, nGroups-1, winners[0])
    cpt = 1 # index of winners and losers in the eponym lists
    for leagueRank in range(nGroups-2,0,-1):
        demotion(groups, leagueRank, losers[nGroups-leagueRank-1])
        promotion(groups, leagueRank, winners[nGroups-leagueRank-1])
    demotion(groups, 0, losers[nGroups-1])
    return groups

def rebuildRankingListFromGroups(groups):
    # the first are the elements of groups[0], then groups[1], ...
    l = []
    for groupNumber in range(len(groups)):
        for j in range(len(groups[groupNumber])):
            l.append(groups[groupNumber].pop(0))
    return l

def mainGroupStage(l, nGroupsMain, numberSeasons = 10):
    groups = makeEqualLevelGroups(l,nGroupsMain) # l already partially ordered, so equal-level groups
    print("main group stage - initial groups from best to worst league:")
    showGroups(groups)
    for i in range(numberSeasons):
        print("\nSeason ", i+1, ":")
        simulSeason(groups)
    print("main group stage - after seasons:")
    showGroups(groups)
    # rebuild l from groups
    l = rebuildRankingListFromGroups(groups)
    return l

def manualInsertionSort(l):
    # insertion sort where the bigger element is decided via prompt
    newL = [l.pop(0)] # sorted list
    for el in l:
        # compare el with elements in newL starting from the last one and stopping at the first time el is not the best
        pos = len(newL) # points one element too far because of while loop
        choice = 1 # corresponds to win of el
        while choice == 1 and pos > 0:
            pos -= 1
            choice = match(el,newL[pos])
        if choice != 1: # el lost against newL[pos]
            newL.insert(pos+1, el) # insert after newL[pos]
        else: # choice == 1 and thus pos == 0, so el beat everyone
            newL.insert(0, el)
        
    return newL

def fineTuneStage(l):
    print("start of end stage with:\n", l)
    l = manualInsertionSort(l)
    return l

def multiGroupStage(l, nGroupsMain, nGroupsPrel = 5, numberSeasons = 10):
    # tournament in multiple phases:
    # 1 - preliminary phase: class randomly into equal sized groups in which an all-round tournament is done.
    #                        return a list with first all winners, followed by all second, ... (order amongst equally-placed unimportant)
    # 2 - main group stage:  from a pre-ordered list, create n equally-sized leagues based on initial ranking. 
    #                        Each 'season' the best of the league is promoted and the last is demoted
    # 3 - fine-tune stage:   Maybe make an all-round with the x first to have a precise top, and others are ranked like 11-20th, ...
    l = preliminaryGroupStage(l,nGroupsPrel)
    l = mainGroupStage(l, nGroupsMain, numberSeasons)
    l = fineTuneStage(l)
    return l

def multiGrade(l):
    # idea: grade all candidates on multiple topics
    # return the sorted list (decreasing) corresponding to the sum of grades for each candidate and each grade
    # 1 - select grade rules (topics on which the grades are given, such as sentimental value)
    # 2 - ask grades (from 0 to 10?)
    # 3 - build sum of grades
    # 4 - order
    # step 1
    rules = getGradeRules()
    # step 2
    nCandidates = len(l)
    nGrades = len(rules)
    mat = zeros(nCandidates,nGrades)
    for i in range(nGrades):
        rule = rules[i]
        for j in range(nCandidates):
            el = l[j]
            mat[i,j] = input("{} for {}:\n")
    # step 3
    return 0


def renommage(l, path):
    """l est la liste classée, path est le chemin d'accès à la liste qui vient
    d'être classée"""
    for i in range(len(l)):
        os.rename(path + '/' + l[i], path + '/{} - '.format(i+1) + l[i])

def ecrivage(l, path):
    cl = ''
    for i in range(len(l)):
        cl += '{} - '.format(i+1) + l[i] + '\n'
    t = time.localtime()
    current_time = time.strftime("%d_%m_%Y_%Hh%Mmin%S", t)
    nom = path + current_time + '.txt'
    fichier = open(nom, "w")
    val = fichier.write(cl)
    if val != len(cl):
        print("euh ça a pas tout écrit dans le fichier...\nil manque {} caractères".format(len(cl) - val))
    fichier.close()
    print("classement :\n{}".format(cl))
    return 0

# il faut que les trucs à classer soient dans un fichier de nom 'liste' de racine root
# on copie la liste et on choisit le pivot
#root = os.path.dirname(sys.modules['__main__'].__file__)
#l = os.listdir(root + '/liste')

def get_list():
    path = input("Quel est le chemin d'accès de la liste?\n")
    root = input("A quel endroit enregistrer le fichier txt contenant le classement?\n")
    l = os.listdir(path)
    newL = []
    for index in range(len(l)):
        if "AlbumArt" not in l[index] and "Folder" not in l[index] and "classement" not in l[index]:
            newL.append(l[index])
    l = newL
    return path,root,l

def choose_sort(l):
    choice = input("\n\nsélection du tri:\n" \
    "1 pour quick sort\n" \
    "2 pour multiple group stage\n")
    if choice == "1":
        l = pivotage(l)
    elif choice == "2":
        print("multiple group stage not fully implemented")
        nGroupsPrel = int(input("number of groups in preliminary stage?\n"))
        if nGroupsPrel > len(l):
            print("too high value proposed for number of groups in preliminary stage. Set to number of elements to rank.")
            nGroupsPrel = len(l)
        nGroupsMain = int(input("number of groups in main stage?\n"))
        if nGroupsMain > int(numpy.floor(len(l)/2)):
            print("too high value proposed for number of groups in main stage.")
            print("Set to ", int(numpy.floor(len(l)/2)), " so that there are at least two elements in each group")
            nGroupsMain = int(numpy.floor(len(l)/2))
        numberSeasons = int(input("number of seasons?\n"))
        l = multiGroupStage(l,nGroupsMain,nGroupsPrel,numberSeasons)
    return l

def save_list(path,root,l):
    choice = input("voulez-vous renommer les fichiers que vous avez trié?\ntaper oui pour le faire\n")
    if choice == 'oui':
        renommage(l, path)
    ecrivage(l, root + '/classements')
    return 0

def main_sort():
    path,root,l = get_list()
    print("path", path, "l", l)
    l = choose_sort(l)
    save_list(path,root,l)
    return 0

main_sort()