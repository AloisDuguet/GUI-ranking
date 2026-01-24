from GroupWindow import *
from DemotePromoteElement import *

class DemotePromoteWindow(GroupWindow):
    def __init__(self, nameList):
        GroupWindow.init(self, nameList, DemotePromoteElement, self.promote, self.demote)
        self.slideElements[0].up.state(['!disabled'])
        self.slideElements[0].down.state(['!disabled'])
        self.toBePromoted = []
        self.toBeDemoted = []
    
    def promote(self, element):
        element.toBePromoted = True
        element.toBeDemoted = False
        print(f"{element.getName()} will be promoted")
        # TODO: add a color to button when True

    def demote(self, element):
        element.toBePromoted = False
        element.toBeDemoted = True
        print(f"{element.getName()} will be demoted")

    def validateRanking(self):
        toStay = []
        for element in self.slideElements:
            if element.toBePromoted:
                self.toBePromoted.append(element)
                print(f"{element.getName()} is promoted")
            elif element.toBeDemoted:
                self.toBeDemoted.append(element)
                print(f"{element.getName()} is demoted")
            else:
                toStay.append(element)
                print(f"{element.getName()} stays")
        self.slideElements = toStay
        self.root.quit()
    
    def classify(self):
        self.root.mainloop()
        return self.toBeDemoted, self.slideElements, self.toBePromoted
    

if __name__ == "__main__":
    nameList = ["comme un boomerang", "la marseillaise", "grand pianola music"]
    window = DemotePromoteWindow(nameList)
    window.root.mainloop()