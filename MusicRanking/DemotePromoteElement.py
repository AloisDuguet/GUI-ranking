from SlideElement import *

class DemotePromoteElement(SlideElement):
    def __init__(self, master, name, callbackPromote, callbackDemote, ranking):
        SlideElement.__init__(self, master, name, callbackPromote, callbackDemote,"undefined")
        self.rankingLabel.grid_remove()
        self.up["text"] = "promote"
        self.down["text"] = "demote"
        self.toBePromoted = False
        self.toBeDemoted = False

if __name__ == "__main__":
    root = tk.Tk()
    demotePromoteElement = DemotePromoteElement(root, "testDemotePromoteElement", lambda x: x, lambda x: x)
    demotePromoteElement.frame.pack()
    root.mainloop()