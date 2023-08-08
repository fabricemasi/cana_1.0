#! /bin/bash

debug "${BASH_SOURCE[0]}" in

gocam ()
{
	if [[ $PROJ != "" ]] && [[ $TYPE != "" ]] && [[ $NAME != "" ]]; then
		if [[ -e $CAM ]]; then
		    cd $CAM
		else
		    mkdir $CAM -p
		    cd $CAM
		fi
	else
		echo "ABORTED. Vous n'etes pas sette correctement."
	fi
}

debug "${BASH_SOURCE[0]}" out