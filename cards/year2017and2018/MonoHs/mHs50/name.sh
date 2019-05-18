#!/bin/bash

name=$(pwd | cut -d"/" -f9)
echo "What is the name? $name"

if [ -e DM_proc_card.dat ]; then
    mv DM_proc_card.dat $name\_proc_card.dat
fi

if [ -e run_card.dat ]; then
    mv run_card.dat $name\_run_card.dat
fi

if [ -e customizecards.dat ]; then
    mv customizecards.dat $name\_customizecards.dat
fi

if [ -e setcuts.f ]; then
    mv setcuts.f $name\_setcuts.f
fi

if [ -e madconfig ]; then
    mv madconfig $name\_madconfig
fi
