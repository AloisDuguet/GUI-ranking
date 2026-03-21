import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import os
from tkinter.messagebox import showinfo

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

def inputPath(message, root):
    frame = ttk.Frame(root,
                      relief='raised')
    root.title("Saving")
    frame.pack()
    label = ttk.Label(frame, text=message)
    label.pack()
    message2 = f"Current directory: {os.getcwd()}"
    label2 = ttk.Label(frame, text=message2)
    label2.pack()
    entry = ttk.Entry(frame)
    entry.pack()
    entry.focus()
    button = ttk.Button(frame, text="confirm", command=root.quit)
    button.pack()
    root.mainloop()
    filename = entry.get()
    frame.destroy()
    return filename

def selectFile():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='open a file',
        initialdir='/',
        filetypes=filetypes)
    showinfo(title='Selected file',
             message=filename)
    return filename

def openTextFile():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    f = fd.askopenfile(
        title='open a file',
        initialdir='/',
        filetypes=filetypes)
    return f
    