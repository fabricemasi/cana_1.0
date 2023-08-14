# coding: utf-8
# !/usr/bin/python

import sys
import pdb

from api.color import color
from api.fonctions import *
from api.var import *
from api.api import *
from api.tools import *

from numpy.core.defchararray import lower


# Commande run :
#
# retourne les variabless STEP et ROOT_STEP
# ======================================================


# FONCTIONS :
# ======================================================


def determine_path_repertoires(step, typ, prj, fld, sft):
    # Permet de renvoyer l'adresse selon la step (TYPE, PROJ ...)

    ret = ""
    if lower(step) == "type":
        # r = os.environ['ROOT_TYPE']
        ret = typ.root()

    elif lower(step) == "proj":
        # r = os.environ['ROOT_PROJ']
        ret = prj.root()

    elif lower(step) == "fold":
        # r = os.environ['ROOT_FOLD']
        ret = fld.root()

    elif lower(step) == "soft":
        # r = os.environ['ROOT_FOLD'] + "/02_work/"
        ret = sft.root()

    return ret


def analyse_arguments(arg1, arg2):
    """
    Remet les arguments dans l'ordre.
    Les arguments sont interchangeable, cad peut importe l'ordre dans lequel on les renseignes.
    Cette fonction les remets dans le bon ordre.\n
    :param arg1: saisie du repertoire dans lequel on veut se setter (dependant de step)
    :param arg2: valeur parmis : "-t","-p","-f","-s","type","proj","fold","soft"
    :return: saisie_step, saisie_name
    """
    liste = ("-t", "-p", "-f", "-s", "type", "proj", "fold", "soft")

    saisie_step = ""
    saisie_name = ""

    if arg1 == "" and arg2 == "":
        saisie_step = ""
        saisie_name = ""

    elif arg1 != "" and arg2 == "":
        if arg1 in liste:
            saisie_step = arg1
            saisie_name = ""
        elif arg1 not in liste:
            saisie_step = ""
            saisie_name = arg1

    elif arg1 != "" and arg2 != "":
        if arg1 in liste:
            saisie_step = arg1
            saisie_name = arg2
        if arg2 in liste:
            saisie_step = arg2
            saisie_name = arg1
        if arg1 in liste and arg2 in liste:
            saisie_step = "erreur"
            saisie_name = "erreur"
        if arg1 not in liste and arg2 not in liste:
            saisie_step = "erreur"
            saisie_name = "erreur"

    return saisie_step, saisie_name


def analyse_saisie_step(saisie_step, typ, prj, fld, sft):
    """
    Analyse toutes les variables de set (typ, prj...), et les remplis si besoin.
    :param saisie_step: le step qui a été renseigné lors de l'appel de la fonction.
    :param typ: selon le step qui a ete sette, on va mettre a jour les objets typ prj fld et sft
    :param prj: objet prj
    :param fld: objet fld
    :param sft: objet sft
    :return: new_step
    """

    new_step = ""

    if saisie_step == "":
        new_step = determine_step(typ, prj, fld, sft)

    elif saisie_step == "-t" or lower(saisie_step) == "type":
        new_step = "type"
        typ.setcurrent(new_step)

    elif saisie_step == "-p" or lower(saisie_step) == "proj":
        if typ.current() != "":
            new_step = "proj"
            prj.setcurrent(new_step)

    elif saisie_step == "-f" or lower(saisie_step) == "fold":
        if prj.current() != "":
            new_step = "fold"
            fld.setcurrent(new_step)

    elif saisie_step == "-s" or lower(saisie_step) == "soft":
        if fld.current() != "":
            new_step = "soft"
            sft.setcurrent(new_step)

    if new_step == "":
        new_step = "erreur"

    return new_step


def determine_root_step_by_step(STEP, typ, prj, fld, sft):
    """
    On fourni la step et la fonction retourne le ROOT_STEP
    :param STEP:
    :param typ: objet typ
    :param prj: objet prj
    :param fld: objet fld
    :param sft: objet sft
    :return: ROOT_STEP
    """
    ret = ""
    if STEP == "type":
        ret = typ.root()
    elif STEP == "proj":
        ret = prj.root()
    elif STEP == "fold":
        ret = fld.root()
    elif STEP == "proj":
        ret = sft.root()

    return ret

def determine_path_step_by_step(STEP, typ, prj, fld, sft):
    """
    On fourni la step et la fonction retourne le ROOT_STEP
    :param STEP:
    :param typ: objet typ
    :param prj: objet prj
    :param fld: objet fld
    :param sft: objet sft
    :return: ROOT_STEP
    """
    ret = ""
    if STEP == "type":
        ret = typ.path()
    elif STEP == "proj":
        ret = prj.path()
    elif STEP == "fold":
        ret = fld.path()
    elif STEP == "proj":
        ret = sft.path()

    return ret


def next_step(STEP):
    ret = ""

    if STEP == "type":
        ret = "proj"
    elif STEP == "proj":
        ret = "fold"
    elif STEP == "fold":
        ret = "soft"
    elif STEP == "soft":
        ret = ""

    return ret


def next_root(step, name, typ, prj, fld, sft):
    # Permet de renvoyer l'adresse selon la step (TYPE, PROJ ...)

    r = ""
    if lower(step) == "type":
        # r = os.environ['ROOT_TYPE']
        r = typ.path()

    elif lower(step) == "proj":
        # r = os.environ['ROOT_PROJ']
        r = prj.path()

    elif lower(step) == "fold":
        # r = os.environ['ROOT_FOLD']
        r = fld.path()

    elif lower(step) == "soft":
        # r = os.environ['ROOT_FOLD'] + "/02_work/"
        r = sft.path()

    return r


def maj_var(step, name, typ, prj, fld, sft):
    if step == "type":
        typ.setcurrent(name)
    elif step == "proj":
        prj.setcurrent(name)
    elif step == "fold":
        fld.setcurrent(name)
    elif step == "soft":
        sft.setcurrent(name)


def run(arg1="", arg2=""):
    """
    Permet de setter la prochaine step. Exemple, si 'type' est deja sette, run settera 'proj'...
    Les arguments sont interchangeables
    :param arg1: saisieName, cad 3d pour le type, hotrod pour projet, etc...
    :param arg2: saisieStep, cad une de ces valeurs : (-t,-p,-f,-s,type,proj,fold,soft)
    :return: STEP et ROOT_STEP
    """
    STEP = ""
    NAME = ""
    ROOT_STEP = ""
    PATH_STEP = ""

    # On charge les differentes classes
    cl = color()

    typ = Step("type")
    prj = Step("proj")
    fld = Step("fold")
    sft = Step("soft")

    # On charge les variables d'environnement si elles existent.
    typ.setcurrent(os.environ["TYPE"])
    prj.setcurrent(os.environ["PROJ"])
    fld.setcurrent(os.environ["FOLD"])
    sft.setcurrent(os.environ["SOFT"])






    # aa(typ=os.environ["TYPE"],prj=os.environ["PROJ"],fld=os.environ["FOLD"],sft=os.environ["SOFT"])
    # var(typ, prj, fld, sft)

    # On analyse les arguments et les step pour extraire
    retourAnalyseArgs = analyse_arguments(arg1, arg2)  # Remet les arguments dans l'ordre.
    retourAnalyseSteps = analyse_saisie_step(retourAnalyseArgs[0], typ, prj, fld, sft)  # Formate le texte de step

    # Resultats des differentes analyses
    saisie_name = retourAnalyseArgs[1]
    saisie_step = retourAnalyseSteps

    # On repertorie les variables qui vont nous servir pour la suite
    step = saisie_step
    name = saisie_name

    # var(typ, prj, fld, sft)

    # Mise a jour des variables d'environnement
    maj_var(step, name, typ, prj, fld, sft)

    # var(typ, prj, fld, sft)

    path = determine_path_repertoires(step, typ, prj, fld, sft)  # On recupere le path de l'endroit ou se positionner

    # aa(step=step, name=name, path=path)
    # aa(step=step, name=name)
    # var(typ, prj, fld, sft)
    # aa(typ=typ.current(),prj=prj.current(), fld=fld.current(), sft=sft.current(), typrrot=typ.root(),
    # prjroot=prj.root(), fldroot=fld.root(), sftroot=sft.root())

    # SI LE NOM DE LA RECHERCHE N'EST PAS RENSEIGNE :
    # ======================================================================

    if name == "":

        # On cree la liste des repertoires
        liste_repertoires = os.listdir(path)

        # On affiche la liste des repertoires pour la step
        affiche_liste("Liste de " + step, liste_repertoires, 10, "", 0, 1)
        print(cl.JAUNE())
        print("Vous pouvez setter un " + step + ": run " + str(lower(step)) + " name." + cl.NEUTRE())

        NAME = ""
        STEP = step
        ROOT_STEP = os.environ["ROOT_CHANTIER"]
        PATH_STEP = ""

        # var(typ, prj, fld, sft)

    # SI LE NOM DE LA RECHERCHE EST RENSEIGNE :
    # ======================================================================

    elif name != "":
        # On verifie l'existence du nom dans le path

        verif = verif_existence(path, name)

        if verif:
            NAME = name
            STEP = step
            ROOT_STEP = determine_root_step_by_step(STEP, typ, prj, fld, sft)
            PATH_STEP = determine_path_step_by_step(STEP, typ, prj, fld, sft)

            # var(typ, prj, fld, sft)
            # aa(name=name, STEP=STEP, ROOT_STEP=ROOT_STEP)

            nextStep = next_step(step)
            nextRoot = next_root(step, name, typ, prj, fld, sft)

            # aa(nextStep=nextStep, nextRoot=nextRoot)

            # On cree la liste des repertoires
            liste_repertoires = os.listdir(nextRoot)

            if next != "":
                affiche_liste(f"Liste des {nextStep}", liste_repertoires, clear=1, largeur=15)

    # Pour le terminal :
    # aa(typ=os.environ["TYPE"], prj=os.environ["PROJ"], fld=os.environ["FOLD"], sft=os.environ["SOFT"])
    fill_return1(NAME)
    fill_return2(STEP)
    fill_return3(ROOT_STEP)
    fill_return4(PATH_STEP)


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
if n == 0:
    run()
elif n == 1:
    run(arguments[0])
elif n == 2:
    run(arguments[0], arguments[1])
