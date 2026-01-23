from Helpers import *

# do an IHM so that it is easy to classify? like a list vertically in which I can move the elements

class Music:
    dataFile = "listOfMusic.txt" # file in which musics are saved

    def __init__(self):
        self.ID = getUniqueSuccessorID(Music.dataFile) # unique positive number for identification
        self.name = "UNK" # name of the song
        self.artist = "UNK" # artist that composed/played the music
        self.compositionDate = -1 # year of creation of the music
        self.genres = list() # genre(s) of the music
        self.length = -1 # duration in second
        self.dateAdded = -1 # date at which this music was added to my ranking
        # add if there are lyrics or not
        # add other boolean questions to differentiate the music and see if there are characteristics often present in my favourite musics
        # structure of music I really like? like:
        # any moment is great (some math rock songs)"
        # "increasing and preparing a pinnacle moment"
        # "one specific part incredible (intro can't stop)"
        # "theme and variation"
        # "a unique sound (like organ or Zabriskie? or in C)"
    
    def enterMusicCharacteristics(self):
        self.name = input("enter name\n")

        self.artist = input("enter artist\n")

        self.compositionDate = input("enter year of composition\n")

        while True:
            genre = input("enter a genre of the music; enter 'stop' to stop\n")
            if genre != "stop":
                self.genres.append(genre)
            else:
                break

        minutes = input("enter number of minutes of song\n")
        seconds = input("enter number of seconds remaining of song\n")
        self.length = 60*int(minutes) + int(seconds)

        year = input("enter year in which it was added to the ranking\n")
        month = input("enter month in number with possible 0 (februar = 02) in which it was added to the ranking\n")
        self.dateAdded = "{}-{}".format(year,month)
        
    def print(self):
        print("Music:\n")
        print("ID: {}".format(self.ID))
        print("name: {}".format(self.name))
        print("artist: {}".format(self.artist))
        print("compositionDate: {}".format(self.compositionDate))
        print("genres: {}".format(makeStringFromList(self.genres)))
        print("length: {}".format(self.length))
        print("dateAdded: {}".format(self.dateAdded))
    
    def addMusicToDataFile(self):
        # add Music info to dataFile at the end
        
        with open(Music.dataFile, "a") as file:
            file.write("Music:\n")
            file.write("ID: {}\n".format(self.ID))
            file.write("name: {}\n".format(self.name))
            file.write("artist: {}\n".format(self.artist))
            file.write("compositionDate: {}\n".format(self.compositionDate))
            file.write("genres: {}\n".format(makeStringFromList(self.genres)))
            file.write("length: {}\n".format(self.length))
            file.write("dateAdded: {}\n".format(self.dateAdded))
            file.write("\n")
    
    def fulfill_with_input(self):
        # take a declared Music,
        # fulfill it via inputs
        # print it and add it to dataFile
        
        self.enterMusicCharacteristics()
        self.print()
        self.addMusicToDataFile()

    

# format of Music saved in dataFile:
# Music:
# {nameFirstAttribute}: {attributeValue}
# ...
# {nameLastAttribute}: {attributeValue}
# (empty line)

m1 = Music()
m1.fulfill_with_input()