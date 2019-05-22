#!/bin/bash

echo "`pwd`"

modelPath=${HOME}/Physics/LPC-DM/Signal_cards/models/tgzfiles

for Med in 195 200 295 300 495 500 995 1000 1995 2000 2495 2500 2995 3000
do
    for Mchi in 100 150 250 500 750 1000 1250 1500  
    do
        targetDirHs1=DarkHiggs_MonoHs_LO_MZprime-${Med}_Mhs-50_Mchi-${Mchi}_gSM-0p25_gDM-1p0_th-0p01_13TeV-madgraph
        targetDirHs2=DarkHiggs_MonoHs_LO_MZprime-${Med}_Mhs-70_Mchi-${Mchi}_gSM-0p25_gDM-1p0_th-0p01_13TeV-madgraph
        targetDirHs3=DarkHiggs_MonoHs_LO_MZprime-${Med}_Mhs-90_Mchi-${Mchi}_gSM-0p25_gDM-1p0_th-0p01_13TeV-madgraph
        targetDir1=DarkHiggs_MonoJet_LO_MZprime-${Med}_Mchi-${Mchi}_gSM-0p25_gDM-1p0_th-0p01_13TeV-madgraph
        targetDir2=DarkHiggs_MonoW_LO_MZprime-${Med}_Mchi-${Mchi}_gSM-0p25_gDM-1p0_th-0p01_13TeV-madgraph
        targetDir3=DarkHiggs_MonoZ_LO_MZprime-${Med}_Mchi-${Mchi}_gSM-0p25_gDM-1p0_th-0p01_13TeV-madgraph
        modelName1=ZpHiggs_UFO_${Med}_50_${Mchi}_700
        modelName2=ZpHiggs_UFO_${Med}_70_${Mchi}_700
        modelName3=ZpHiggs_UFO_${Med}_90_${Mchi}_700

        echo "Mono Dark Higgs with mass 50 GeV start!"
        if [ -e MonoDarkHiggs/mHs50/${targetDirHs1} ]; then
            rm MonoDarkHiggs/mHs50/${targetDirHs1}/${targetDirHs1}_madconfig
            cp run_card.dat MonoDarkHiggs/mHs50/${targetDirHs1}/${targetDirHs1}_run_card.dat
            cp ${modelPath}/${modelName1}.tgz MonoDarkHiggs/mHs50/${targetDirHs1}/
            #echo "Direcotry exists!"
            if [ -e MonoDarkHiggs/mHs50/${targetDirHs1}/${targetDirHs1}_proc_card.dat ]; then
                cd MonoDarkHiggs/mHs50/${targetDirHs1}
                sed -i "1s/.*/import model "${modelName1}"/g" ${targetDirHs1}_proc_card.dat
                sed -i "5s/.*/output "${targetDirHs1}"/g" ${targetDirHs1}_proc_card.dat
                
                if [ -e ${targetDirHs1}_extramodels.dat ]; then
                    rm ${targetDirHs1}_extramodels.dat
                    echo ${modelName1}.tgz >> ${targetDirHs1}_extramodels.dat
                else
                    echo ${modelName1}.tgz >> ${targetDirHs1}_extramodels.dat
                fi
                
                cd -
            fi
        fi
        echo ""

        echo "Mono Dark Higgs with mass 70 GeV start!"
        if [ -e MonoDarkHiggs/mHs70/${targetDirHs2} ]; then
            rm MonoDarkHiggs/mHs70/${targetDirHs2}/${targetDirHs2}_madconfig
            cp run_card.dat MonoDarkHiggs/mHs70/${targetDirHs2}/${targetDirHs2}_run_card.dat
            cp ${modelPath}/${modelName2}.tgz MonoDarkHiggs/mHs70/${targetDirHs2}/
            #echo "Direcotry exists!"
            if [ -e MonoDarkHiggs/mHs70/${targetDirHs2}/${targetDirHs2}_proc_card.dat ]; then
                cd MonoDarkHiggs/mHs70/${targetDirHs2}
                sed -i "1s/.*/import model "${modelName2}"/g" ${targetDirHs2}_proc_card.dat
                sed -i "5s/.*/output "${targetDirHs2}"/g" ${targetDirHs2}_proc_card.dat
                
                if [ -e ${targetDirHs2}_extramodels.dat ]; then
                    rm ${targetDirHs2}_extramodels.dat
                    echo ${modelName2}.tgz >> ${targetDirHs2}_extramodels.dat
                else
                    echo ${modelName2}.tgz >> ${targetDirHs2}_extramodels.dat
                fi

                cd -
                #echo "  card exists!"
            fi
        fi
        echo ""

        echo "Mono Dark Higgs with mass 90 GeV start!"
        if [ -e MonoDarkHiggs/mHs90/${targetDirHs3} ]; then
            rm MonoDarkHiggs/mHs90/${targetDirHs3}/${targetDirHs3}_madconfig
            cp run_card.dat MonoDarkHiggs/mHs90/${targetDirHs3}/${targetDirHs3}/${targetDirHs3}_run_card.dat
            cp ${modelPath}/${modelName3}.tgz MonoDarkHiggs/mHs90/${targetDirHs3}/
            #echo "Direcotry exists!"
            if [ -e MonoDarkHiggs/mHs90/${targetDirHs3}/${targetDirHs3}_proc_card.dat ]; then
                cd MonoDarkHiggs/mHs90/${targetDirHs3} 
                sed -i "1s/.*/import model "${modelName3}"/g" ${targetDirHs3}_proc_card.dat
                sed -i "5s/.*/output "${targetDirHs3}"/g" ${targetDirHs3}_proc_card.dat
                
                if [ -e ${targetDirHs3}_extramodels.dat ]; then
                    rm ${targetDirHs3}_extramodels.dat
                    echo ${modelName3}.tgz >> ${targetDirHs3}_extramodels.dat
                else
                    echo ${modelName3}.tgz >> ${targetDirHs3}_extramodels.dat
                fi
                
                cd -
                #echo "  card exists!"
            fi
        fi
        echo ""

        echo "Mono jet start!"
        if [ -e Monojet/${targetDir1} ]; then
            rm Monojet/${targetDir1}/${targetDir1}_madconfig
            cp run_card.dat Monojet/${targetDir1}/${targetDir1}_run_card.dat
            cp ${modelPath}/${modelName2}.tgz Monojet/${targetDir1}/
            #echo "Direcotry exists!"
            if [ -e Monojet/${targetDir1}/${targetDir1}_proc_card.dat ]; then
                cd Monojet/${targetDir1}
                sed -i "1s/.*/import model "${modelName2}"/g" ${targetDir1}_proc_card.dat
                sed -i "5s/.*/output "${targetDir1}"/g" ${targetDir1}_proc_card.dat
                
                if [ -e ${targetDir1}_extramodels.dat ]; then
                    rm ${targetDir1}_extramodels.dat
                    echo ${modelName2}.tgz >> ${targetDir1}_extramodels.dat
                else
                    echo ${modelName2}.tgz >> ${targetDir1}_extramodels.dat
                fi
                
                cd -
                #echo "  card exists!"
            fi
        fi
        echo ""

        echo "Mono W start!"
        if [ -e MonoWMatch/${targetDir2} ]; then
            rm MonoWMatch/${targetDir2}/${targetDir2}_madconfig
            cp run_card.dat MonoWMatch/${targetDir2}/${targetDir2}_run_card.dat
            cp ${modelPath}/${modelName2}.tgz MonoWMatch/${targetDir2}/
            #echo "Direcotry exists!"
            if [ -e MonoWMatch/${targetDir2}/${targetDir2}_proc_card.dat ]; then
                cd MonoWMatch/${targetDir2}
                sed -i "1s/.*/import model "${modelName2}"/g" ${targetDir2}_proc_card.dat
                sed -i "7s/.*/output "${targetDir2}"/g" ${targetDir2}_proc_card.dat
                
                if [ -e ${targetDir2}_extramodels.dat ]; then
                    rm ${targetDir2}_extramodels.dat
                    echo ${modelName2}.tgz >> ${targetDir2}_extramodels.dat
                else
                    echo ${modelName2}.tgz >> ${targetDir2}_extramodels.dat
                fi
                
                cd -
                #echo "  card exists!"
            fi
        fi
        echo ""

        echo "Mono Z start!"
        if [ -e MonoZMatch/${targetDir3} ]; then
            rm MonoZMatch/${targetDir3}/${targetDir3}_madconfig
            cp run_card.dat MonoZMatch/${targetDir3}/${targetDir3}_run_card.dat
            cp ${modelPath}/${modelName2}.tgz MonoZMatch/${targetDir3}/
            #echo "Direcotry exists!"
            if [ -e MonoZMatch/${targetDir3}/${targetDir3}_proc_card.dat ]; then
                cd MonoZMatch/${targetDir3}
                sed -i "1s/.*/import model "${modelName2}"/g" ${targetDir3}_proc_card.dat
                sed -i "5s/.*/output "${targetDir3}"/g" ${targetDir3}_proc_card.dat
                
                if [ -e ${targetDir3}_extramodels.dat ]; then
                    rm ${targetDir3}_extramodels.dat
                    echo ${modelName2}.tgz >> ${targetDir3}_extramodels.dat
                else
                    echo ${modelName2}.tgz >> ${targetDir3}_extramodels.dat
                fi
                
                cd -
                #echo "  card exists!"
            fi
        fi
        echo ""

    done
done
