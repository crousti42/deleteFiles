# Script de suppressions de fichiers dont la liste est récupérée dans un fichier input
# Version 1.0
# Author gbrugere
# coding: utf8

import datetime
import os

#  --------------- Configuration du script 

inputFilename  = "inputFile.txt"

#  --------------- 

inputFilePath = os.getcwd()+"\\"+inputFilename

date = datetime.datetime.now()

print("Debut du script - "+str(date)+"\n")

# On vérifie que le fichier existe bien
if not os.path.isfile(inputFilePath):
    print("Erreur: Le fichier "+inputFilePath+" n'existe pas.")
    exit(1)

inputFile = open(inputFilePath, "r")

for currentLine in inputFile:
    
    fileTodeletePath = currentLine.rstrip('\n')
    
    if os.path.exists(fileTodeletePath):
        print(fileTodeletePath+" Suppression du fichier")    
        #os.remove(fileTodeletePath)
    else:
        print(fileTodeletePath+" Impossible de supprimer le fichier car il n'existe pas")    

inputFile.close()

print("Fin du script - "+str(date))