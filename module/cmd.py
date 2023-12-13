import os
import sys
import builtins
import storage
import module
import board
from analogio import AnalogIn

def cls():
    for loop in range(0,20):
        print()

def nano(chemin):
    #recupération du chemin
    size = len(chemin)
    if size > 5:
        chemin = chemin[5:size]
        module.nano.nano_call(chemin)
    else:
        print("Entrée un nom de fichier 2")

def ls(chemin):
    #recupération du chemin
    size = len(chemin)
    chemin = chemin[3:size]

    #récupération de la liste de fichier
    try:
        file_list = os.listdir(chemin)

        #récupéraion de la longeur du tableau
        size = len(file_list)

        #renvoie des dossiers
        for loop in range(0,size):
            if not "." in file_list[loop]:
                if not "System Volume Information" in file_list[loop]:
                    print(file_list[loop])
        
        #renvoie des fichier
        for loop in range(0,size):
            if "." in file_list[loop]:
                if file_list[loop][0:1] != '.':
                    print(file_list[loop])

    #gestion des exception
    except Exception as err:
        print("*ERREUR* Exeception:",str(err))

def rmdir(chemin):
    #recupération du chemin
    size = len(chemin)
    chemin = chemin[6:size]

    #effacement du dossier
    try:
        #effacement du dossier
        storage.remount("/",False)
        os.rmdir(chemin)
        storage.remount("/",True)
    
    #gestion des exception
    except Exception as err:
        print("*ERREUR* Exeception:",str(err))

def rm(chemin):
    #recupération du chemin
    size = len(chemin)
    chemin = chemin[3:size]

    #effacement du dossier
    try:
        #effacement du dossier
        storage.remount("/",False)
        os.remove(chemin)
        storage.remount("/",True)
    
    #gestion des exception
    except Exception as err:
        print("*ERREUR* Exeception:",str(err))

def cd(chemin):
    #recupération du chemin
    size = len(chemin)
    chemin = chemin[3:size]

    #changement du dossier
    try:
        os.chdir(chemin)
    #gestion des exception
    except Exception as err:
        print("*ERREUR* Exeception:",str(err))

def mkdir(chemin):
    #recupération du chemin
    size = len(chemin)
    chemin = chemin[6:size]

    #changement du dossier
    try:
        storage.remount("/",False)
        os.mkdir(chemin)
    except Exception as err:
        print("*ERREUR* Exeception:",str(err))

def voltage():
    #retourne voltage batterie
    #attache pin
    #CALIBRATION NESSECAIRE

    batt_in = AnalogIn(board.IO4)

    #changement de la référence
    print(batt_in.reference_voltage)

    #calcul voltage
    voltage = batt_in.value * 3.3 / 65536

    #relachement pin
    batt_in.deinit()

    #retourne le voltage
    return voltage

def batt_charge():
    #4.2V < x = 100%  
    #3.3V > x = 0%
    #CALIBRATION NESSECAIRE
    
    max = 4.2
    min = 3.3

    #attache pin
    batt_in = AnalogIn(board.IO4)

    #calcul charge
    charge = 100 / (max - min) * (batt_in.value * 3.3 / 65536 - min) 

    #relachement pin
    batt_in.deinit()

    #retourne la charge en %
    return charge