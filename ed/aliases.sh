#!/usr/bin/env bash
#!/bin/bash

export EDITOR='gedit'


# NOEL
# ----------------------------------------------------------------

alias secret="python $BIN/python/noel_01_secret.py"
alias pirate="python $BIN/python/noel_02_pirate.py"
alias bateau="python $BIN/python/noel_03_bateau.py"

alias cine="python $BIN/python/cineteque.py"


# CINE
# ----------------------------------------------------------------

alias acti="cd /Volumes/CINEMA_01/01_ACTION;cl;l"
alias aven="cd /Volumes/CINEMA_01/02_AVENTURE;cl;l"
alias poli="cd /Volumes/CINEMA_01/03_POLICIER;cl;l"
alias thri="cd /Volumes/CINEMA_01/04_THRILLER;cl;l"
alias espi="cd /Volumes/CINEMA_01/05_ESPIONNAGE;cl;l"
alias come="cd /Volumes/CINEMA_01/06_COMEDIE;cl;l"
alias dram="cd /Volumes/CINEMA_01/07_DRAME;cl;l"
alias cata="cd /Volumes/CINEMA_01/08_CATASTROPHE;cl;l"
alias fant="cd /Volumes/CINEMA_01/09_FANTASTIQUE;cl;l"
alias scie="cd /Volumes/CINEMA_01/10_SCIENCE_FICTION;cl;l"
alias comi="cd /Volumes/CINEMA_01/11_COMICS;cl;l"
alias west="cd /Volumes/CINEMA_01/12_WESTERN;cl;l"
alias guer="cd /Volumes/CINEMA_01/13_GUERRE;cl;l"
alias hist="cd /Volumes/CINEMA_01/14_HISTORIQUE;cl;l"
alias pepl="cd /Volumes/CINEMA_01/15_PEPLUM;cl;l"
alias horr="cd /Volumes/CINEMA_01/16_HORREUR;cl;l"

alias an2d="cd /Volumes/CINEMA_02/18_ANIMATION_2D;cl;l"
alias an3d="cd /Volumes/CINEMA_02/18_ANIMATION_3D;cl;l"

# SET
# ----------------------------------------------------------------

alias t="run type"
alias p="run proj"
alias f="run fold"

alias r="run"

alias rt="type_remove"

alias z="python $BIN/python/test.py"
alias z2="python $BIN/python/test2.py"

alias g="pyside6-uic $BIN/python/interface/ui/main_window.ui -o $BIN/python/interface/ui/main_window.py; python $BIN/python/gui.py"


# CANA
# ----------------------------------------------------------------

alias bin="cd $BIN; clear; ls -lah"

alias binenv=". $BIN/venv/bin/activate"

alias i="export AUTORUN=0; init"
alias i1="init 1"

alias kp="killpipe"


# SOFTS
# ----------------------------------------------------------------

if [[ $SYSTEM == "linux" ]]; then
    alias sublime="/usr/bin/subl"
    alias sub=sublime

    alias rv="/mnt/c/'Program Files'/DJV2/bin/djv.com"
fi

alias style="sublime /home/fabrice/Dropbox/PIPELINE/bin/cana_1.0/python/interface/styles/test.css &"
alias des="pyside6-designer &"


# SYSTEME
# ----------------------------------------------------------------

alias ed="$EDITOR '$BIN/ed/aliases.sh'"
alias ed2="$EDITOR '$BIN/ed/$SYSTEM/softs_$SYSTEM'"
alias eds="source $BIN/ed/aliases.sh;source $BIN/ed/$SYSTEM/softs_$SYSTEM"

alias ls="ls --color=auto"

alias l="ls -lAvh"
alias ll="ls -lAvh"
alias lll="ls -lAvh"
alias cl="clear"
alias cll="clear; l"

alias brc="$EDITOR ~/.bashrc"

alias sh1='sudo shutdown -h +60'
alias sh2='sudo shutdown -h +120'
alias sh3='sudo shutdown -h +180'
alias sh4='sudo shutdown -h +240'

alias s0="sudo shutdown -h +9000000; echo''; echo $'Redémarrage annulé'; echo''"

if [[ $SYSTEM == "linux" ]]; then
    alias 4k="xrandr -s 3840x2160"
    alias 2k="xrandr -s 2560x1440"
    alias hd="xrandr -s 1920x1080"

    alias su="sudo su"

    alias nn="nautilus ."

    alias smb="$EDITOR /etc/samba/smb.conf"
    alias fst="$EDITOR /etc/fstab"

    alias ram="free -h && sysctl vm.drop_caches=3 && free -h"

elif [[ $SYSTEM == "windows" ]]; then
    alias shtd="$ROOT_C/WINDOWS/system32/shutdown.exe -s"

elif [[ $SYSTEM == "mac" ]]; then
    pass

fi

# DEPLACEMENT
# ----------------------------------------------------------------

alias ci1="cd /media/partage/CINEMA_01"
alias ci2="cd /media/partage/CINEMA_02"
alias tmp="cd /media/partage/TEMP"
alias dow="cd /media/partage/DOWNLOADS"
alias pipe="cd /media/partage/PIPELINE"
alias med="cd /media/partage/MEDIA"
alias sto="cd /media/partage/STORAGE"
alias tut="cd /media/partage/PIPELINE/ref/_TUTOS"

alias font="cd $PATH_FONTS; clear; ls -la"
alias icon="cd $PATH_ICONES; clear; ls -la"

alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias .....="cd ../../../.."
alias ......="cd ../../../../.."
alias .......="cd ../../../../../.."
alias ........="cd ../../../../../../.."
alias .........="cd ../../../../../../../.."
alias ..........="cd ../../../../../../../../.."
alias ...........="cd ../../../../../../../../../.."

# DIVERS
# ----------------------------------------------------------------

alias note="$EDITOR ~/notes/notes.txt"
alias lnk="$EDITOR ~/Desktop/'A garder'/.link"


# SSH
# ----------------------------------------------------------------

alias ser="sudo ssh fabrice@192.168.0.180"
alias ttttt="sudo ssh fabrice@192.168.0.180 sudo su -S"


# GIT
# ----------------------------------------------------------------

alias gitp="git push -u origin master"


# A TESTER
# ----------------------------------------------------------------

alias shut="sudo shutdown -h now"
alias pycin="python $BIN/../prog/cineteque/main2.py"
