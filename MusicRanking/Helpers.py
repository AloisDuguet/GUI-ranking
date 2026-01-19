def makeStringFromList(l):
    # concatenate elements with '-' between two elements
    s = ""
    separator = "/"
    for element in l:
        s += element + separator
    s = s[0:len(s)-1]
    return s

def getUniqueSuccessorID(dataFile):
    # check in dataFile how many Music instances have been declared
    # and return the successor

    # each Music saved uses exactly once the string "Music:"
    pattern = "Music:"
    with open(dataFile, "r") as file:
        countMusic = sum((line.count(pattern) >= 1) for line in file)
    print("number of Music ID: ", countMusic+1)
    return countMusic+1