#! /bin/bash

debug "${BASH_SOURCE[0]}" in

goprojet ()
{
	if [[ $PROJ != "" ]]; then
		cd $ROOT_PROJ
	else
		echo "ABORTED. Vous n'etes pas sette correctement."
	fi
}

debug "${BASH_SOURCE[0]}" out