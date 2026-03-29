import tkinter as tk
from tkinter import ttk

class ResultWindow:
    def __init__(self, root, listToRank):
        self.root = root
        self.listToRank = listToRank
        self.frame = ttk.Frame(self.root,
                               width=600,
                               height=600,
                               relief='raised')
            
        # add button to close this window
        self.closeButton = ttk.Button(self.frame,
                                      text="close ranking",
                                      command=self.root.quit)
        self.closeButton.pack()

        # setup text
        self.text = tk.Text(self.frame,
                            height=len(self.listToRank.competitors))
        self.text.pack()
        rankingString = self.listToRank.produceStringRanking()
        self.text.insert(index="1.0",
                         chars=rankingString)

        # disable editing to keep the ranking intact
        self.text['state'] = 'disabled'
        
        # add vertical scrollbar
        self.scrollbar = ttk.Scrollbar(self.frame,
                                       orient=tk.VERTICAL, 
                                       command=self.text.yview)
        self.text['yscrollcommand'] = self.scrollbar.set

    def fillTextWithRanking(self):
        for i in range(len(self.listToRank.competitors)):
            print("inserting one competitor at rank {} in line {}".format(i+1,i+1))
            self.text.insert(index='{}.0'.format(i+1),
                             chars="{} - {}\n".format(i+1,self.listToRank.competitors[i]))
        
    def showResults(self):
        self.frame.pack(fill="both", expand=True)
        self.root.mainloop()
        self.frame.destroy()
        return 0
