#!/bin/bash

count=0
mkdir -p Vector_Monotop_Cards
rm -rf Vector_Monotop_Cards/*
for Med in 300 500 700 1000 1500 1750 2000 2250 2500
do
    for Mchi in 1 200 490 500 990 1000
    do
        modelName=DMsimp_s_spin1_monotop_${Med}_${Mchi}_800
        dirName=Vector_MonoTop_NLO_Mphi-${Med}_Mchi-${Mchi}_gSM-0p25_gDM-1p0_13TeV-madgraph

        if [ -e MonotopModels/${modelName} ]; then
            #echo ${modelName}
            ((count++))

            mkdir -p Vector_Monotop_Cards/${dirName}

            ## run_card.dat and madspin
            cp monot_cards_jongho/monotop_300_1000_800_run_card.dat Vector_Monotop_Cards/${dirName}/${dirName}_run_card.dat
            cp monot_cards_jongho/monotop_300_1000_800_madspin_card.dat Vector_Monotop_Cards/${dirName}/${dirName}_madspin_card.dat

            ## extramodels.dat
            if [ -e Vector_Monotop_Cards/${dirName}/${dirName}_extramodels.dat ]; then
                rm Vector_Monotop_Cards/${dirName}/${dirName}_extramodels.dat
            fi
            echo "${modelName}.tgz" >> Vector_Monotop_Cards/${dirName}/${dirName}_extramodels.dat

            ## customizecards.dat
            if [ -e Vector_Monotop_Cards/${dirName}/${dirName}_customizecards.dat ]; then
                rm Vector_Monotop_Cards/${dirName}/${dirName}_customizecards.dat
            fi
            cp monot_cards_jongho/monotop_300_1000_800_customizecards.dat Vector_Monotop_Cards/${dirName}/${dirName}_customizecards.dat
            sed -i "16s/.*/set param_card mass 55  "${Med}"/g" Vector_Monotop_Cards/${dirName}/${dirName}_customizecards.dat
            sed -i "17s/.*/set param_card mass 18  "${Mchi}"/g" Vector_Monotop_Cards/${dirName}/${dirName}_customizecards.dat

            ## proc_card.dat
            if [ -e Vector_Monotop_Cards/${dirName}/${dirName}_proc_card.dat ]; then
                rm Vector_Monotop_Cards/${dirName}/${dirName}_proc_card.dat
            fi
            cp monot_cards_jongho/monotop_300_1000_800_proc_card.dat Vector_Monotop_Cards/${dirName}/${dirName}_proc_card.dat
            sed -i "1s/.*/import "${modelName}"/g" Vector_Monotop_Cards/${dirName}/${dirName}_proc_card.dat
            sed -i "4s/.*/output "${dirName}"/g" Vector_Monotop_Cards/${dirName}/${dirName}_proc_card.dat

            ## copy model
            tar -zcf ${modelName}.tgz MonotopModels/${modelName}
            mv ${modelName}.tgz Vector_Monotop_Cards/${dirName}
        fi
    done
done

