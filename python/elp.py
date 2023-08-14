# coding: utf-8
# !/usr/bin/python
import os

print(f"""
VARIABLES:
AUTORUN = {os.environ["AUTORUN"]}
VERBOSE = {os.environ["VERBOSE"]}
ROOT_PIPE = {os.environ["ROOT_PIPE"]}
FOLD_PIPE = {os.environ["FOLD_PIPE"]}
PATH_PIPE = {os.environ["PATH_PIPE"]}
ROOT_CHANTIER = {os.environ["ROOT_CHANTIER"]}
FOLD_CHANTIER = {os.environ["FOLD_CHANTIER"]}
PATH_CHANTIER = {os.environ["PATH_CHANTIER"]}
ROOT_ARCHIVES = {os.environ["ROOT_ARCHIVES"]}
FOLD_ARCHIVES = {os.environ["FOLD_ARCHIVES"]}
PATH_ARCHIVES = {os.environ["PATH_ARCHIVES"]}









""")





#    echo -e ""$ROUGE
#    echo -e "===================="
#    echo -e "HELP $BINV"
#    echo -e "===================="
#    echo -e ""${BLANC}${GRAS}
#    echo -e "COMMANDES :"
#    echo -e ""$STANDARD
#    printf "%-31s %s\n" "settype :"                 "Setter un type de proj"
#    printf "%-31s %s\n" "setproj :"                 "Setter un proj"
#    printf "%-31s %s\n" "setfold :"                 "Setter un fold (sous-repertoire de proj)"
#    printf "%-31s %s\n" "job :"                     "Super utilisation des commandes de set"
#    printf "%-31s %s\n" "jh :"                      "Afficher l'historique des precedents sets"
#    printf "%-31s %s\n" "jhh :"                     "idem 'jh' sans filtre de doublons, et avec heure de set"
#    printf "%-31s %s\n" "jll :"                     "Setter le dernier proj de l'historique"
#    printf "%-31s %s\n" "killpipe :"                "Reinitialise les variables du pipe"
#    echo -e ""${BLANC}${GRAS}
#    echo -e "TRICS :"
#    echo -e ""$STANDARD
#    echo -e "Sublime : Replier tout ........ Ctrl k 1 "
#    echo -e "Utiliser la couleur ........... echo -e \$BLANC"
#    echo -e "extract ....................... Extraire des fichiers compresses"
#    echo -e ""
#    echo -e "${BLANC}${GRAS}VARIABLES PRINCIPALES :${STANDARD}"
#    echo -e ""
#    echo -e "RAPPEL : "
#    echo -e "ROOT_PIPE / chantier / TYPE / PROJ / FOLD "
#    echo -e "TYPE .......................... $TYPE"
#    echo -e "ROOT_TYPE ..................... $ROOT_TYPE"
#    echo -e "PROJ .......................... $PROJ"
#    echo -e "ROOT_PROJ ..................... $ROOT_PROJ"
#    echo -e "FOLD .......................... $FOLD"
#    echo -e "ROOT_SOFT ..................... $ROOT_SOFT"
#    echo -e "SOFT .......................... $SOFT"
#    echo -e "ROOT_FOLD ..................... $ROOT_FOLD"
#    echo -e "VERBOSE ....................... $VERBOSE ${GRIS} (init_01) ${NEUTRE}"
#    echo -e ""
#    echo -e "${BLANC}${GRAS}PATHS :${STANDARD}"
#    echo -e ""
#    echo -e "BINV .......................... $BINV ${GRIS} (bashrc) ${NEUTRE}"
#    echo -e "BIN ........................... $BIN ${GRIS} (bashrc) ${NEUTRE}"
#    echo -e "CACHE ......................... $CACHE ${ROUGE}(A creer)${NEUTRE}"
#    echo -e "RENDER ........................ $RENDER ${ROUGE}(A creer)${NEUTRE}"
#    echo -e "ROOT_PIPE ..................... $ROOT_PIPE ${GRIS} (init_03) ${NEUTRE}"
#    echo -e "ROOT_TEMP ..................... $ROOT_TEMP ${GRIS} (init_03) ${NEUTRE} ${ROUGE}(A creer)${NEUTRE}"
#    echo -e "ROOT_PUBLISH .................. $ROOT_PUBLISH${ROUGE}(A creer)${NEUTRE}"
#    echo -e ""
#    echo -e "${BLANC}${GRAS}LOGICIELS :${STANDARD}"
#    echo -e "${CYAN} $LISTE_SOFTS"
