#!/bin/bash

echo "`pwd`"

for Med in 195 200 295 300 495 500 995 1000 1995 2000 2495 2500 2995 3000
do
    for Mchi in 100 150 250 500 750 1000 1250 1500  
    do
        #targetDir=DarkHiggs_MonoHs_LO_MZprime-$Med\_Mhs-90_Mchi-$Mchi\_gSM-0p25_gDM-1p0_th-0p01_13TeV-madgraph
        #targetDir=DarkHiggs_MonoJet_LO_MZprime-${Med}_Mchi-${Mchi}_gSM-0p25_gDM-1p0_th-0p01_13TeV-madgraph
        #targetDir=DarkHiggs_MonoW_LO_MZprime-${Med}_Mchi-${Mchi}_gSM-0p25_gDM-1p0_th-0p01_13TeV-madgraph
        targetDir=DarkHiggs_MonoZ_LO_MZprime-${Med}_Mchi-${Mchi}_gSM-0p25_gDM-1p0_th-0p01_13TeV-madgraph
        modelName=ZpHiggs_UFO_${Med}_70_${Mchi}_700
        if [ -e $targetDir ]; then
            cp run_card.dat ${targetDir}/${targetDir}_run_card.dat
            cp /home/jongho/Physics/LPC-DM/Signal_cards/DarkHiggs_models/${modelName}.tgz ${targetDir}/
            
            cd $targetDir
            
            pwd | cut -d"/" -f9 # Mono-jet, V
            #pwd | cut -d"/" -f10 ## Mono-Dark Higgs
            
            if [ -e ${targetDir}_extramodels.dat ]; then
                echo "Extramodels.dat exists!"
            else
                echo ZpHiggs_UFO_${Med}_70_${Mchi}_700.tgz >> ${targetDir}_extramodels.dat
            fi
            
            if [ -e ${targetDir}_proc_card.dat ]; then
                #sed -i "1s/import/import model/g" ${targetDir}_proc_card.dat
                #sed -i "1s/.*/import model "${modelName}"/g" ${targetDir}_proc_card.dat
                #sed -i "5s/.*/output "${targetDir}"/g" ${targetDir}_proc_card.dat
                #sed -i "5s/.*/add process    p p > zp w- , zp > dm dm , w- > j j/g" ${targetDir}_proc_card.dat
                #sed -i "7s/.*/output "${targetDir}"/g" ${targetDir}_proc_card.dat
                echo "Nothing to change!"
            fi
            
            cd ../
        fi
    done
done
