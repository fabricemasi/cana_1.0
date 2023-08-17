#!/usr/bin/env bash

debug "${BASH_SOURCE[0]}" in

killpipe ()
{
	if [[ $# == 0 ]]; then
	    unset TYPE
        unset PROJ
        unset FOLD
        unset SOFT

        unset ROOT_TYPE
        unset ROOT_PROJ
        unset ROOT_FOLD
        unset ROOT_SOFT

        unset PATH_TYPE
        unset PATH_PROJ
        unset PATH_FOLD
        unset PATH_SOFT

        cd ~
        clear
	    ps1
	else
	    input="$1"
        arg=$(echo "$input" | tr '[:upper:]' '[:lower:]')


	    if [[ $arg == "type" ]]; then
            unset PROJ
            unset FOLD
            unset SOFT

            unset ROOT_PROJ
            unset ROOT_FOLD
            unset ROOT_SOFT
        elif [[ $arg == "proj" ]]; then
            unset FOLD
            unset SOFT

            unset ROOT_FOLD
            unset ROOT_SOFT
        elif [[ $arg == "fold" ]]; then
            unset SOFT

            unset ROOT_SOFT
        fi
    fi


}

debug "${BASH_SOURCE[0]}" out