#! /bin/bash

debug "${BASH_SOURCE[0]}" in


setfold ()
{
    export FOLD=""
	export SOFT=""

	export ROOT_FOLD=""
	export ROOT_SOFT=""

	condition=0
    msg=""

	#  0 argument :
	#----------------------------------------------------------------------------
	if [[ $# == 0 ]]; then
	    if [[ $TYPE == "" ]] && [[ $PROJ == "" ]]; then
	        msg="${COLOR4}${GRAS}Aucun type ni proj n'a encore ete sette. Utilisez les commandes 'settype' et 'setproj'."
	        condition=2
	    elif [[ $TYPE != "" ]] && [[ $PROJ == "" ]]; then
	        msg="${COLOR4}${GRAS}Aucun proj n'a ete sette. Utilisez la commande 'setproj'."
	        condition=2
	    elif [[ $TYPE != "" ]] && [[ $PROJ != "" ]]; then
	        condition=1
	    fi
	fi

	#  1 argument :
	#----------------------------------------------------------------------------
	if [[ $# == 1 ]]; then

		path=$ROOT_PROJ/$1

		# si le proj n'existe pas :
		if ! [[ -e $path ]]; then
			echo -e ${COLOR4} ""
			read -p "Le sous-repertoire $1 n'existe pas. Voulez vous le créer ? (o,n) " reponse
			echo -e ${NEUTRE} ""

			if [[ $reponse == "o" ]]; then
				mkdir $path
				mkdir $path/01_ref
				mkdir $path/02_work
				mkdir $path/03_temp
				mkdir $path/04_publish
				mkdir $path/05_final
				msg="Espace de travail cree."
				condition=0

			elif [[ $reponse == "n" ]]; then
                msg="Commande annulee."
                condition=1

			else
				msg="Erreur de saisie, commande annulee. (setfold_1)."
				condition=1

			fi
		# si le sous-repertoire existe :
		else
			condition=0
		fi
	fi

	#  trop d'argument :
	#----------------------------------------------------------------------------
	if [[ $# > 1 ]]; then
	    msg "Erreur de saisie (trop d'arguments), commande annulee. (setfold_2)."
	    condition=1

	fi










	# =============================================
	#  resultat :
	# =============================================

    clear

	if [[ $condition == 0 ]]; then
		fold=$1
		if [[ ${fold: -1} == "/" ]]; then
			 	fold=${fold:: -1}
		fi



		export FOLD=$fold
		export ROOT_FOLD=$ROOT_PROJ/$fold



#        export REF=$ROOT_PIPE/projs/$TYPE/$NAME/01_ref
#		 export WORK=$ROOT_PIPE/projs/$TYPE/$NAME/02_work
#        export TEMP=$ROOT_PIPE/projs/$TYPE/$NAME/03_temp
#        export PUBLISH=$ROOT_PIPE/projs/$TYPE/$NAME/04_publish
#        export FINAL=$ROOT_PIPE/projs/$TYPE/$NAME/05_final
#
#        if [[ $SYSTEM == "windows" ]]; then
#            echo "Systeme detecte : WINDOWS"
#            echo "  -> Correction de la variable d'environnement 'PUBLISH'"
#            publish_w=""$ROOT_PIPE_W"\\projs\\"$TYPE"\\"$NAME"\\04_publish"
#            /mnt/c/Windows/System32/reg.exe add "HKCU\Environment" /v PUBLISH /t REG_SZ /d $publish_w /f
#        fi
#
#
#

        echo "#!/bin/bash" > $BIN/data/pipe_set.sh
        echo "export TYPE='"$TYPE"'" >> $BIN/data/pipe_set.sh
        echo "export PROJ='"$PROJ"'" >> $BIN/data/pipe_set.sh
        echo "export FOLD='"$FOLD"'" >> $BIN/data/pipe_set.sh

        dt=`date +%F"--"%T`

        echo $dt-----job $TYPE $PROJ $FOLD >> $BIN/data/pipe_set_history.txt
        echo -e ${BLEU}${GRAS}
        echo -e "Enregistrement des donnees de set OK."
        echo -e ${NEUTRE}
        lst     "${NEUTRE}${COLOR0}TYPE....... ${COLOR3}$TYPE${COLOR0} \n PROJ..... ${COLOR3}$PROJ${COLOR0} \n FOLD..... ${COLOR3}$FOLD"   "Liste des espaces de travail pour le proj ${COLOR3}$PROJ${COLOR0}${GRAS} / ${COLOR3}$FOLD${COLOR0}${GRAS} :"   $ROOT_FOLD/02_work   1   ${COLOR4}${GRAS}"Vous devez setter un software"

        cd $ROOT_FOLD

        ps1

	elif [[ $condition == 1 ]]; then
        cd $ROOT_PROJ
        cl
        lst     "${NEUTRE}${COLOR0}TYPE....... ${COLOR3}$TYPE${COLOR0} \n PROJ..... ${COLOR3}$PROJ"   "Liste des repertoires pour le proj ${COLOR3}$PROJ${COLOR0} :"   $ROOT_PROJ   1   ${COLOR4}${GRAS}"Vous devez setter un sous-repertoire (fold) : 'setfold' ou 's3'"

        echo ""
        echo $msg

		ps1
	elif [[ $condition == 2 ]]; then
        cd $ROOT_PROJ

        echo ""
        echo -e ${COLOR6}${GRAS}$msg${NEUTRE}
		ps1
	fi
}




debug "${BASH_SOURCE[0]}" out




