# coding: utf-8
# !/usr/bin/python

import sys

from numpy.core.defchararray import lower

from api.fonctions import *
from api.color import color

from api.api import *


def root(step):
    # Permet de renvoyer l'adresse selon la step (TYPE, PROJ ...)
    r = ""
    if lower(step) == "type":
        r = os.environ['ROOT_CHANTIER']
    elif lower(step) == "proj":
        r = os.environ['ROOT_TYPE']
    elif lower(step) == "fold":
        r = os.environ['ROOT_PROJ']
    elif lower(step) == "soft":
        r = os.environ['ROOT_FOLD'] + "/02_work/"

    return r


def run(step, mode_furtif=0, nom=""):
    # arg_step      : type, proj, fold ou soft
    # mode_furtif   : si =0, les affichages terminal apparaitront
    # nom           : nom du repertoire a selectionner

    cl = color()

    # On recupere le path de l'endroit ou se positionner
    path = root(step)

    # On cree la liste des types de proj :
    liste_repertoires = os.listdir(path)

    # On verifie si l'argument n1 match avec l'un des types
    match = 0
    for l in liste_repertoires:
        if nom == "" and nom == l:
            match = 1
            break

    # Aucun argument :
    # ===============================================================

    if nom == "":
        # On affiche la liste des steps
        affiche_liste("Liste de " + step, liste_repertoires, 30, "", 0, 1)

        # Invite de saisie : choix du step
        print(cl.JAUNE() + "\nSur quel " + step + " voulez-vous vous setter?\n" + cl.NEUTRE())
        reponse = raw_input()

        if str(reponse) == "0":
            STEP = ""
            ROOT_STEP = ""
        else:
            tp = reponse
            exist = verif_existence(path, tp)

            if exist == 1:
                STEP = tp
                ROOT_STEP = path + "/" + tp
            elif exist == 0:
                print(cl.JAUNE() + "\nLe repertoire " + cl.BLINK() + tp + cl.NEUTRE() +
                      cl.JAUNE() + " n'existe pas, voulez-vous le creer?\n" + cl.NEUTRE())
                reponse = raw_input()

                if reponse == "o" or reponse == "y":
                    os.mkdir(path + "/" + tp, mode=0o755)
                    STEP = tp
                    ROOT_STEP = path + "/" + tp
                else:
                    STEP = ""
                    ROOT_STEP = ""

        # Return :
        # ========================================================

        os.environ[step] = STEP
        os.environ["ROOT_" + step] = ROOT_STEP

        # Pour le terminal :
        fill_return_nb(2)
        fill_return1(STEP)
        fill_return2(ROOT_STEP)

        # Affichage final :
        # ========================================================

        affiche_liste("Liste de " + step, liste_repertoires, 30, "", 0, 1)

    # 1 argument :
    # ===============================================================

    if nom != "":
        pass


# On recupere les arguments
args = sys.argv[1]

# On splitte (,) les arguments, et on cree une liste 'argument'
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
    run(arguments[0], int(arguments[1]))
elif n == 3:
    run(arguments[0], int(arguments[1]), arguments[2])
