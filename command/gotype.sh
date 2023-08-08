#! /bin/bash

debug "${BASH_SOURCE[0]}" in

gotype ()
{
	if [[ $PROJ != "" ]] && [[ $TYPE != "" ]]; then
		cd $ROOT_TYPE
	else
		echo "ABORTED. Vous n'etes pas sette correctement."
	fi
}

debug "${BASH_SOURCE[0]}" out