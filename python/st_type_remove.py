# coding: utf-8
# !/usr/bin/python
import os
import sys

from api.cana_api import *
from api.AFAC import couleur
from api.main_color import color

from api.main_api import *

ROUGE = os.environ["ROUGE"]

args = sys.argv[1]

RC = os.environ['ROOT_CHANTIER']
cl = color()


# On nettoie les args (on split.sh par "," et "/")
# et on cree une nouvelle liste clean "arguments"

args = args.split(',')
arguments = []

for arg in args:
    arg = arg.split('/')
    for a in arg:
        if a != "":
            arguments.append(a)


# On cree la liste des types de proj :
liste_types = os.listdir(RC)


# Nombre d'arguments :
nb = arguments.__len__()


# Aucun argument :
# ===============================================================
if nb == 0:
    # On affiche la liste :
    affiche_liste("Liste des types de proj", liste_types, 30, "", 0, 1)

    # Saisie 1 :
    print(cl.JAUNE() + "\nQuel type de proj vous voulez supprimer?\n" + cl.NEUTRE())

    reponse = raw_input()
    print("")

    tp = reponse
    path = RC + "/" + tp

    # Saisie 2 :
    if not os.path.exists(path):
        print(cl.JAUNE() + "Le repertoire indique n'existe pas. Commande annulee." + cl.NEUTRE())
    else:
        print(
            cl.JAUNE() + "Etes vous sure de vouloir supprimer le repertoire " +
            cl.ROUGE() + cl.GRAS() + cl.BLINK() + tp + cl.NEUTRE() + cl.JAUNE() + " et son contenu?")
        print(cl.NEUTRE())

        reponse = raw_input()
        print("")

        if reponse == "o" or reponse == "y":
            try:
                shutil.rmtree(path)
            except:
                print(cl.JAUNE() + "Erreur, aucun repertoire supprime." + cl.NEUTRE())
            finally:
                print(cl.JAUNE() + "Le repertoire " + cl.ROUGE() + tp + cl.JAUNE() + " a ete supprime." + cl.NEUTRE())

