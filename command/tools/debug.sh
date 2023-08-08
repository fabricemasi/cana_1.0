#!/usr/bin/env bash

# Permet d'afficher des informations si $VERBOSE>0 - Interet : uniformiser les couleurs d'affichage.
# -----------------------------------------------------------------------------------------------


debug()
{
    if [[ $VERBOSE == 1 ]]; then
        IFS="/" read -ra test <<< "$1"
        echo " - " ${test[${#test}-1]} - "${2^^}"
        sleep 0.01
    fi
}

