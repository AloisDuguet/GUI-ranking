from GroupWindow import *
from DemotePromoteElement import *

class DemotePromoteWindow(GroupWindow):
    def __init__(self, nameList):
        GroupWindow.init(self, nameList, DemotePromoteElement, self.promote, self.demote)
        self.slideElements[0].up.state(['!disabled'])
        self.slideElements[self.nSlideElements-1].down.state(['!disabled'])
        self.toBePromoted = []
        self.toBeDemoted = []

        # define styles depending on whose option is selected
        style = ttk.Style()
        style.configure("Promoted.TButton", background="green")
        style2 = ttk.Style()
        style2.configure("Demoted.TButton", background="red")
        style3 = ttk.Style()
        style3.configure("notPressed.TButton")
    
    def promote(self, element):
        if element.toBePromoted == False:
            element.toBePromoted = True
            element.toBeDemoted = False
            print(f"{element.getName()} will be promoted")
            element.up.config(style="Promoted.TButton")
            element.down.config(style="notPressed.TButton")
        else:
            element.toBePromoted = False
            element.up.config(style="notPressed.TButton")

    def demote(self, element):
        if element.toBeDemoted == False:
            element.toBePromoted = False
            element.toBeDemoted = True
            print(f"{element.getName()} will be demoted")
            element.down.config(style="Demoted.TButton")
            element.up.config(style="notPressed.TButton")
        else:
            element.toBeDemoted = False
            element.down.config(style="notPressed.TButton")

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