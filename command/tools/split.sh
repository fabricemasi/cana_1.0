#! /bin/bash

split (){

    IFS="$2" read -ra spl <<< "$1"
    return spl

}