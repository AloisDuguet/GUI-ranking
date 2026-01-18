# on copie la liste dans le dossier et on donne son chemin à empliste
# on crée une matrice carrée qui contiendra les résultats des matchs, avec des zéros partout
# on tire un élément de Sn avec n le nombre de match aller (n(n-1)/2)
# on fait les matchs dans l'ordre donné par l'élément de Sn en notant les résultats aux deux endroits du tableau en même temps
# on calcule le score de chacun puis sa place, et on affiche la liste donnant les places, scores et nom des musiques

# os.listdir('path') renvoie les fichiers et dossiers de path dans une liste
# os.path.isfile(path) renvoie True si path désigne un fichier existant
# Pour supprimer un fichier, il suffit d'utiliser la fonction os.remove(path)
# os.renames(src, dst) permet de renommer le fichier src en dst tout en créant
# si nécessaire les répertoires contenant le fichier de destination

import os
import sys
import numpy.random
import time

def tirage_calendrier(n):
    """n est le nombre d'éléments dans le championnat"""
    nbmatch = int(n*(n-1)/2)
    sym = numpy.random.choice(numpy.arange(nbmatch), size=nbmatch, replace=False) + 1
    calendrier = []
    for i in sym:
        j = i
        k = 1
        while j > n-k:
            j = j-n+k
            k = k+1
        calendrier.append([k,j+k])
    return calendrier
    
path = input("Quel est le chemin d'accès de la liste?\n")
#path = "D:\Music\Moi\Anciennes musiques préférées\Classement par tournoi\liste_test"
#root = "D:\Music\Moi\Anciennes musiques préférées\Classement par tournoi\liste_test"
root = input("A quel endroit enregistrer le fichier txt contenant le classement?\n")
l = os.listdir(path)

n = len(l)
calendrier = tirage_calendrier(n)
resultat = numpy.zeros((n,n))
#print(calendrier)

for match in calendrier:
    choix = input("qui gagne, 1 pour premier, autre pour second:\n\t{}\n\t{}\n".format(l[match[0]-1], l[match[1]-1]))
    if choix == '1':
        resultat[match[0]-1,match[1]-1] = 1
    else:
        resultat[match[1]-1,match[0]-1] = 1

points = numpy.sum(resultat,1)
#print(resultat)
#print(points)
recap_points = []
for i in range(n):
    ligne = l[i]
    ligne = ligne.rpartition('.mp3')[0]
    recap_points.append([int(points[i]), '{}'.format(ligne)])
classement = sorted(recap_points, key = lambda x : x[0], reverse = True)
#print(classement)
texte = ''
for i in range(n):
    ligne = '{}'.format(classement[i][0]) + ' - ' + classement[i][1]
    texte = texte + ligne + '\n'

t = time.localtime()
current_time = time.strftime("%d_%m_%Y_%Hh%Mmin%S", t)
nom = path + current_time + '.txt'
fichier = open(nom, "w")
val = fichier.write(texte)
if val != len(texte):
    print("euh ça a pas tout écrit dans le fichier...\nil manque {} caractères".format(len(texte) - val))
fichier.close()
print("Résultats :\n{}".format(texte))
