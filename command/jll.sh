#! /bin/bash
# Load le dernier set projet

debug "${BASH_SOURCE[0]}" in

jll (){
    source $BIN/data/pipe_set.sh
    job $TYPE $PROJET $FOLDER
}

debug "${BASH_SOURCE[0]}" out