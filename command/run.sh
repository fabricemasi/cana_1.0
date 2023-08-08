#! /bin/bash

# Creation des variables
#  - TYPE
#  - ROOT_TYPE



debug "${BASH_SOURCE[0]}" in


run () {
# $1 = arg_step      : type, projet, folder ou soft
# $2 = nom           : nom du repertoire a selectionner
# $3 = mode_furtif   : si =0, les affichages terminal apparaitront


    input="$1"
    arg=$(echo "$input" | tr '[:upper:]' '[:lower:]')

    if [[ $arg == "type" ]]; then
        pyt "$BIN/python/run.py" "$1","$2","$3"

        # On desactive toutes les variables sauf type
        killpipe "type"
        export TYPE=$RETURN1
        export ROOT_TYPE=$RETURN2

        if [[ $AUTORUN == 0 ]]; then
            cd "$ROOT_TYPE" || return
        fi
	fi

    if [[ $arg == "projet" ]]; then
        if [[ $TYPE != "" ]]; then
            pyt "$BIN/python/run.py" "$1","$2","$3"

            # On desactive toutes les variables sauf type
            killpipe "projet"
            export PROJET=$RETURN1
            export ROOT_PROJET=$RETURN2

            if [[ $AUTORUN == 0 ]]; then
                cd "$ROOT_PROJET" || return
            fi
        else
            echo -e "$JAUNE"
            echo "Erreur, vous devez setter un type de projet avant cette etape."
        fi
	fi

	if [[ $arg == "folder" ]]; then
        if [[ $TYPE != "" ]] && [[ $PROJET != "" ]]; then
            pyt "$BIN/python/run.py" "$1","$2","$3"

            # On desactive toutes les variables sauf type
            killpipe "folder"
            export FOLDER=$RETURN1
            export ROOT_FOLDER=$RETURN2

            if [[ $AUTORUN == 0 ]]; then
                cd "$ROOT_FOLDER" || return
            fi
        else
            echo -e "$JAUNE"
            echo "Erreur, vous devez setter un type de projet et un projet avant cette etape."
        fi
	fi

    remove_returns
    ps1

}


debug "${BASH_SOURCE[0]}" out
