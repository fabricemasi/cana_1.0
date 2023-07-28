#!/usr/bin/env bash

elp ()
{
    echo -e ""$ROUGE
    echo -e "===================="
    echo -e "HELP $BINV"
    echo -e "===================="
    echo -e ""${BLANC}${GRAS}
    echo -e "COMMANDES :"
    echo -e ""$STANDARD
    echo -e "settype ....................... Setter un type de projet"
    echo -e "setprojet ..................... Setter un projet"
    echo -e "setfolder ..................... Setter un folder (sous-repertoire de projet)"
    echo -e "job ........................... Super utilisation des commandes de set"
    echo -e "jh ............................ Afficher l'historique des precedents sets"
    echo -e "jhh ........................... idem 'jh' sans filtre de doublons, et avec heure de set"
    echo -e "jll ........................... Setter le dernier projet de l'historique"
    echo -e "killpipe ...................... Reinitialise les variables du pipe"
    echo -e ""${BLANC}${GRAS}
    echo -e "TRICS :"
    echo -e ""$STANDARD
    echo -e "Sublime : Replier tout ........ Ctrl k 1 "
    echo -e "Utiliser la couleur ........... echo -e \$BLANC"
    echo -e "extract ....................... Extraire des fichiers compresses"
    echo -e ""
    echo -e "${BLANC}${GRAS}VARIABLES PRINCIPALES :${STANDARD}"
    echo -e ""
    echo -e "RAPPEL : "
    echo -e "ROOT_PIPE / chantiers / TYPE / PROJET / FOLDER "
    echo -e "TYPE .......................... $TYPE"
    echo -e "PROJET ........................ $PROJET"
    echo -e "FOLDER ........................ $FOLDER"
    echo -e "SOFT .......................... $SOFT"
    echo -e "VERBOSE ....................... $VERBOSE ${GRIS} (init_01) ${NEUTRE}"
    echo -e ""
    echo -e "${BLANC}${GRAS}PATHS :${STANDARD}"
    echo -e ""
    echo -e "BINV .......................... $BINV ${GRIS} (bashrc) ${NEUTRE}"
    echo -e "BIN ........................... $BIN ${GRIS} (bashrc) ${NEUTRE}"
    echo -e "CACHE ......................... $CACHE ${ROUGE}(A creer)${NEUTRE}"
    echo -e "RENDER ........................ $RENDER ${ROUGE}(A creer)${NEUTRE}"
    echo -e "ROOT_PIPE ..................... $ROOT_PIPE ${GRIS} (init_03) ${NEUTRE}"
    echo -e "ROOT_TEMP ..................... $ROOT_TEMP ${GRIS} (init_03) ${NEUTRE} ${ROUGE}(A creer)${NEUTRE}"
    echo -e "ROOT_TYPE ..................... $ROOT_TYPE"
    echo -e "ROOT_PROJET ................... $ROOT_PROJET ${GRIS} (init_03) ${NEUTRE}"
    echo -e "ROOT_FOLDER ................... $ROOT_FOLDER"
    echo -e "ROOT_SOFT ..................... $ROOT_SOFT"
    echo -e "ROOT_PUBLISH .................. $ROOT_PUBLISH${ROUGE}(A creer)${NEUTRE}"
    echo -e ""
    echo -e "${BLANC}${GRAS}LOGICIELS :${STANDARD}"
    echo -e "${CYAN} $LISTE_SOFTS"
}