#! /bin/bash

debug "${BASH_SOURCE[0]}" in

go ()		# 2 arg : $path, $extension
{
    path=$path									    # path du repertoire de travail
    extension=$extension							# extension des fichiers

    condition=false
    xx=false

    cd $ROOT_FOLDER/02_work

        if ! [[ -e $path ]]; then
            echo -e ${COLOR4}${GRAS}
            read -p "Le repertoire de travail pour $SOFT n'existe pas, voulez-vous le creer? " reponse
            echo -e ${NEUTRE}""
            if [[ $reponse == "o" ]];then
                mkdir $path
                echo "path : " $path

                if [[ $extension != "" ]]; then
                    touch $path/$NAME'.v001.'$extension
                fi
                condition=true
            elif [[ $reponse == "n" ]];then
                echo "Repertoire non creer."
            else
                echo "Aborted."
            fi
        else
            condition=true
        fi

    # RESULTAT :

    if [[ $condition == true ]]; then

        export CACHE=$ROOT_TEMP/CACHE/$NAME/$SOFT
        export RENDER=$ROOT_TEMP/RENDER/$NAME/$SOFT

        cd $path
        eval ll
        ps1

    fi
}

debug "${BASH_SOURCE[0]}" out