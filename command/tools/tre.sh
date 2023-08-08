#! /bin/bash

debug "${BASH_SOURCE[0]}" in

tre ()
{
    if [[ $# == 1 ]]; then
        tree -I '__*' -L $1 -v
    fi
}

debug "${BASH_SOURCE[0]}" out