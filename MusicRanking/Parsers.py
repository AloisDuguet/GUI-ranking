from Helpers import *

def parseListFromTxt(filename):
    """read one element for each line of the txt file"""

    l = []
    with open(filename, "r") as file:
        while line := file.readline():
            l.append(line.rstrip())
    
    return l

def getSpecificList(name):
    """Get a list called <name>"""
    if name == "4Mangas":
        return ["Naruto", "Full Metal Alchemist", 
                "Frieren", "One Punch Man"]
    if name == "20Mangas":
        return ["Naruto", "Full Metal Alchemist", 
                "Frieren", "One Punch Man", 
                "Devilman: crybaby", "Hunter x Hunter",
                "Dragon Ball", "Jujutsu Kaisen",
                "L'Attaque des Titans", "Bleach",
                "SaikiK", "One Piece",
                "Uncle from Another World", "Mob Psycho 100",
                "Alice in Wonderland", "Solo Leveling",
                "My Hero Academia", "Detective Conan",
                "Vinland Saga", "Golden Kamui"]

def getListFromFolder(root, key=".jpg"):
    """returns a list with all files of folder
    except the ones containing <key>"""
    folder = inputPath("Enter path to folder: each file of this folder will be in the competition", root)
    list = os.listdir(folder)
    filteredList = []
    for el in list:
        if key not in el:
            filteredList.append(el)
    
    return filteredList