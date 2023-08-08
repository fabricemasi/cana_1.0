# coding: utf-8
# !/usr/bin/python

import sys

from numpy.core.defchararray import lower

from api.fonctions import *
from api.color import color

from api.api import *

# FONCTIONS :
# ======================================================


def root(step):
    # Permet de renvoyer l'adresse selon la step (TYPE, PROJET ...)
    r = ""
    if lower(step) == "type":
        r = os.environ['ROOT_CHANTIERS']
    elif lower(step) == "projet":
        r = os.environ['ROOT_TYPE']
    elif lower(step) == "folder":
        r = os.environ['ROOT_PROJET']
    elif lower(step) == "soft":
        r = os.environ['ROOT_FOLDER'] + "/02_work/"

    return r

def create_folder(path, folder):
    cl = color()
    exist = verif_existence(path, folder)

    if exist == 1:
        STEP = tp
        ROOT_STEP = path + "/" + tp

    elif exist == 0:
        print(cl.JAUNE() + "\nLe repertoire " + cl.BLINK() + folder + cl.NEUTRE() +
              cl.JAUNE() + " n'existe pas, voulez-vous le creer?\n" + cl.NEUTRE())
        reponse = raw_input()

        if reponse == "o" or reponse == "y":
            os.mkdir(path + "/" + folder, mode=0o755)
            STEP = folder
            ROOT_STEP = path + "/" + folder
        else:
            STEP = ""
            ROOT_STEP = ""

    return (STEP, ROOT_STEP)

def run(step, nom="", mode_furtif=0):
    # arg_step      : type, projet, folder ou soft
    # nom           : nom du repertoire a selectionner
    # mode_furtif   : si =0, les affichages terminal apparaitront


    cl = color()

    # On recupere le path de l'endroit ou se positionner
    path = root(step)

    # On cree la liste des types de projet :
    liste_repertoires = os.listdir(path)

    # On verifie si l'argument n1 match avec l'un des types
    match = 0
    for l in liste_repertoires:
        if nom == "" and nom == l:
            match = 1
            break


    # On affiche la liste des steps
    affiche_liste("Liste de " + step, liste_repertoires, 30, "", 0, 1)

    # Aucun argument :
    # ===============================================================

    if nom == "":
        print(cl.JAUNE() + "\nVous pouvez setter un "+ step + " (run " + step + " + nom du " + step + ")" + cl.NEUTRE())

        # # Invite de saisie : choix du step
        # print(cl.JAUNE() + "\nSur quel " + step + " voulez-vous vous setter?\n" + cl.NEUTRE())
        # reponse = raw_input()
        #
        # if str(reponse) == "0":
        #     STEP = ""
        #     ROOT_STEP = ""
        # else:
        #     folder = reponse
        #     ret = create_folder(path, folder)
        #
        #     STEP = ret[0]
        #     ROOT_STEP = ret[1]
        #
        # # Return :
        # # ========================================================
        #
        # os.environ[step] = STEP
        # os.environ["ROOT_" + step] = ROOT_STEP
        #
        # # Pour le terminal :
        # fill_return_nb(2)
        # fill_return1(STEP)
        # fill_return2(ROOT_STEP)
        #
        # # Affichage final :
        # # ========================================================
        #
        # affiche_liste("Liste de " + step, liste_repertoires, 30, "", 0, 1)

    # 1 argument :
    # ===============================================================

    if nom != "":
        exist = verif_existence(path, nom)
        if not exist:
            create_folder(path, nom)



    # Return :
    # ========================================================

    os.environ[step] = STEP
    os.environ["ROOT_" + step] = ROOT_STEP

    # Pour le terminal :
    fill_return_nb(2)
    fill_return1(STEP)
    fill_return2(ROOT_STEP)


# SCRIPT :
# ======================================================

# On recupere les arguments
args = sys.argv[1]

# On splite (,) les arguments, et on cree une liste 'argument'
args = args.split(',')
arguments = []

# On splitte (/) a nouveau et on supprime les arguments vides
for arg in args:
    arg = arg.split('/')
    for a in arg:
        if a != "":
            arguments.append(a)

n = len(arguments)

if n == 1:
    run(arguments[0])
elif n == 2:
    run(arguments[0], arguments[1])
elif n == 3:
    run(arguments[0], arguments[1], int(arguments[2]))
