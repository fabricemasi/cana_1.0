#! /bin/bash

ps1 ()
{
	if [[ $TYPE == "" ]] && [[ $PROJET == "" ]] && [[ $FOLDER == "" ]] && [[ $SOFT == "" ]]; then
		cl1=$VERT2
		cl2=$BLEU2
		cl3=$BLANC
		cl4=$GRIS
		PS1="\[\e]0;\w\a\]\n\[${cl1}\]\u@\h${cl3}:\[${cl2}\]\w\[\e[0m\]\n\$"
	else
		cl1=$BLEU2
		cl2=$CYAN	# projet et shot
		cl3=$BLANC	# discipline
		cl4=$CYAN		# adresse
        cl5=$JAUNE2 # soft
        cl6=$ROUGE   	# cache
        cl7=$VERT
        cl8=$JAUNE
        cl9=$GRIS
        cl10=$VERT2
        cl11=$GRIS2
    fi
    if [[ -e $PATH_CACHE ]] && [[ -e $PATH_RENDER ]]; then
      PS1="\n${cl7}\u@\h $cl1[${cl2}${TYPE}${cl1}]-[${cl8}${PROJET}${cl1}]-[${cl8}${FOLDER}${cl1}]${cl7}-[${cl9}${SOFT}${cl9}]-${cl6}cache${cl1}-${cl6}render${cl1} ${cl4}\n\w ${cl1}> ${NEUTRE}"

    elif ! [[ -e $PATH_CACHE ]] && [[ -e $PATH_RENDER ]]; then
      PS1="\n${cl7}\u@\h $cl1[${cl2}${TYPE}${cl1}]-[${cl8}${PROJET}${cl1}]-[${cl8}${FOLDER}${cl1}]${cl7}-[${cl9}${SOFT}${cl9}]-${cl6}render${cl1} ${cl4}\n\w ${cl1}> ${NEUTRE}"

    elif [[ -e $PATH_CACHE ]] && ! [[ -e $PATH_RENDER ]]; then
      PS1="\n${cl7}\u@\h $cl1[${cl2}${TYPE}${cl1}]-[${cl8}${PROJET}${cl1}]-[${cl8}${FOLDER}${cl1}]${cl7}-[${cl9}${SOFT}${cl9}]-${cl6}cache${cl1} ${cl4}\n\w ${cl1}> ${NEUTRE}"

    else
      PS1="\n${cl7}\u@\h $cl1[${cl1}${TYPE}${cl1}]-[${cl8}${PROJET}${cl1}]-[${cl8}${FOLDER}${cl1}]${cl1} ${cl1}${SOFT}${cl1} ${cl4}\n\w ${cl1}> ${NEUTRE}"
    fi
}



#    if [[ -e $PATH_CACHE ]] && [[ -e $PATH_RENDER ]]; then
#      PS1="\n${cl7}\u@\h $cl1[${cl2}${PROJ}${cl1}]-[${cl2}${TYPE}${cl1}]-[${cl8}${NAME}${cl1}]-[${cl3}${DISC}${cl1}]-[${cl5}${SOFT}${cl1}]-${cl6}cache${cl1}-${cl6}render${cl1} ${cl4}\n\w ${cl1}> ${NEUTRE}"
#
#    elif ! [[ -e $PATH_CACHE ]] && [[ -e $PATH_RENDER ]]; then
#      PS1="\n${cl7}\u@\h $cl1[${cl2}${PROJ}${cl1}]-[${cl2}${TYPE}${cl1}]-[${cl8}${NAME}${cl1}]-[${cl3}${DISC}${cl1}]-[${cl5}${SOFT}${cl1}]-${cl6}render${cl1} ${cl4}\n\w ${cl1}> ${NEUTRE}"
#
#    elif [[ -e $PATH_CACHE ]] && ! [[ -e $PATH_RENDER ]]; then
#      PS1="\n${cl7}\u@\h $cl1[${cl2}${PROJ}${cl1}]-[${cl2}${TYPE}${cl1}]-[${cl8}${NAME}${cl1}]-[${cl3}${DISC}${cl1}]-[${cl5}${SOFT}${cl1}]-${cl6}cache${cl1} ${cl4}\n\w ${cl1}> ${NEUTRE}"
#
#    else
#      PS1="\n${cl7}\u@\h $cl1[${cl2}${PROJ}${cl1}]-[${cl2}${TYPE}${cl1}]-[${cl8}${NAME}${cl1}]-[${cl3}${DISC}${cl1}]-[${cl5}${SOFT}${cl1}] ${cl4}\n\w ${cl1}> ${NEUTRE}"
#    fi
