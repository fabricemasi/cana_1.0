#! /bin/bash

debug "${BASH_SOURCE[0]}" in

jh ()
{
	python "$BIN/python/jh.py"
}

jhh ()
{
    cat "$BIN/data/pipe_set_history.txt"
}

debug "${BASH_SOURCE[0]}" out