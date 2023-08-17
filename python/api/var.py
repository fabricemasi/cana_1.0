# coding: utf-8
# !/usr/bin/python

import os
from .tools import *



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
                os.environ["ROOT_TYPE"] = PATH_CHANTIER
                os.environ["PATH_TYPE"] = PATH_CHANTIER + "/" + name
            else :
                os.environ["TYPE"] = ""
                os.environ["ROOT_TYPE"] = PATH_CHANTIER
                os.environ["PATH_TYPE"] = PATH_CHANTIER

        elif self.step.upper() == "PROJ":
            if name:
                PATH_TYPE = os.environ["PATH_TYPE"]
                os.environ["PROJ"] = name
                os.environ["ROOT_PROJ"] = PATH_TYPE
                os.environ["PATH_PROJ"] = PATH_TYPE + "/" + name
            else:
                PATH_TYPE = os.environ["PATH_TYPE"]
                os.environ["PROJ"] = ""
                os.environ["ROOT_PROJ"] = ""
                os.environ["PATH_PROJ"] = ""

        elif self.step.upper() == "FOLD":
            if name:
                PATH_PROJ = os.environ["PATH_PROJ"]
                os.environ["FOLD"] = name
                os.environ["ROOT_FOLD"] = PATH_PROJ
                os.environ["PATH_FOLD"] = PATH_PROJ + "/" + name + "/02_work/"
            else:
                PATH_PROJ = os.environ["PATH_PROJ"]
                os.environ["FOLD"] = ""
                os.environ["ROOT_FOLD"] = ""
                os.environ["PATH_FOLD"] = ""

        elif self.step.upper() == "SOFT":
            if name:
                PATH_FOLD = os.environ["PATH_FOLD"]
                os.environ["SOFT"] = name
                os.environ["ROOT_SOFT"] = PATH_FOLD
                os.environ["PATH_SOFT"] = PATH_FOLD + "/" + name
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
            ret = ROOT_TYPE
        if self.step.upper() == "PROJ":
            ret = ROOT_PROJ
        if self.step.upper() == "FOLD":
            ret = ROOT_FOLD
        if self.step.upper() == "SOFT":
            ret = ROOT_SOFT

        return ret


    def path(self):
        PATH_TYPE = os.environ["PATH_TYPE"]
        PATH_PROJ = os.environ["PATH_PROJ"]
        PATH_FOLD = os.environ["PATH_FOLD"]
        PATH_SOFT = os.environ["PATH_SOFT"]

        if self.step.upper() == "TYPE":
            ret = PATH_TYPE
        if self.step.upper() == "PROJ":
            ret = PATH_PROJ
        if self.step.upper() == "FOLD":
            ret = PATH_FOLD
        if self.step.upper() == "SOFT":
            ret = PATH_SOFT

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