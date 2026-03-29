import math

class ListToRank:
    """A class to describe the list of competitors, the name of this ranking,
    and the criterion with which to rank the competitors"""
    def __init__(self, competitors = [], name = "", criterion = "What do you prefer?"):
        self.competitors = competitors
        self.name = name
        self.criterion = criterion
        self.ranking = dict()

    def resetRanking(self):
        self.ranking = dict()

    def produceKey(self, lowerValue, upperValue = "UNK"):
        if upperValue == "UNK":
            upperValue = lowerValue
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
    
    def produceStringRanking(self):
        orderedKeys = self.orderRankingKeys()
        # print values of each key in increasing order
        rankingString = ""
        for key in orderedKeys:
            values = self.ranking[key]
            for value in values:
                rankingString += f"{key}: {value}\n"
        return rankingString

    def printRanking(self):
        if len(self.ranking.keys()) == 0:
            print("No ranking")
        else:
            orderedKeys = self.orderRankingKeys()
            # print values of each key in increasing order
            for key in orderedKeys:
                values = self.ranking[key]
                for value in values:
                    print(f"{key}: {value}")
    
    def fillRankingFromCompetitors(self):
        # fill in ranking from order of self.competitors
        for i,competitor in enumerate(self.competitors):
            self.ranking[f"{i}"] = [competitor]
    
    def fillCompetitorsFromRanking(self):
        # fill in competitors from ranking, in ranking order (best to worst)
        self.competitors = []
        orderedKeys = self.orderRankingKeys()
        for key in orderedKeys:
            values = self.ranking[key]
            if type(values) == list:
                for value in values:
                    self.competitors.append(value)
            elif type(values) == str:
                self.competitors.append(values)
            else:
                raise("unknown type of value in ListToRank.ranking:\n{self.ranking}")

    def describe(self):
        print(f"list: {self.name}\n" \
        f"criterion: {self.criterion}\n" \
        f"list of competitors:\n{self.competitors}\n" \
        "ranking:")
        self.printRanking()
        print(self.ranking)