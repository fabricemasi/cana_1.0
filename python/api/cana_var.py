# coding: utf-8
# !/usr/bin/python

import os
from .main_tools import *
from .cana_constants import *
from .main_api import supprime_last_slash


class Step:
    def __init__(self, step):

        self.step = step


    def current_name(self):
        """
        :return: la valeur de la step
        """
        ret = os.environ[self.step.upper()]
        return ret


    def set_current_name(self, name):
        """
        Modifie les variables d'environnements en fonction du 'name':
        Par exemple, TYPE et ROOT_TYPE dans le cas de 'type'
        :param name: le nom du repertoire selectionne (en fonction de la step)
        :return: Rien. modifie les variables d'environnement
        """

        if self.step.upper() == "TYPE":
            PATH_CHANTIER = os.environ["PATH_CHANTIER"]
            if name:
                os.environ["TYPE"] = name
                os.environ["ROOT_TYPE"] = supprime_last_slash(PATH_CHANTIER)
                os.environ["PATH_TYPE"] = supprime_last_slash(PATH_CHANTIER + "/" + name + schem_type)
            else :
                os.environ["TYPE"] = ""
                os.environ["ROOT_TYPE"] = supprime_last_slash(PATH_CHANTIER)
                os.environ["PATH_TYPE"] = supprime_last_slash(PATH_CHANTIER)

        elif self.step.upper() == "PROJ":
            if name:
                PATH_TYPE = os.environ["PATH_TYPE"]
                os.environ["PROJ"] = name
                os.environ["ROOT_PROJ"] = supprime_last_slash(PATH_TYPE)
                os.environ["PATH_PROJ"] = supprime_last_slash(PATH_TYPE + "/" + name + schem_proj)
            else:
                PATH_TYPE = os.environ["PATH_TYPE"]
                os.environ["PROJ"] = ""
                os.environ["ROOT_PROJ"] = ""
                os.environ["PATH_PROJ"] = ""

        elif self.step.upper() == "FOLD":
            if name:
                PATH_PROJ = os.environ["PATH_PROJ"]
                os.environ["FOLD"] = name
                os.environ["ROOT_FOLD"] = supprime_last_slash(PATH_PROJ)
                os.environ["PATH_FOLD"] = supprime_last_slash(PATH_PROJ + "/" + name + schem_fold)
            else:
                PATH_PROJ = os.environ["PATH_PROJ"]
                os.environ["FOLD"] = ""
                os.environ["ROOT_FOLD"] = ""
                os.environ["PATH_FOLD"] = ""

        elif self.step.upper() == "SOFT":
            if name:
                PATH_FOLD = os.environ["PATH_FOLD"]
                os.environ["SOFT"] = name
                os.environ["ROOT_SOFT"] = supprime_last_slash(PATH_FOLD)
                os.environ["PATH_SOFT"] = supprime_last_slash(PATH_FOLD + "/" + name + schem_soft)
            else:
                PATH_FOLD = os.environ["PATH_FOLD"]
                os.environ["SOFT"] = ""
                os.environ["ROOT_SOFT"] = ""
                os.environ["PATH_SOFT"] = ""


    def root(self):
        ROOT_TYPE = os.environ["ROOT_TYPE"]
        ROOT_PROJ = os.environ["ROOT_PROJ"]
        ROOT_FOLD = os.environ["ROOT_FOLD"]
        ROOT_SOFT = os.environ["ROOT_SOFT"]

        if self.step.upper() == "TYPE":
            ret = supprime_last_slash(ROOT_TYPE)
        if self.step.upper() == "PROJ":
            ret = supprime_last_slash(ROOT_PROJ)
        if self.step.upper() == "FOLD":
            ret = supprime_last_slash(ROOT_FOLD)
        if self.step.upper() == "SOFT":
            ret = supprime_last_slash(ROOT_SOFT)

        return ret


    def path(self):
        PATH_TYPE = os.environ["PATH_TYPE"]
        PATH_PROJ = os.environ["PATH_PROJ"]
        PATH_FOLD = os.environ["PATH_FOLD"]
        PATH_SOFT = os.environ["PATH_SOFT"]

        if self.step.upper() == "TYPE":
            ret = supprime_last_slash(PATH_TYPE)
        if self.step.upper() == "PROJ":
            ret = supprime_last_slash(PATH_PROJ)
        if self.step.upper() == "FOLD":
            ret = supprime_last_slash(PATH_FOLD)
        if self.step.upper() == "SOFT":
            ret = supprime_last_slash(PATH_SOFT)

        return ret


    def liste_item(self):

        ROOT_TYPE = os.environ["ROOT_TYPE"]
        ROOT_PROJ = os.environ["ROOT_PROJ"]
        ROOT_FOLD = os.environ["ROOT_FOLD"]
        ROOT_SOFT = os.environ["ROOT_SOFT"]

        if self.step.upper() == "TYPE":
            liste = os.listdir(ROOT_TYPE)
        if self.step.upper() == "PROJ":
            liste = os.listdir(ROOT_PROJ)
        if self.step.upper() == "FOLD":
            liste = os.listdir(ROOT_FOLD)
        if self.step.upper() == "SOFT":
            liste = os.listdir(ROOT_SOFT)

        return liste