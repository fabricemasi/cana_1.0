#! /bin/bash
# Load le dernier set proj

debug "${BASH_SOURCE[0]}" in

jll (){
    pyt "jll.py"

    declare -a names=("${RETURN1}")

    run "${RETURN1}" "${RETURN2}" "${RETURN3}" "${RETURN4}"
}

debug "${BASH_SOURCE[0]}" out