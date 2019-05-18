#!/bin/bash

for Med in 195 200 295 300 495 500 995 1000 1995 2000 2495 2500 2995 3000
do
    for Mchi in 100 150 250 500 750 1000 1250 1500  
    do
        targetDir=DarkHiggs_MonoHs_LO_MZprime-$Med\_Mhs-50_Mchi-$Mchi\_gSM-0p25_gDM-1p0_th-0p01_13TeV-madgraph
        if [ -e $targetDir ]; then
            cp run_card.dat ${targetDir}/${targetDir}_run_card.dat
        fi
    done
done

