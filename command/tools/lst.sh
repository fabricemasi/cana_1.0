#! /bin/bash

# Arguments :   1 : msg 1 = renseignement sur les variables de set deja crees
#               2 : msg 2 = renseignement sur ce qu'est la liste affichee
#               3 : path ou se positionner
#               4 : nombre d'indentations pour tree
#               5 : msg 3 = Message de sortie

debug "${BASH_SOURCE[0]}" in

lst ()
{
	msg1=$1
	msg2=$2
	path=$3
	indent=$4
	msg3=$5

	cd $path
	liste=$(ls)


    echo -e $GRIS2"=============================================================================================================="
	echo -e $GRIS2' '$msg1
    echo -e $GRIS2"--------------------------------------------------------------------------------------------------------------"
    echo -e $GRIS2' '$msg2
    echo ""
    for l in $liste; do
	echo " - "$l
	done
	echo ""
    echo -e $GRIS2"=============================================================================================================="
	echo ""
	echo -e ${COLOR4}$msg3${NEUTRE}
}


debug "${BASH_SOURCE[0]}" out
