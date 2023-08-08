#! /bin/bash

debug "${BASH_SOURCE[0]}" in

jh ()
{
	python "$BIN/python/pipe_set_history_filtre.py"
}

jhh ()
{
    cat "$BIN/data/pipe_set_history.txt"
}

debug "${BASH_SOURCE[0]}" out