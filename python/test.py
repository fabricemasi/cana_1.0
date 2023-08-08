# coding: utf-8
# !/usr/bin/python

from api.color import color

cl = color()

# for i in range(0, 200):
#     print("\033[" + str(i) + "m" + "033[" + str(i) + "m")

print(cl.GRIS_BCK()+cl.BLANC())
print("teest")
print(cl.NEUTRE())