#! /bin/bash

# GESTION DES VARIABLES :
#  - TYPE
#  - ROOT_TYPE
#  - PROJ
#  - ROOT_PROJ
#  - FOLD
#  - ROOT_FOLD
#  - SOFT
#  - ROOT_SOFT


debug "${BASH_SOURCE[0]}" in


# $1 - $2 = les deux arguments sont switchables :
# - nom du repertoire a selectionner
# - valeurs suivantes : (-t, -p, -f, -s, type, proj, fold, soft)
run () {

    format_variables

    pyt "run.py" "$1","$2"

    export NAME=$RETURN1
    export STEP=$RETURN2
    export ROOT_STEP=$RETURN3
    export PATH_STEP=$RETURN4

    fill_steps $NAME $STEP $ROOT_STEP $PATH_STEP

    remove_returns
    ps1
}

fill_steps () {
    if [[ $2 == "type" ]]; then
        export TYPE=$1
        export ROOT_TYPE=$3
        export PATH_TYPE=$4
    elif [[ $2 == "proj" ]]; then
        export PROJ=$1
        export ROOT_PROJ=$3
        export PATH_PROJ=$4
    elif [[ $2 == "fold" ]]; then
        export FOLD=$1
        export ROOT_FOLD=$3
        export PATH_FOLD=$4
    elif [[ $2 == "soft" ]]; then
        export SOFT=$1
        export ROOT_SOFT=$3
        export PATH_SOFT=$4
    fi
}

format_variables () {
    if [[ $TYPE == "" ]]; then
        export TYPE=""
    fi
    if [[ $ROOT_TYPE == "" ]]; then
        export ROOT_TYPE=""
    fi
    if [[ $PATH_TYPE == "" ]]; then
        export PATH_TYPE=""
    fi



    if [[ $PROJ == "" ]]; then
        export PROJ=""
    fi
    if [[ $ROOT_PROJ == "" ]]; then
        export ROOT_PROJ=""
    fi
    if [[ $PATH_PROJ == "" ]]; then
        export PATH_PROJ=""
    fi



    if [[ $FOLD == "" ]]; then
        export FOLD=""
    fi
    if [[ $ROOT_FOLD == "" ]]; then
        export ROOT_FOLD=""
    fi
    if [[ $PATH_FOLD == "" ]]; then
        export PATH_FOLD=""
    fi



    if [[ $SOFT == "" ]]; then
        export SOFT=""
    fi
    if [[ $ROOT_SOFT == "" ]]; then
        export ROOT_SOFT=""
    fi
    if [[ $PATH_SOFT == "" ]]; then
        export PATH_SOFT=""
    fi
}


debug "${BASH_SOURCE[0]}" out




#    input="$1"
#    arg=$(echo "$input" | tr '[:upper:]' '[:lower:]')
#
#    if [[ $arg == "type" ]]; then
#        pyt "$BIN/python/run.py" "$1","$2","$3"
#
#        # On desactive toutes les variables sauf type
#        killpipe "type"
#        export TYPE=$RETURN1
#        export ROOT_TYPE=$RETURN2
#
#        if [[ $AUTORUN == 0 ]]; then
#            cd "$ROOT_TYPE" || return
#        fi
#	fi
#
#    if [[ $arg == "proj" ]]; then
#        if [[ $TYPE != "" ]]; then
#            pyt "$BIN/python/run.py" "$1","$2","$3"
#
#            # On desactive toutes les variables sauf type
#            killpipe "proj"
#            export PROJ=$RETURN1
#            export ROOT_PROJ=$RETURN2
#
#            if [[ $AUTORUN == 0 ]]; then
#                cd "$ROOT_PROJ" || return
#            fi
#        else
#            echo -e "$JAUNE"
#            echo "Erreur, vous devez setter un type de proj avant cette etape."
#        fi
#	fi
#
#	if [[ $arg == "fold" ]]; then
#        if [[ $TYPE != "" ]] && [[ $PROJ != "" ]]; then
#            pyt "$BIN/python/run.py" "$1","$2","$3"
#
#            # On desactive toutes les variables sauf type
#            killpipe "fold"
#            export FOLD=$RETURN1
#            export ROOT_FOLD=$RETURN2
#
#            if [[ $AUTORUN == 0 ]]; then
#                cd "$ROOT_FOLD" || return
#            fi
#        else
#            echo -e "$JAUNE"
#            echo "Erreur, vous devez setter un type de proj et un proj avant cette etape."
#        fi
#	fi