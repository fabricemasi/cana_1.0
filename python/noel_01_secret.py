import time
import random
import os
from api.main_color import color

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

    print()
    print(f"{jau}    Initialisation en cours...{neu}")
    time.sleep(0.1)

    print(f"{jau}    Configuration en cours...{neu}")
    time.sleep(0.1)


    code = f"""{ble}
    Bonjour, je m'appelle moussaillon, l'inteligence artificielle de Barbe blanche. Je suis ravi de faire votre 
    connaissance. 
    Je vais vous assister dans le deballage de vos cadeaux, et je serai votre lien avec Barbe blanche.
    
    Je vais maintenant etablir la connection avec lui...
    {mag}    
    
    Demande en attente de confirmation par Barbe blanche...
    ........................................................................................................
    
    ----------> Connection avec Barbe Blanche etablie
                                       
    Demande confirmee par Barbe blanche ...
"""

    type_code(code)


    for _ in range(60):
        # Barre de chargement bleue
        print(f"    Chargement des données pour Elyne l'intrepide {bla}[" + "#" * _ + " " * (52 - _) + "]", end='\r')
        time.sleep(0.05)
    print()
    print(f"{rou}    Donnees pour Elyne l'intrepide mises en memoire{neu}")
    print()

    for _ in range(60):
        # Barre de chargement bleue
        print(f"    Chargement des données pour Leane la barbare  {bla}[" + "#" * _ + " " * (52 - _) + "]", end='\r')
        time.sleep(0.05)
    print()
    print(f"{rou}    Donnees pour Leane la barbare mises en memoire{neu}")

    print(f"{ble}")
    code = """
    Les donnees ont ete mises en memoire avec succes!
    Les differents codes secrets ont ete generes.
    Vous pouvez maintenant entrer votre premier code secret.
"""
    type_code(code)







if __name__ == "__main__":
    simulate_loading()
