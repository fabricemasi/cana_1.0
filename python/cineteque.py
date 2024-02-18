#coding: utf-8
#!/usr/bin/python

import os
import sys
import subprocess
import shutil

##################################################
#   API GENERALE
##################################################

class clr:
    rg  = '\033[31m'
    gr = '\033[32m'
    jn = '\033[33m'
    bl = '\033[34m'
    mg = '\033[35m'
    cy  = '\033[36m'
    blc = '\033[37m'


    it = '\033[3m'
    cl = '\033[1m'
    fc = '\033[2m'
    sl = '\033[4m'
    fd = '\033[7m'

    std = '\033[00m'

### Fait la liste des repertoires
def list_folder(list_old):
    list_new = []
    for el in list_old:
        if os.path.isdir(el):
            list_new.append(el)
    return list_new

### Fait la liste des fichiers
def list_file(list_old):
    list_new = []
    for el in list_old:
        if  os.path.isfile(el):
            list_new.append(el)
    return list_new

### Retourne une liste de fichiers ayant l'extension specifiee
def list_ext(list_old, ext): # Argument 1: liste des films a tester | Argument 2: extension a chercher
    list_new = []

    for el in list_old:
        if os.path.splitext(el)[1] == ext:
            list_new.append(el)

    return list_new

### Reparti le nombre d'espace selon la longueur d'une chaine
def tab(chaine, separateur = "", val_tab = 5):
    """
    :param chaine:
    :param separateur: Si on veut un separateur du type "-"
    :param val_tab: Largeur de l'espace en nombre de caracteres (par defaut : 5)
    :return:
    """
    val_tab -= len(str(chaine))
    espace = ""

    chaine = str(chaine)

    for e in range(1, val_tab - 1):
        espace += " "


    if separateur != "":
        espace += separateur + " "

    return espace


def remplir_espace(chaine):
    chaine = chaine.replace(" ", "_")
    return chaine


def analyse_argument(argument):
    x=0
    arguments = []
    for a in argument:
        x += 1
        if x == 1 and a != "-":
            arguments.append(argument)
            break
        else:
            arguments.append(a)

    return arguments





##################################################
#   API SOFT
##################################################


def affiche_menu(liste_menu):

    os.system('clear')

    print(Cd.jn)

    for cle in liste_menu.keys():
        print('   ', cle, '-', liste_menu[cle])

    print(Cd.std)


def make_list(path, def_repertoires, def_fichiers):

    # On se deplace a l'endroit de la videotheque
    os.chdir(path)

    list_base = os.listdir(path)

    genre = list_folder(list_base)
    mkv = list_ext(list_base, '.mkv')

    # AFFICHAGE A L'ECRAN :
    #######################

    os.system("clear")
    x = 0

    print('')
    print("========")
    print(def_repertoires, ":")
    print("========")
    for g in genre:
        x += 1
        space = tab(x, '-')
        print('    ', x, space, g)

    print('')
    print("===============")
    print(def_fichiers, ":")
    print("===============")

    liste_affichee = {}

    print('')
    for f in mkv:
        x += 1
        liste_affichee[x] = f
        space = tab(x, '-')
        print('    ', x, space, f)

    return liste_affichee


### Verifie la convention de fichier
def verif_conv(file):
    result = True

    # VERIF 1 : on verifie le nombre de split
    verif1 = file.split("-")

    if len(verif1) != 3:
        result = False

    else :
        # VERIF 2 : on verifie si le split 1 est une annee
        verif2=verif1[1]
        if verif2 not in str(range(1900, 2075)):
            result = False

        else:
            # VERIF 3 : on verifie le dernier split (qualite, genre, extension fichier)
            verif3 = verif1[1]
            verif3 = verif3.split('.')
            
            
            # 3: extension fichier :
            ext = ['mkv', 'avi', 'm2ts', 'iso', 'mp4', 'MKV', 'AVI', 'M2TS', 'ISO', 'MP4']
            if verif3[1] not in ext:
                result = False

    return result


### Verifie si le fichier est un fichier video
def is_video_file(file):

    ext1 = ['.mkv', '.avi', '.m2ts', '.iso', '.mp4']
    ext2 = os.path.splitext(file)[1]

    if ext2.lower() in ext1:
        return True
    else:
        return False


### Renvoie la liste des fichiers video
def video_files(files):
    new_liste = []
    for file in files:
        ext1 = ['.mkv', '.avi', '.m2ts', '.iso', '.mp4']
        ext2 = os.path.splitext(file)[1]

        if ext2.lower() in ext1:
            new_liste.append(file)
    return new_liste


### Nettoie une chaine de caracteres des caracteres specifies
def nettoyage_chaine(chaine):
    a_nettoyer = ['.', '-', '_']

    new_title = ""
    for c in chaine:
        if c in a_nettoyer:
            new_letter = " "
        else:
            new_letter = c
        new_title = new_title + new_letter

    new_title = new_title.strip(" ")  # supression des espaces avant et apres la chaine

    new_title = new_title.lower()

    sp = ['      ', '     ', '    ', '   ']
    for s in sp:
        new_title = new_title.replace(s, ' ')

    return new_title


### Extraction de l'annee a partir du nom du fichier
def extract_annee(file):
    annee = ''
    for an in range(1900, 2075):
        a = str(an)
        if a in file:
            annee = a
    return annee


### Extraction de la qualite a partir du nom du fichier
def extract_qualite(file):
    qualite = ''
    qual = ["720p", "1080p", "dvd", "divx"]
    reste = []

    for q in qual:
        if q.lower() in file.lower():
            qualite = q
    return qualite


### Extraction du titre a partir du nom du fichier
def extract_title(file):

    file = os.path.splitext(file)[0]

    annee = extract_annee(file)
    qualite = extract_qualite(file)
    reste = []

    # On commence a remplir la liste 'reste' qui sera composee de tous les elements
    # du nom du fichier (decoupe)
    # 1/ On decoupe a l'endroit de l'annee
    if annee != '':
        test1 = file.split(annee)
        for i in test1:
            reste.append(i)
    else:
        reste.append(file)

    # 2/ On decoupe s l'endroit de la qualite
    if qualite != '':
        for r in reste:
            if qualite in r:
                reste.remove(r)
                reste.append(r.split(qualite)[0])
                reste.append(r.split(qualite)[1])

    # On fait le tri dans la liste "reste"
    filtre = ['bluray', 'ac3', 'x264', 'zone-telechargement', 'multi', 'french']
    for e in filtre:
        for r in reste:
            if e.lower() in r.lower():
                reste.remove(r)  # si l'element se trouve dans la black liste

            if r == '':
                reste.remove(r)  # si l'element est ''

            if r == '.':
                reste.remove(r)  # si l'element est '.'

    x=0
    for r in reste:
        rr = nettoyage_chaine(r)
        reste[x] = rr
        x+=1

    return reste


def extract_genre(file):
    genreID = 0
    gen = [".g1.", ".g2.", ".g3.", ".g4.", ".g5.", ".g6.", ".g7.", ".g8.", ".g9", ".g10.", ".g11.", ".g12.", ".g13.", "-g1.", "-g2.", "-g3.", "-g4.", "-g5.", "-g6.", "-g7.", "-g8.", "-g9", "-g10.", "-g11.", "-g12.", "-g13."]

    x = 0
    for g in gen:
        x += 1
        if g in file:
            genreID = x

    return genreID


def genreF(id):
    genreName = ""
    if id == 0:
        genreName = ""

    if id == 1:
        genreName = "action"
    if id == 2:
        genreName = "policier, thriller, espionnage"
    if id == 3:
        genreName = "aventure"
    if id == 4:
        genreName = "catastrophe"
    if id == 5:
        genreName = "comedie, drame"
    if id == 6:
        genreName = "historique, guerre"
    if id == 7:
        genreName = "fantastique"
    if id == 8:
        genreName = "science fiction"
    if id == 9:
        genreName = "comics"
    if id == 10:
        genreName = "western"
    if id == 11:
        genreName = "horreur, epouvante"
    if id == 12:
        genreName = "animation"
    if id == 13:
        genreName = "making off"


    return genreName


def help():
    print("    ====")
    print("    HELP")
    print("    ====")
    print("    -a   : Tous les fichiers mkv")




##################################################
#   PROGRAMME
##################################################

def aa(ROOT):
    print("")

    # On fait la liste de tout ce qu'il y a dans le root:
    files = os.listdir(ROOT)

    # On filtre les fichiers :
    files = list_file(files)

    # On filtre les fichiers video :
    files = video_files(files)

    x = 1

    print("\n")
    print("====================================================================================================")
    print("\n")

    for file in files:

        rename(file, x)

        print("\n")
        print("====================================================================================================")
        print("\n")

        x += 1


def ww(ROOT):
    print("")

    # On fait la liste de tout ce qu'il y a dans le root:
    files = os.listdir(ROOT)

    # On filtre les fichiers :
    files = list_file(files)

    # On filtre les fichiers video :
    files = video_files(files)

    x = 1

    print("\n")
    print("====================================================================================================")
    print("\n")

    for file in files:
        if verif_conv(file) == False:
            rename(file, x)

            print("\n")
            print("====================================================================================================")
            print("\n")

            x += 1


def ff(ROOT):
    print("")

    # On fait la liste de tout ce qu'il y a dans le root:
    files = os.listdir(ROOT)

    # On filtre les fichiers :
    files = list_file(files)

    # On filtre les fichiers video :
    files = video_files(files)


    for file in files:
        if verif_conv(file):
            titre = file.split('-')[1]
            titre = titre.replace('.', ' ')

            titre1 = clr.gr + clr.fc + file.split('-')[0] + ' - ' + clr.std + clr.gr +  titre
            titre2 = clr.std + clr.fc + file.split('-')[2].split('.')[0]
            titre3 = file.split('-')[2].split('.')[1] + clr.std

            titre = titre1 + tab(titre1,"",90) + titre2 + tab(titre2,"",20) + titre3

            print(titre)

        else :
            print(clr.rg + file + clr.std)


def rename(file, x):
        annee = ""
        qualite = ""
        genreID = 0
        titles = []
        title = ""
        validation = False
        isnewtitle = False
        while validation == False:  # tant que la validation n'est pas faite
            # ==========================================================================================================
            # On assigne les variables :
            if annee == "":
                annee = extract_annee(file)
            if title == "":
                titles = extract_title(file)
                if len(titles) > 0:
                    title = titles[0]

            # ==========================================================================================================
            # On verifie la naming convention :
            verif = verif_conv(file)

            # ==========================================================================================================
            # On affiche les informations :
            if verif:
                print(clr.gr + "     ", x, ":", file)
            else:
                print(clr.rg + "     ", x, ":", file)

            if isnewtitle == False :
                title = title.lower()
            else:
                title = title

            print(clr.gr + "         ", "Titre   :" + clr.std, title)
            print(clr.gr + "         ", "Annee   :" + clr.std, annee, '\n')

            new_file = title + " - " + annee + os.path.splitext(file)[1]
            # new_file = annee + " - " remplir_espace(title) + "-" + annee + "." + os.path.splitext(file)[1]

            print("          "+new_file)

            print(clr.jn)

            # ==========================================================================================================
            # On affiche le menu :
            print("          1       : changer le titre")
            print("          2       : changer l'annee")
            print("          3       : enregistrer les changements")
            print("          entree  : pas de changements")
            print("")
            print("          0       : EFFACER LE FICHIER", clr.std, "\n")


            # ==========================================================================================================
            # On affiche l'invite de saisie :
            choix = input("          Choix : ")

            # ==========================================================================================================
            # On analyse le choix :
            if choix == '0':
                annee = ""
                qualite = ""
                titles = []
                title = ""

                os.remove(file)

                validation = True

            elif choix == '1':    # Changer l'annee ---------------------------------------
                title = input("          Title : ")
                isnewtitle = True

            elif choix == '2':  # Changer la qualite ---------------------------------------
                annee = input("          Annee : ")


            elif choix == '':  # --- ANNULATION --- ---------------------------------------
                # annee = ""
                # titles = []
                # title = ""

                validation = True

            elif choix == '3':   # --- VALIDATION --- ---------------------------------------
                annee = ""
                titles = []
                title = ""


                if file != new_file:
                    os.rename(file, new_file)

                validation = True

            else:   # Si une chaine de carac ds la saisie -> new titre
                title = choix

            # ==========================================================================================================


def test(ROOT):
    os.system("clear")

    files = os.listdir(ROOT)
    for f in files:
        tt = verif_conv(f)
        print(tt)



####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################








PATH = os.getcwd()

aa(PATH)








