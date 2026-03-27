class ListToRank:
    """A class to describe the list of competitors, the name of this ranking,
    and the criterion with which to rank the competitors"""
    def __init__(self, competitors = [], name = "", criterion = "What do you prefer?"):
        self.competitors = competitors
        self.name = name
        self.criterion = criterion
    
    def describe(self):
        print("list: {}\n" \
        "criterion: {}\n" \
        "list of competitors:\n{}".format(self.name, self.criterion, self.competitors))