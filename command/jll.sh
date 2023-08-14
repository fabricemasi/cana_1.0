#! /bin/bash
# Load le dernier set proj

debug "${BASH_SOURCE[0]}" in

jll (){
    source $BIN/data/pipe_set.sh
    job $TYPE $PROJ $FOLD
}

debug "${BASH_SOURCE[0]}" out