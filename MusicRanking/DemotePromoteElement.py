from SlideElement import *

class DemotePromoteElement(SlideElement):
    def __init__(self, master, name, callbackPromote, callbackDemote):
        SlideElement.__init__(self, master, name, callbackPromote, callbackDemote)
        self.up["text"] = "promote"
        self.down["text"] = "demote"

if __name__ == "__main__":
    root = tk.Tk()
    demotePromoteElement = DemotePromoteElement(root, "testDemotePromoteElement", lambda x: x, lambda x: x)
    demotePromoteElement.frame.pack()
    root.mainloop()