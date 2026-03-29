import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog as fd

from Helpers import *
from Parsers import *
from ListToRank import *

class ChooseListWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Selection of competitors")
        self.frame = ttk.Frame(self.root,
                               relief='raised')
        
        # explanation on top
        criterionExplanation = "criterion for the ranking:"
        explanationMessage = "Choose a criterion for the ranking in the zone after '{}'; the default is 'what do you prefer?'. " \
            "Then, choose a list of competitors through one of the following means.\n" \
            "\t1) opening the content of a text file via button 'Open a file'\n" \
            "\t2) typing one competitor per line in the rectangle of text\n" \
            "\t3) a combination of the two, given that the content of a file is always added at the start of the rectangle of text.\n" \
            "When the list as displayed in the rectangle of text is done, click 'confirm list'.".format(criterionExplanation)
        self.explanation = tk.Message(self.frame,
                                      text=explanationMessage, 
                                      width = 800, 
                                      font=(tk.font.nametofont("TkTextFont").actual()["family"],10))
        self.explanation.pack()

        # criterion Label and Text
        self.labelCriterion = ttk.Label(self.frame,
                                        text=criterionExplanation)
        self.labelCriterion.pack()
        self.textCriterion = tk.Text(self.frame, height=1)
        self.textCriterion.pack()
        self.textCriterion.focus_set()

        # get list from a file
        self.labelFile = ttk.Label(self.frame,
                                   text="From a file:")
        self.labelFile.pack()
        self.buttonFile = ttk.Button(self.frame,
                                     text="Open a file",
                                     command=self.openFileIntoTextWidget)
        self.buttonFile.pack()
        
        # text
        self.labelText = ttk.Label(self.frame,
                                   text="write list of competitors here:")
        self.text = tk.Text(self.frame, height=10)
        self.labelText.pack()
        self.text.pack()

        # button to confirm list
        self.confirmButton = ttk.Button(self.frame,
                                        text="confirm list",
                                        command=self.getListToRank)
        self.confirmButton.pack()

    def openFileIntoTextWidget(self):
        filename = selectFile()
        self.list = parseListFromTxt(filename)
        #print("end of text in Text widget in position: {}".format(tk.END))
        lineNumber = 0
        print("last position in Text widget:")
        print(self.text.index('end'))
        for l in self.list:
            lineNumber += 1
            self.text.insert('{}.0'.format(lineNumber),"{}\n".format(l))
        #self.text.insert('1.0', f.readlines())

    def getListToRank(self):
        # get criterion from Text widget
        self.stringCriterion = self.textCriterion.get('1.0', tk.END)
        if self.stringCriterion[-1] == '\n':
            self.stringCriterion = self.stringCriterion[0:-1]
        print(f"stringCriterion found: {self.stringCriterion}")
        # get list from Text widget
        self.stringList = self.text.get('1.0', tk.END)
        rawList = self.stringList.split('\n')
        
        # remove empty competitors
        self.list = []
        for l in rawList:
            if l != "":
                self.list.append(l)

        print("list of competitors:")
        for i in range(len(self.list)):
            print(self.list[i])
        self.root.quit()

    def chooseList(self):
        self.frame.pack()
        self.root.mainloop()
        self.frame.destroy()
        if self.stringCriterion != "":
            return ListToRank(self.list, "", self.stringCriterion)
        else:
            return ListToRank(self.list, "")