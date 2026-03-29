from GroupWindow import *
from DemotePromoteElement import *

class DemotePromoteWindow(GroupWindow):
    def __init__(self, root, listToRank, nameGroup):
        explanationMessage = "To promote a competitor to the immediately stronger division in the next season, click the corresponding 'promote' button.\n" \
            "To demote a competitor to the immediately weaker division in the next season, click the corresponding 'demote' button.\n" \
            "Multiple competitors can be demoted and promoted, so the number of competitors per group may vary.\n" \
            "In the strongest division, promotion is not possible. In the worst division, demotion is not possible. " \
            "When done, click the 'validate ranking' to confirm this ranking."
        self.listToRank = listToRank
        self.toBePromoted = []
        self.toBeDemoted = []

        self.initUpperFrame(root, nameGroup, explanationMessage)
        self.initLowerFrame(root, DemotePromoteElement, self.promote, self.demote)

    def widgetStyles(self):
        GroupWindow.widgetStyles(self)
        # define styles depending on whose option is selected
        style = ttk.Style()
        style.configure("Promoted.TButton", background="green")
        style2 = ttk.Style()
        style2.configure("Demoted.TButton", background="red")
        style3 = ttk.Style()
        style3.configure("notPressed.TButton")

    def disableButtons(self):
        # no buttons to disable at initialization
        # this class does not know the division of the group
        # noPromote() and noDemote() are called from above
        pass
    
    def promote(self, element):
        if element.toBePromoted == False:
            element.toBePromoted = True
            element.toBeDemoted = False
            element.up.config(style="Promoted.TButton")
            element.down.config(style="notPressed.TButton")
        else:
            element.toBePromoted = False
            element.up.config(style="notPressed.TButton")

    def demote(self, element):
        if element.toBeDemoted == False:
            element.toBePromoted = False
            element.toBeDemoted = True
            element.down.config(style="Demoted.TButton")
            element.up.config(style="notPressed.TButton")
        else:
            element.toBeDemoted = False
            element.down.config(style="notPressed.TButton")

    def noPromotion(self):
        # called by a higher level if it is the best group
        for element in self.slideElements:
            element.up.state(["disabled"])

    def noDemotion(self):
        # called by a higher level if it is the worst group
        for element in self.slideElements:
            element.down.state(["disabled"])

    def validateRanking(self):
        toStay = []
        for element in self.slideElements:
            if element.toBePromoted:
                self.toBePromoted.append(element.getName())
            elif element.toBeDemoted:
                self.toBeDemoted.append(element.getName())
            else:
                toStay.append(element.getName())
        self.slideElements = toStay
        self.root.quit()
    
    def classify(self):
        ranking = GroupWindow.classify(self)
        return [self.toBeDemoted, self.slideElements, self.toBePromoted]
    
