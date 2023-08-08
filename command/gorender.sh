#! /bin/bash

debug "${BASH_SOURCE[0]}" in

gorender ()
{
	if [[ $PROJ != "" ]] && [[ $TYPE != "" ]] && [[ $NAME != "" ]] && [[ $DISC != "" ]]; then
		if [[ -e $RENDER ]]; then
		    cd $RENDER
		else
		    mkdir $RENDER -p
		    cd $RENDER
		fi
	else
		echo "ABORTED. Vous n'etes pas sette correctement."
	fi
}

debug "${BASH_SOURCE[0]}" out