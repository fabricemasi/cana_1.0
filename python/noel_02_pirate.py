import time
import random
from api.main_color import color
import os

os.system('clear')

def type_code(code):
    for line in code.split('\n'):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.1)  # Ajustez cette valeur pour contrôler la vitesse de frappe
        print()


def simulate_loading():
    cl = color()
    neu = cl.NEUTRE()
    gra = cl.GRAS()
    gri = cl.GRIS2()
    ble = cl.BLEU()
    rou = cl.ROUGE()
    mag = cl.MAGENTA()
    jau = cl.JAUNE()
    bla = cl.BLANC()

    used_codes = []

    print(f"{ble}")
    code = """
    Bravo! Vous avez decouvert votre premier code secret!
    
    Voici quelques instructions qui vont vous permettre de decouvrir l'ordre dans lesquels les paquets doivent etre
    ouverts...
    
    Vous devez taper un nouveau code.
    Un indice se trouve au chaud, la ou on peut aussi trouver de quoi payer le lait ...
"""
    type_code(code)


if __name__ == "__main__":
    simulate_loading()

