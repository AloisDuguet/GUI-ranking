import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog as fd

from Helpers import *
from Parsers import *

class ChooseListWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Selection of competitors")
        self.frame = ttk.Frame(self.root,
                               relief='raised')
        
        # explanation on top
        explanationMessage = "Choose a list of competitors through one of the following means."
        self.explanation = tk.Message(self.frame,
                                      text=explanationMessage, 
                                      width = 800, 
                                      font=(tk.font.nametofont("TkTextFont").actual()["family"],10))
        self.explanation.pack()

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
                                        command=self.getList)
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

    def getList(self):
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
        return self.list