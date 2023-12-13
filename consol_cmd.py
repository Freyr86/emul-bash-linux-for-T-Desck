#################################################################################
#                                                                               #
#   Gestion de la console circuitPython drectement avec le clavier du t-deck    #
#   Module de commande avancer                                                  #
#                                                                               #
#   Modifier par:   Freyr86                                                     #
#   Github:         https://github.com/Freyr86                                  #
#                                                                               #
#################################################################################

from sys import stdin,stdout,implementation
import sys
sys.path.append('../')

import module
from module import clavier_gestion
from module import cmd

import displayio
import os
import storage
import module

work = True

while work:
    cmd_text = clavier_gestion.input("~" + os.getcwd() + ">")
    result = None

    #clear zone commande
    if "cls" in cmd_text:
        cmd.cls()

    #appeler nano
    elif "nano" in cmd_text:
        from module import nano
        cmd.nano(cmd_text)

    #lister les dossier
    elif "ls" in cmd_text:
        cmd.ls(cmd_text)

    #effacer dossier
    elif "rmdir" in cmd_text:
        cmd.rmdir(cmd_text)
    
    #effacer fichier
    elif "rm" in cmd_text:
        cmd.rm(cmd_text)

    #changement du fichier actuel
    elif "cd" in cmd_text:
        cmd.cd(cmd_text)

    #créer un dossier
    elif "mkdir" in cmd_text:
        cmd.mkdir(cmd_text)

    #verifier la batterie
    elif "voltage" in cmd_text:
        print(cmd.voltage())

    #verification du % batterie
    elif "batt" in cmd_text:
        print(cmd.batt_charge())

    #sortie de la console
    elif "exit" in cmd_text:
        work = False


    else:
        try:
            exec('result='+cmd_text)
        except:
            try:
                exec(cmd_text)
            except Exception as err:
                print("*ERROR* Exception:",str(err))
    if result != None and cmd_text.find('=') == -1:
        print(result)