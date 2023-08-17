# coding: utf-8
# !/usr/bin/python
import os
import sys

from api.tools import *
from api.fonctions import *
from api.var import *


def run_type(saisie: str = ""):

    name = saisie.lower()

    create_var_env_if_not_exist()

    typ = Step("type")

    aa(TYPE=typ.current_name())










#     cl = color()
#
#     name = saisie
#
#     typ = Step("type")



arg = sys.argv[1]
run_type(arg)
