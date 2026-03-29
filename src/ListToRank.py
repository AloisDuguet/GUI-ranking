import math

class ListToRank:
    """A class to describe the list of competitors, the name of this ranking,
    and the criterion with which to rank the competitors"""
    def __init__(self, competitors = [], name = "", criterion = "What do you prefer?"):
        self.competitors = competitors
        self.name = name
        self.criterion = criterion
        self.ranking = dict()

    def produceKey(self, lowerValue, upperValue):
        if lowerValue != math.floor(lowerValue):
            raise("trying to produce a ranking with " \
                  "a float rank")
        if upperValue != math.floor(upperValue):
            raise("trying to produce a ranking with " \
                  "a float rank")
        if lowerValue == upperValue:
            return f"{lowerValue}"
        elif lowerValue > upperValue:
            raise("trying to produce a ranking with " \
                  "invalid range: lower value > upper value")
        else:
            return f"{lowerValue}-{upperValue}"

    def orderRankingKeys(self):
        # preparation step for printing ranking
        # get all keys
        keys = self.ranking.keys()
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

    def printRanking(self):
        orderedKeys = self.orderRankingKeys()
        # print values of each key in increasing order
        for key in orderedKeys:
            values = self.ranking[key]
            for value in values:
                print(f"{key}: {value}")
    
    def fillRankingFromCompetitors(self):
        # fill in ranking from order of self.competitors
        for i,competitor in enumerate(self.competitors):
            self.ranking[f"{i}"] = competitor
    
    def fillCompetitorsFromRanking(self):
        # fill in competitors from ranking, in ranking order (best to worst)
        self.competitors = []
        orderedKeys = self.orderRankingKeys()
        for key in orderedKeys:
            values = self.ranking[key]
            for value in values:
                self.competitors.append(value)

    def describe(self):
        print(f"list: {self.name}\n" \
        f"criterion: {self.criterion}\n" \
        f"list of competitors:\n{self.competitors}\n" \
        "ranking:")
        self.printRanking()