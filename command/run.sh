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


run () {

    pyt "run.py" $1,$2,$3,$4,$5

    fill_var_env
    determine_path_to_go
    cd $path_to_go
    remove_returns

    ps1
}




fill_var_env ()
{
    declare -a names=(${RETURN1})
    declare -a roots=(${RETURN2})
    declare -a paths=(${RETURN3})

    export TYPE=${names[0]}
    export ROOT_TYPE=${roots[0]}
    export PATH_TYPE=${paths[0]}

    export PROJ=${names[1]}
    export ROOT_PROJ=${roots[1]}
    export PATH_PROJ=${paths[1]}

    export FOLD=${names[2]}
    export ROOT_FOLD=${roots[2]}
    export PATH_FOLD=${paths[2]}

    export SOFT=${names[3]}
    export ROOT_SOFT=${roots[3]}
    export PATH_SOFT=${paths[3]}

}


determine_path_to_go ()
{
    declare -a names=(${RETURN1})

    if [[ ${names[0]} == "" ]] && [[ ${names[1]} == "" ]] && [[ ${names[2]} == "" ]] && [[ ${names[3]} == "" ]]; then
        path=$PATH_CHANTIER
    fi
    if [[ ${names[0]} != "" ]] && [[ ${names[1]} == "" ]] && [[ ${names[2]} == "" ]] && [[ ${names[3]} == "" ]]; then
        path=$PATH_TYPE
    fi
    if [[ ${names[0]} != "" ]] && [[ ${names[1]} != "" ]] && [[ ${names[2]} == "" ]] && [[ ${names[3]} == "" ]]; then
        path=$PATH_PROJ
    fi
    if [[ ${names[0]} != "" ]] && [[ ${names[1]} != "" ]] && [[ ${names[2]} != "" ]] && [[ ${names[3]} == "" ]]; then
        path=$PATH_FOLD
    fi
    if [[ ${names[0]} != "" ]] && [[ ${names[1]} != "" ]] && [[ ${names[2]} != "" ]] && [[ ${names[3]} != "" ]]; then
        path=$PATH_SOFT
    fi

    path_to_go=$path

}



debug "${BASH_SOURCE[0]}" out
