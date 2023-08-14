#! /bin/bash

var () {
    echo -e $NOIR2'===================================================================================================='
    printf "${NOIR2}${GRAS}%-10s %-15s\n" "TYPE" "= ${NEUTRE}${BLEU} $TYPE ${NEUTRE}"
    printf "${NOIR2}${GRAS}%-10s %-15s\n" "ROOT_TYPE" "= ${NEUTRE}${BLEU} $ROOT_TYPE ${NEUTRE}"
    printf "${NOIR2}${GRAS}%-10s %-15s\n" "PATH_TYPE" "= ${NEUTRE}${BLEU} $PATH_TYPE ${NEUTRE}"
    echo -e $NOIR2'----------------------------------------------------------------------------------------------------'
    printf "${NOIR2}${GRAS}%-10s %-15s\n" "PROJ" "= ${NEUTRE}${BLEU} $PROJ ${NEUTRE}"
    printf "${NOIR2}${GRAS}%-10s %-15s\n" "ROOT_PROJ" "= ${NEUTRE}${BLEU} $ROOT_PROJ ${NEUTRE}"
    printf "${NOIR2}${GRAS}%-10s %-15s\n" "PATH_PROJ" "= ${NEUTRE}${BLEU} $PATH_PROJ ${NEUTRE}"
    echo -e $NOIR2'----------------------------------------------------------------------------------------------------'
    printf "${NOIR2}${GRAS}%-10s %-15s\n" "FOLD" "= ${NEUTRE}${BLEU} $FOLD ${NEUTRE}"
    printf "${NOIR2}${GRAS}%-10s %-15s\n" "ROOT_FOLD" "= ${NEUTRE}${BLEU} $ROOT_FOLD ${NEUTRE}"
    printf "${NOIR2}${GRAS}%-10s %-15s\n" "PATH_FOLD" "= ${NEUTRE}${BLEU} $PATH_FOLD ${NEUTRE}"
    echo -e $NOIR2'----------------------------------------------------------------------------------------------------'
    printf "${NOIR2}${GRAS}%-10s %-15s\n" "SOFT" "= ${NEUTRE}${BLEU} $SOFT ${NEUTRE}"
    printf "${NOIR2}${GRAS}%-10s %-15s\n" "ROOT_SOFT" "= ${NEUTRE}${BLEU} $ROOT_SOFT ${NEUTRE}"
    printf "${NOIR2}${GRAS}%-10s %-15s\n" "PATH_SOFT" "= ${NEUTRE}${BLEU} $PATH_SOFT ${NEUTRE}"
    echo -e $NOIR2'===================================================================================================='
}