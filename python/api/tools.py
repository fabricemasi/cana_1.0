# coding: utf-8
# !/usr/bin/python

import time
import pdb
import inspect

from .color import color


def aa(stop=1, tabulation=0, cadre=1, **kwargs):
    """
    Permet de visualiser une variable rapidement. Accepte les tableaux.
    Fonctionne comme la fonction "a" mais la syntaxe change un peu.\n
    Syntaxe :\n
    Exemple 1: les variables:\n
    p(var1=var1, var2=var2)\n
    Exemple 2: les tableaux:\n
    for key, value in dict.items():
     p(**{key:value})
    """

    cl = color()
    neu = cl.NEUTRE()
    gra = cl.GRAS()
    gri = cl.GRIS2()
    ble = cl.BLEU()

    if tabulation == 0:
        tab = 0
        for cle, valeur in kwargs.items():
            if len(cle) > tab:
                tab = len(cle)
        tabulation = tab


    if cadre == 1:
        print(f"{gri}=========================================================================={neu}")


    for cle, valeur in kwargs.items():
        print(f"{gra}{gri}{cle:<{tabulation}} : {neu}{ble}{valeur}{neu}")

    if cadre == 1:
        print(f"{gri}=========================================================================={neu}")

    if stop == 1:
        pause(99)


def pause(arg1=99, arg2="Pause"):
    """
    Fait une pause dans le script
    :param arg1: temps de pause
    :param arg2: element a printer ("Pause" par defaut)

    """

    cl = color()
    bli = cl.BLINK()
    neu = cl.NEUTRE()
    gri = cl.GRIS()
    gra = cl.GRAS()


    if arg1 > 98:
        input(f"{gri}Script en pause. Appuyez sur{bli}{gra} entree{neu}{gri} pour continuer{neu}")
    else:
        print(arg1, "(" + str(arg1) + "sec)")
        time.sleep(arg1)
