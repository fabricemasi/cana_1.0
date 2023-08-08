import shutil

from . import colo
from past.builtins import raw_input

import os


def affiche_liste(titre, lignes, largeur=50, prefixe="", prefixe_only_1st_lign=1, clear=0):
    # Ligne 1 : ╭───────────────╮

    # Ligne 2 : │               │

    # Ligne 3 : ├───────────────┤

    # Ligne 4 : │               │
    #           │               │
    #           │               │
    #           │               │

    # Ligne 5:  ╰───────────────╯

    tableau = []
    decalage_liste = 1

    # Rafraichissement de l'acran ou non :
    # ========================================================

    if clear :
        os.system("clear")

    # Petit ajustement de largeur si necessaire :
    # ========================================================

    if len(titre) > largeur:
        largeur = len(titre)

    for l in lignes:
        if len(l) + len(prefixe) > largeur:
            largeur = len(l) + len(prefixe)

    largeur = largeur + decalage_liste * 2

    # Ligne 1 :
    # ========================================================

    ligne = "╭"
    for i in range(1, largeur + 1):
        ligne = ligne + "─"
    ligne = ligne + "╮"

    tableau.append(ligne)

    # Ligne 2 :
    # ========================================================

    espacement_total = largeur - len(titre)
    espacement_gauche = int(espacement_total / 2)
    espacement_droit = largeur - espacement_gauche - len(titre)

    ligne = "│"
    for i in range(1, espacement_gauche + 1):
        ligne = ligne + " "
    ligne = ligne + titre
    for i in range(1, espacement_droit + 1):
        ligne = ligne + " "
    ligne = ligne + "│"

    tableau.append(ligne)

    # Ligne 3 :
    # ========================================================

    ligne = "├"
    for i in range(1, largeur + 1):
        ligne = ligne + "─"
    ligne = ligne + "┤"

    tableau.append(ligne)

    # Ligne 4 :
    # ========================================================
    n = 0
    for l in lignes:
        n = n + 1
        if n == 1 or prefixe_only_1st_lign == 0:
            espacement_gauche = decalage_liste
            espacement_droit = largeur - len(l) - len(prefixe) - espacement_gauche

            ligne = "├"
            for i in range(1, espacement_gauche + 1):
                ligne = ligne + " "
            ligne = ligne + prefixe + l
            for i in range(1, espacement_droit + 1):
                ligne = ligne + " "
            ligne = ligne + "│"
        else:
            espacement_gauche = decalage_liste + len(prefixe)
            espacement_droit = largeur - len(l) - espacement_gauche

            ligne = "├"
            for i in range(1, espacement_gauche + 1):
                ligne = ligne + " "
            ligne = ligne + l
            for i in range(1, espacement_droit + 1):
                ligne = ligne + " "
            ligne = ligne + "│"

        tableau.append(ligne)

    # Ligne 5 :
    # ========================================================

    ligne = "╰"
    for i in range(1, largeur + 1):
        ligne = ligne + "─"
    ligne = ligne + "╯"

    tableau.append(ligne)

    # Resultat :
    # ========================================================

    for t in tableau:
        print(t)


def verif_existence(path, saisie):
    liste = os.listdir(path)

    if saisie in liste:
        return 1
    else:
        return 0

