#! /bin/bash

debug "${BASH_SOURCE[0]}" in

goname ()
{
	if [[ $PROJ != "" ]] && [[ $TYPE != "" ]] && [[ $NAME != "" ]]; then
		cd $ROOT_NAME
	else
		echo "ABORTED. Vous n'etes pas sette correctement."
	fi
}

debug "${BASH_SOURCE[0]}" out