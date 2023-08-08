#! /bin/bash

debug "${BASH_SOURCE[0]}" in

gocache ()
{
	if [[ $PROJ != "" ]] && [[ $TYPE != "" ]] && [[ $NAME != "" ]] && [[ $DISC != "" ]]; then
		if [[ -e $CACHE ]]; then
		    cd $CACHE
		else
		    mkdir $CACHE -p
		    cd $CACHE
		fi
	else
		echo "ABORTED. Vous n'etes pas sette correctement."
	fi
}

debug "${BASH_SOURCE[0]}" out