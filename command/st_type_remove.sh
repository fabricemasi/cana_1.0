#! /bin/bash

# Creation des variables
#  - TYPE
#  - ROOT_TYPE


debug "${BASH_SOURCE[0]}" in

type_remove () {

    pyt "$BIN/python/st_type_remove.py" $1,$2,$3,$4

    export TYPE=$RETURN1
    export ROOT_TYPE=$RETURN2

    remove_returns

    if [[ $AUTORUN == 0 ]]; then
        cd $ROOT_TYPE
    fi

    ps1
}

debug "${BASH_SOURCE[0]}" out
