import tkinter as tk
from tkinter import ttk

class ResultWindow:
    def __init__(self, root, participants):
        self.root = root
        self.participants = participants
        self.text = tk.Text(self.root,
                            height=len(self.participants),
                            relief='raised')

        # fill in participants with corresponding ranking
        self.elements = []
        self.rankings = []
        for i in range(len(self.participants)):
            print("inserting one competitor at rank {} in position {}.0".format(i+1,i+1))
            self.text.insert(index='{}.0'.format(i+1),
                             chars="{} - {}\n".format(i+1,self.participants[i]))
        # disable editing to keep the ranking intact
        self.text['state'] = 'disabled'

        # test coordinates in self.text
        # print("copy of text from line 30 on:")
        # self.copy = self.text.get('10.0',tk.END)
        # print(type(self.copy))
        # print(self.copy)
            
        # add button to close this window
        self.closeButton = ttk.Button(self.root,
                                      text="close ranking",
                                      command=self.root.quit)
        
        # add vertical scrollbar
        self.scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.text.yview)
        self.text['yscrollcommand'] = self.scrollbar.set
        
    def showResults(self):
        self.text.pack(fill="both", expand=True)
        self.closeButton.pack()
        self.root.mainloop()
        self.text.destroy()
        self.closeButton.destroy()
        return 0
