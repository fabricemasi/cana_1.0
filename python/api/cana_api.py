# coding: utf-8
# !/usr/bin/python

import shutil

from .main_tools import *
from .cana_constants import *

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

    # Rafraichissement de l'ecran ou non :
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

            ligne = "│"
            for i in range(1, espacement_gauche + 1):
                ligne = ligne + " "
            ligne = ligne + prefixe + l
            for i in range(1, espacement_droit + 1):
                ligne = ligne + " "
            ligne = ligne + "│"
        else:
            espacement_gauche = decalage_liste + len(prefixe)
            espacement_droit = largeur - len(l) - espacement_gauche

            ligne = "│"
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


def determine_step(saisie_step=""):

    curentTyp = os.environ["TYPE"]
    curentPrj = os.environ["PROJ"]
    curentFol = os.environ["FOLD"]
    curentSft = os.environ["SOFT"]

    if saisie_step == "":

        step = ""

        if curentTyp == "":
            step = "type"
        elif curentPrj == "":
            step = "proj"
        elif curentFol == "":
            step = "fold"
        elif curentSft == "":
            step = "soft"
    else:

        step = saisie_step

    return step


def create_folder(path, folder):

    print(f"\n{jau1}Le repertoire {bli}{folder}{neu}{jau1} n'existe pas, voulez-vous le creer?{neu}\n")
    reponse = input()

    if reponse == "o" or reponse == "y":
        try:
            os.mkdir(path + "/" + folder, mode=0o755)
        except:
            print(f"\n{rou1}Erreur.{neu} Le repertoire {folder} n'a pas ete cree.{rou1} exit_pipe{neu}")
            return 0
        else:
            print(f"\n{jau1}Le repertoire {folder} a bien ete creer")
            return 1

    else:
        print(f"\n{jau1}Le repertoire {folder} n'a pas ete cree.{rou1} exit_pipe{neu}")
        return 0

# def determine_step():


def var(typ, prj, fld, sft):

    cl = color()
    neu = cl.NEUTRE()
    gra = cl.GRAS()
    gri = cl.GRIS2()
    ble = cl.BLEU()

    nb = 13

    print(f"{gri}=========================================================================={neu}")
    print(f"{gra}{gri}{'typ.current()':<{nb}}{gri} = {neu}{ble}{str(typ.current_name())}{neu}")
    print(f"{gra}{gri}{'typ.root()':<{nb}}{gri} = {neu}{ble}{str(typ.root())}")
    print(f"{gra}{gri}{'typ.path()':<{nb}}{gri} = {neu}{ble}{str(typ.path())}")
    print(f"{gri}--------------------------------------------------------------------------{neu}")
    print(f"{gra}{gri}{'prj.current()':<{nb}}{gri} = {neu}{ble}{str(prj.current_name())}{neu}")
    print(f"{gra}{gri}{'prj.root()':<{nb}}{gri} = {neu}{ble}{str(prj.root())}{neu}")
    print(f"{gra}{gri}{'prj.path()':<{nb}}{gri} = {neu}{ble}{str(prj.path())}{neu}")
    print(f"{gri}--------------------------------------------------------------------------{neu}")
    print(f"{gra}{gri}{'fld.current()':<{nb}}{gri} = {neu}{ble}{str(fld.current_name())}{neu}")
    print(f"{gra}{gri}{'fld.root()':<{nb}}{gri} = {neu}{ble}{str(fld.root())}{neu}")
    print(f"{gra}{gri}{'fld.path()':<{nb}}{gri} = {neu}{ble}{str(fld.path())}{neu}")
    print(f"{gri}--------------------------------------------------------------------------{neu}")
    print(f"{gra}{gri}{'sft.current()':<{nb}}{gri} = {neu}{ble}{str(sft.current_name())}{neu}")
    print(f"{gra}{gri}{'sft.root()':<{nb}}{gri} = {neu}{ble}{str(sft.root())}{neu}")
    print(f"{gra}{gri}{'sft.path()':<{nb}}{gri} = {neu}{ble}{str(sft.path())}{neu}")
    print(f"{gri}=========================================================================={neu}")
    #pause()


def creation_var_env_si_existe_pas():
    # Creation des variables d'environnement si elles n'existent pas
    if "PATH_CHANTIER" not in os.environ:
        os.environ["PATH_CHANTIER"] = ""
    if "TYPE" not in os.environ:
        os.environ["TYPE"] = ""
    if "ROOT_TYPE" not in os.environ:
        os.environ["ROOT_TYPE"] = ""
    if "PATH_TYPE" not in os.environ:
        os.environ["PATH_TYPE"] = ""
    if "PROJ" not in os.environ:
        os.environ["PROJ"] = ""
    if "ROOT_PROJ" not in os.environ:
        os.environ["ROOT_PROJ"] = ""
    if "PATH_PROJ" not in os.environ:
        os.environ["PATH_PROJ"] = ""
    if "FOLD" not in os.environ:
        os.environ["FOLD"] = ""
    if "ROOT_FOLD" not in os.environ:
        os.environ["ROOT_FOLD"] = ""
    if "PATH_FOLD" not in os.environ:
        os.environ["PATH_FOLD"] = ""
    if "SOFT" not in os.environ:
        os.environ["SOFT"] = ""
    if "ROOT_SOFT" not in os.environ:
        os.environ["ROOT_SOFT"] = ""
    if "PATH_SOFT" not in os.environ:
        os.environ["PATH_SOFT"] = ""


def determine_current_step(step_depart=""):
    """
    Determine l'etape courante (seulement si step_depart n'est pas renseigne)
    :param step_depart: bypass la fonction si renseigne
    :return: step
    """

    step = ""

    if step_depart == "":
        if os.environ["TYPE"] == "":
            step = "type"
        elif os.environ["PROJ"] == "":
            step = "proj"
        elif os.environ["FOLD"] == "":
            step = "fold"
        elif os.environ["SOFT"] == "":
            step = "soft"
        else:
            step = "soft"
    else:
        step = step_depart

    return step