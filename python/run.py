# coding: utf-8
# !/usr/bin/python
import os
import sys
import pdb

from api.constants import *
from api.color import color
from api.fonctions import *
from api.var import *
from api.api import *
from api.tools import *

from numpy.core.defchararray import lower


def maj_var_env(step, name, typ, prj, fld, sft):
    if step == "type":
        typ.set_current_name(name)
        prj.set_current_name("")
        fld.set_current_name("")
        sft.set_current_name("")
    elif step == "proj":
        prj.set_current_name(name)
        fld.set_current_name("")
        sft.set_current_name("")
    elif step == "fold":
        fld.set_current_name(name)
        sft.set_current_name("")
    elif step == "soft":
        sft.set_current_name(name)


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


def create_list_steps(step_depart: str, nb_name: int):
    steps = ["type", "proj", "fold", "soft"]
    liste = []

    if nb_name == 0:
        nb_name = 1

    # On determine le numero de l'etape de depart, ex: si la saisie est fold, gap = 2
    n = 0
    gap = 0
    for i in steps:
        if i == step_depart:
            gap = n
        n = n + 1

    n = 0
    for i in range(nb_name):
        liste.append(steps[n + gap])
        n = n + 1

    return liste


def format_names(saisie: list) -> list:
    """
    Formate les saisies names pour qu'elles soient compatibles avec le programme.
    :param saisie: saisie des names
    :return: liste des names correctement formatées.
    """
    liste = []

    for s in saisie:
        items = s.split("/")
        for item in items:
            if item != "":
                liste.append(item)

    return liste


def format_step(saisie: str) -> str:
    """
    Formate la saisie step pour qu'elle soit compatible avec le programme.
    :param saisie: saisie de la step : -t, -type, -p ...
    :return: str de la step correctement formatée.
    """
    step = ""

    if saisie == "-t" or saisie == "-type" or saisie == "t" or saisie == "type":
        step = "type"
    if saisie == "-p" or saisie == "-proj" or saisie == "p" or saisie == "proj":
        step = "proj"
    if saisie == "-f" or saisie == "-fold" or saisie == "f" or saisie == "fold":
        step = "fold"
    if saisie == "-s" or saisie == "-soft" or saisie == "s" or saisie == "soft":
        step = "soft"

    return step


def format_export(txt):
    buffer = ""
    for t in txt:
        buffer = buffer + " " + t

    return buffer


def env():
    print("Type= " + os.environ["TYPE"])
    print("Proj= " + os.environ["PROJ"])
    print("Fold= " + os.environ["FOLD"])
    print("Soft= " + os.environ["SOFT"])


def analyse_step_depart(step_depart):
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
        step = step_depart

    return step


def determine_path_by_var_env():
    path = ""

    if os.environ["TYPE"] == "":
        path = os.environ["PATH_CHANTIER"]
    elif os.environ["PROJ"] == "":
        path = os.environ["PATH_TYPE"]
    elif os.environ["FOLD"] == "":
        path = os.environ["PATH_PROJ"]
    elif os.environ["SOFT"] == "":
        path = os.environ["PATH_FOLD"]

    if os.environ["SOFT"] != "":
        path = os.environ["PATH_SOFT"]

    return path


def run(step_saisie: str, liste_names: list):
    """

    :param liste_names:
    :param step_saisie:

    :return:
    """

    NAMES = []
    ROOTS = []
    PATHS = []

    typ = Step("type")
    prj = Step("proj")
    fld = Step("fold")
    sft = Step("soft")

    creation_var_env_si_existe_pas()

    step_depart = analyse_step_depart(step_saisie)

    names = liste_names
    steps = create_list_steps(step_depart, len(names))

    name = ""
    step = ""
    path = ""

    nb_boucles = len(liste_names)

    if not names:
        step = steps[0]

        # Mise a jour des variables d'environnement
        maj_var_env(step, name, typ, prj, fld, sft)

        path = determine_path_by_var_env()

        # On génère la liste des repertoires
        liste_repertoires = os.listdir(path)

        # var(typ, prj, fld, sft)

        # On affiche la liste des repertoires pour la step
        affiche_liste("Liste de " + step, liste_repertoires, 10, "", 0, 1)
        print(f"\n{jau1}Vous pouvez setter un {step}: run {str(lower(step))} name.{neu}")

    for n in range(nb_boucles):
        name = names[n]
        step = steps[n]

        # Mise a jour des variables d'environnement
        maj_var_env(step, name, typ, prj, fld, sft)

        # On récupère le path de l'endroit ou se positionner
        # path = determine_path_repertoires(step, typ, prj, fld, sft)
        path = determine_path_by_var_env()

        # AFFICHAGE ====================================================================================================

        # if name == "" and step == "":

        # On génère la liste des repertoires
        liste_repertoires = os.listdir(path)

        # var(typ, prj, fld, sft)

        # On affiche la liste des repertoires pour la step
        affiche_liste("Liste de " + step, liste_repertoires, 10, "", 0, 1)
        print(f"\n{jau1}Vous pouvez setter un {step}: run {str(lower(step))} name.{neu}")

        # elif name != "":
        #     # On verifie l'existence du nom dans le path
        #     verif = verif_existence(path, name)
        #
        #     if verif:
        #         nextStep = next_step(step)
        #         nextRoot = next_root(step, name, typ, prj, fld, sft)
        #
        #         # On cree la liste des repertoires
        #         liste_repertoires = os.listdir(nextRoot)
        #
        #         if next != "":
        #             affiche_liste(f"Liste des {nextStep}", liste_repertoires, clear=1, largeur=15)

        # STEPS.append(step)
        NAMES.append(name)
        ROOTS.append(path)
        PATHS.append(path + "/" + name)

    # EXPORT ===========================================================================================================

    NAMES = (typ.current_name(), prj.current_name(), fld.current_name(), sft.current_name())
    ROOTS = (typ.root(), prj.root(), fld.root(), sft.root())
    PATHS = (typ.path(), prj.path(), fld.path(), sft.path())

    fill_return1(format_export(NAMES))
    fill_return2(format_export(ROOTS))
    fill_return3(format_export(PATHS))


# MAIN SCRIPT :
# ======================================================

# On recupere les arguments
args = sys.argv[1]

# On analyse et on format les saisies:
args = args.split(',')

liste_steps = (
    "-t", "-p", "-f", "-s", "t", "p", "f", "s", "-type", "-proj", "-fold", "-soft", "type", "proj", "fold", "soft")
saisie_names = []
saisie_step = ""

for arg in args:
    if arg != "" and arg not in liste_steps:
        saisie_names.append(arg)
    if arg in liste_steps:
        saisie_step = arg

saisie_names = format_names(saisie_names)
saisie_step = format_step(saisie_step)

run(saisie_step, saisie_names)
