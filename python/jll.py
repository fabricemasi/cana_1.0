# coding: utf-8
# !/usr/bin/python

import os

from api.cana_import import *

BIN = os.environ['BIN']

path = BIN + '/data'
file = path + '/' + 'pipe_set_history.txt'

# Chargement du fichier ds le buffer :
file = open(file)
buffer = file.read()
file.close()

buffer = buffer.split('\n')[-1:][0]
buffer = buffer.split(' ')[-4:]

fill_return1(buffer[0])
fill_return2(buffer[1])
fill_return3(buffer[2])
fill_return4(buffer[3])
