#!/bin/bash

echo "`pwd`"

for Med in 195 200 295 300 495 500 995 1000 1995 2000 2495 2500 2995 3000
do
    for Mchi in 100 150 250 500 750 1000 1250 1500  
    do
        targetDir=DarkHiggs_MonoHs_LO_MZprime-$Med\_Mhs-50_Mchi-$Mchi\_gSM-0p25_gDM-1p0_th-0p01_13TeV-madgraph
        if [ -e $targetDir ]; then
            #echo "The file $targetDir exists!"
            cd $targetDir
            pwd | cut -d"/" -f10
            if [ -e ${targetDir}_extramodels.dat ]; then
                echo "Extramodels.dat exists!"
            else
                echo ZpHiggs_UFO_${Med}_50_${Mchi}_700.tgz >> ${targetDir}_extramodels.dat
            fi
            cd ../
        fi
    done
done

