#!/usr/bin/env bash

debug "${BASH_SOURCE[0]}" in

killpipe ()
{
	if [[ $# == 0 ]]; then
	    unset TYPE
        unset PROJET
        unset FOLDER
        unset SOFT

        unset ROOT_TYPE
        unset ROOT_PROJET
        unset ROOT_FOLDER
        unset ROOT_SOFT

        cd ~
	    ps1
	else
	    input="$1"
        arg=$(echo "$input" | tr '[:upper:]' '[:lower:]')


	    if [[ $arg == "type" ]]; then
            unset PROJET
            unset FOLDER
            unset SOFT

            unset ROOT_PROJET
            unset ROOT_FOLDER
            unset ROOT_SOFT
        elif [[ $arg == "projet" ]]; then
            unset FOLDER
            unset SOFT

            unset ROOT_FOLDER
            unset ROOT_SOFT
        elif [[ $arg == "folder" ]]; then
            unset SOFT

            unset ROOT_SOFT
        fi
    fi


}

debug "${BASH_SOURCE[0]}" out