#! /bin/bash

# Creation des variables
#  - TYPE
#  - ROOT_TYPE


debug "${BASH_SOURCE[0]}" in



setproj ()
{
    export PROJ=""
    export FOLD=""
    export SOFT=""

    export ROOT_PROJ=""
    export ROOT_FOLD=""
    export ROOT_SOFT=""

	condition=0

    #  0 argument :
	#----------------------------------------------------------------------------
    if [[ $# == 0 ]]; then
        export PROJ=""
        export FOLD=""
        export ROOT_PROJ=""
        export ROOT_FOLD=""

	    condition=1
    fi

    #  1 argument :
	#----------------------------------------------------------------------------
    if [[ $# == 1 ]]; then

        path=$ROOT_TYPE/$1

        # si le type n'existe pas :
        if ! [[ -e $path ]]; then
        	echo -e ${GRIS2} ""
            read -p "Le proj $1 n'existe pas. Voulez vous le creer ? (o,n) " reponse
			echo -e ${NEUTRE} ""
            if [[ $reponse == "o" ]]; then
                mkdir $path
                proj=$1
			    condition=0
            elif [[ $reponse == "n" ]]; then
                condition=1
            else
                echo "Erreur de saisie, commande annulee. (setproj 1) "
                condition=1
            fi
        # si le type existe :
        else
            proj=$1
            # si le dernier caractere est "/" on le supprime
            if [[ ${proj: -1} == "/" ]]; then
                proj=${proj:: -1}
            fi
            condition=0
        fi
    fi

    #  2 arguments :
	#----------------------------------------------------------------------------
    if [[ $# == 2 ]]; then
        settype $1
        setproj $2
    fi

    #  trop d' argument :
	#----------------------------------------------------------------------------
    if [[ $# > 2 ]]; then
        echo "Erreur de saisie, commande annulee. (setproj 2) "
        condition=1
    fi










    # =============================================
    #  resultat :
    # =============================================

    clear

    if [[ $condition == 0 ]]; then

        export PROJ=$proj
        export ROOT_PROJ=$ROOT_TYPE/$PROJ




        if [[ $AUTORUN == 0 ]]; then
            cd $ROOT_PROJ
            lst     "${NEUTRE}${COLOR0}TYPE....... ${COLOR3}$TYPE${COLOR0} \n PROJ..... ${COLOR3}$PROJ"   "Liste des repertoires pour le proj ${COLOR3}$PROJ${COLOR0} :"   $ROOT_PROJ   1   ${COLOR4}${GRAS}"Vous devez setter un sous-repertoire (fold) : 'setfold' ou 's'"
        fi

        # Lance la commande setfold si il n'y a qu'un seul fold
        nb_fold=`ls -l | grep ^d |wc -l`
        if [[ $nb_fold == 1 ]]; then
            fold=`ls`
            setfold $fold
        fi

    elif [[ $condition == 1 ]]; then
        export PROJ=""
        export ROOT_PROJ=""

        cd $ROOT_TYPE
		lst     "TYPE   = ${COLOR4}$TYPE${COLOR0}"   "Liste de projs de type $TYPE :"   $ROOT_TYPE   1   ${COLOR4}${GRAS}"Vous devez setter un proj : 'setproj' ou 'p'"
    fi


    ps1




}

debug "${BASH_SOURCE[0]}" out