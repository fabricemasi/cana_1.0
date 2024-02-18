# coding: utf-8
# !/usr/bin/python

import os
import sys
from datetime import datetime

from api.cana_Step import Step
from api.cana_api import *
from api.cana_constants import *
from api.main_tools import *
from api.main_api import *


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


def create_list_steps(step_depart: str, nb_name: int):
    steps = ["type", "proj", "fold", "soft"]
    liste = []

    if nb_name == 0:
        nb_name = 1
    if nb_name == 4 and step_depart == "soft":
        step_depart = "type"
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

    if buffer[0] == " ":
        buffer = buffer[1:]

    return buffer


def env():
    print("Type= " + os.environ["TYPE"])
    print("Proj= " + os.environ["PROJ"])
    print("Fold= " + os.environ["FOLD"])
    print("Soft= " + os.environ["SOFT"])


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


def determine_root_by_var_env():
    root = ""

    tp = os.environ["TYPE"]
    pr = os.environ["PROJ"]
    fl = os.environ["FOLD"]
    sf = os.environ["SOFT"]

    if tp != "" and pr == "" and fl == "" and sf == "":
        root = os.environ["ROOT_TYPE"]
    if tp != "" and pr != "" and fl == "" and sf == "":
        root = os.environ["ROOT_PROJ"]
    if tp != "" and pr != "" and fl != "" and sf == "":
        root = os.environ["ROOT_FOLD"]
    if tp != "" and pr != "" and fl != "" and sf != "":
        root = os.environ["ROOT_SOFT"]

    root = supprime_last_slash(root)

    return root


def determine_next_step_by_step(step):
    next_step = ""
    libele: str = ""

    if step == "":
        next_step = "type"
        libele = "type"
    if step == "type":
        next_step = "proj"
        libele = "projet"
    if step == "proj":
        next_step = "fold"
        libele = "sous-repertoire"
    if step == "fold":
        next_step = "soft"
        libele = "soft"
    if step == "soft":
        next_step = "soft"
        libele = "Fichier"

    return next_step, libele


def add_libelle_for_step(step):
    stp = ""
    libele = ""

    if step == "type":
        stp = "type"
        libele = "type"
    if step == "proj":
        stp = "proj"
        libele = "projet"
    if step == "fold":
        stp = "fold"
        libele = "sous-repertoire"
    if step == "soft":
        stp = "soft"
        libele = "soft"

    return stp, libele


def schema(step):
    schem = ""

    if step.lower() == "type":
        schem = schem_type
    if step.lower() == "proj":
        schem = schem_proj
    if step.lower() == "fold":
        schem = schem_fold
    if step.lower() == "soft":
        schem = schem_soft

    return schem


def killpipe(typ, prj, fld, sft):
    typ.set_current_name("")
    prj.set_current_name("")
    fld.set_current_name("")
    sft.set_current_name("")


def analyse_nb_arguments(step_depart, nb_names, typ, prj, fld, sft):
    verif = 0
    if nb_names == 4 and sft.current_name() != "":
        killpipe(typ, prj, fld, sft)
        verif = 1
    if nb_names == 4 and sft.current_name() != "soft":
        killpipe(typ, prj, fld, sft)
        verif = 1

    else:
        if step_depart == "type":
            if nb_names <= 4:
                verif = 1
        elif step_depart == "proj":
            if nb_names <= 3:
                verif = 1
        elif step_depart == "fold":
            if nb_names <= 2:
                verif = 1
        elif step_depart == "soft":
            if nb_names <= 1:
                verif = 1

    return verif


def possibly_make_history(typ, prj, fld, sft):
    command = ""
    if typ != "" and prj != "" and fld != "" and sft != "":
        BIN = os.environ["BIN"]

        now = datetime.now()
        dt = now.strftime("%Y-%m-%d")
        tm = now.strftime("%H:%M:%S")

        file = f"{BIN}/data/pipe_set_history.txt"

        command = f"\n{dt}--{tm}-----run {typ} {prj} {fld} {sft}"

        file = open(file, 'a')
        file.write(command)
        file.close()


def check_liste_names(liste_names):
    liste = []

    # Si liste_names n'est pas une liste on le transforme en liste
    if type(liste_names) is not list:
        liste_names = [liste_names]

    for i in liste_names:
        if i != "":
            liste.append(i)

    return liste


def run_old(step_saisie: str, liste_names: list, typ=Step("type"), prj=Step("proj"), fld=Step("fold"), sft=Step("soft"),
            console: bool = 0):
    if console:
        NAMES = []
        ROOTS = []
        PATHS = []

    # On format le step depart
    step_depart = determine_current_step(step_saisie)

    # On verifie la liste_names (on supprime les champs vides)
    liste_names = check_liste_names(liste_names)

    # Verification du nombre d'arguments. S'il est incoherent, on sort du programme.
    verif = analyse_nb_arguments(step_depart, len(liste_names), typ, prj, fld, sft)

    if verif == 0:
        print(f"\n{jau1}Le nombre d'argument est incoherent. {rou1}exit_pipe{neu}")
        return

    names = liste_names

    steps = create_list_steps(step_depart, len(names))

    name = ""
    step = ""
    path = ""

    nb_boucles = len(liste_names)

    if not names:
        # Step
        step = steps[0]
        affiche_step = add_libelle_for_step(step)

        # Mise a jour des variables d'environnement
        maj_var_env(step, name, typ, prj, fld, sft)

        # Path
        path = determine_path_by_var_env()

        # On génère la liste des repertoires
        liste_repertoires = os.listdir(path)

        # On affiche la liste des repertoires pour la step
        affiche_liste("LISTE DES " + affiche_step[1].upper() + "S", liste_repertoires, 10, "", 0, 1)

        NAMES.append(name)
        ROOTS.append(path)
        PATHS.append(path + "/" + name)

    for n in range(nb_boucles):
        # Name
        name = names[n]

        # Step
        step = steps[n]
        next = determine_next_step_by_step(step)

        # Mise a jour des variables d'environnement
        maj_var_env(step, name, typ, prj, fld, sft)

        # Root
        root = supprime_last_slash(determine_root_by_var_env())

        # Path
        path = supprime_last_slash(root + "/" + name + schema(step))

        verif = os.path.isdir(path)

        if not verif:
            create = create_folder(root, name)
            if create == 0:
                return

        # On génère la liste des repertoires
        liste_repertoires = os.listdir(path)

        # On affiche la liste des repertoires pour la step
        affiche_liste("LISTE DES " + next[1].upper() + "S", liste_repertoires, 10, "", 0, 1)

        NAMES.append(name)
        ROOTS.append(path)
        PATHS.append(path + name)
    # EXPORT TERMINAL===================================================================================================

    possibly_make_history(typ.current_name(), prj.current_name(), fld.current_name(), sft.current_name())

    NAMES = (typ.current_name(), prj.current_name(), fld.current_name(), sft.current_name())
    ROOTS = (typ.root(), prj.root(), fld.root(), sft.root())
    PATHS = (typ.path(), prj.path(), fld.path(), sft.path())

    fill_return1(format_export(NAMES))
    fill_return2(format_export(ROOTS))
    fill_return3(format_export(PATHS))


def determine_step_from_nothing():
    step = ""

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

    return step


def run(step: str, names: list, typ=Step("type"), prj=Step("proj"), fld=Step("fold"), sft=Step("soft"),
        console: bool = False):
    """
    :Syntaxe : run("type",['3d','hotrod'])
    :param step:
    :param names:
    :param typ:
    :param prj:
    :param fld:
    :param sft:
    :param console:
    :return:
    """

    # On supprime les chants vides de la liste names
    names = check_liste_names(names)

    # Verification du nombre d'arguments. S'il est incoherent, on sort du programme
    verif = analyse_nb_arguments(step, len(names), typ, prj, fld, sft)
    if verif == 0:
        print(f"\n{jau1}Le nombre d'argument est incoherent. {rou1}exit_pipe{neu}")
        return

    # Creation de la liste des steps qui correspondront au names
    steps = create_list_steps(step, len(names))

    # Nombre de boucles necessaires
    nb_boucles = len(names)

    NAMES = []
    ROOTS = []
    PATHS = []

    libelle_step = []

    liste_repertoires = []

    path = ""

    if not names:
        # Name
        name = ""

        # step
        step = steps[0]
        libelle_step = add_libelle_for_step(step)

        # Mise a jour des variables d'environnement
        maj_var_env(step, name, typ, prj, fld, sft)

        # RESULTATS :
        path = determine_path_by_var_env()

        NAMES.append(name)
        ROOTS.append(path)
        PATHS.append(path + "/" + name)

    for n in range(nb_boucles):
        # Name
        name = names[n]
        libelle_step = add_libelle_for_step(step)

        # Step
        step = steps[n]
        next = determine_next_step_by_step(step)
        libelle_step = add_libelle_for_step(next)

        # Mise a jour des variables d'environnement
        maj_var_env(step, name, typ, prj, fld, sft)

        # Root
        root = supprime_last_slash(determine_root_by_var_env())

        # Path
        path = supprime_last_slash(root + "/" + name + schema(step))
        verif = os.path.isdir(path)
        if not verif:
            create = create_folder(root, name)
            if create == 0:
                return

        NAMES.append(name)
        ROOTS.append(path)
        PATHS.append(path + "/" + name)

    # On génère la liste des repertoires
    liste_repertoires = os.listdir(path)

    # On complete l'historique si le set est complet
    possibly_make_history(typ.current_name(), prj.current_name(), fld.current_name(), sft.current_name())

    NAMES = (typ.current_name(), prj.current_name(), fld.current_name(), sft.current_name())
    ROOTS = (typ.root(), prj.root(), fld.root(), sft.root())
    PATHS = (typ.path(), prj.path(), fld.path(), sft.path())

    if console:
        # On affiche la liste des repertoires pour la step
        affiche_liste("LISTE DES " + libelle_step[1].upper() + "S", liste_repertoires, 10, "", 0, 1)

        fill_return1(format_export(NAMES))
        fill_return2(format_export(ROOTS))
        fill_return3(format_export(PATHS))

    return step


# FONCTIONS POUR TERMINAL :
# ======================================================


if __name__ == "__main__":
    # On recupere les arguments
    args = sys.argv[1]

    # On analyse et on format les saisies:
    args = args.split(',')

    # On reformatte les saisies et on cree les saisie_names et saisie_step
    liste_steps = (
        "-t", "-p", "-f", "-s", "t", "p", "f", "s",
        "-type", "-proj", "-fold", "-soft", "type", "proj", "fold", "soft")
    step = ""
    names = []

    for arg in args:
        if arg != "" and arg not in liste_steps:
            names.append(arg)
        if arg in liste_steps:
            step = arg

    step = format_step(step)
    names = format_names(names)

    if step == "":
        step = determine_step_from_nothing()

    test = run(step, names, console=True)
