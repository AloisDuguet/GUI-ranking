import tkinter as tk
from tkinter import ttk
import os

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

def getListFromFolder(key=".jpg"):
    # returns a list with all elements of folder
    folder = inputPath("Enter path to folder with list to build")
    list = os.listdir(folder)
    filteredList = []
    for el in list:
        if key not in el:
            filteredList.append(el)
    return filteredList

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