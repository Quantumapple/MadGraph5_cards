#!/bin/bash

#targetPath=/home/jongho/Physics/LPC-DM/Signal_cards/year2017and2018/MonoDarkHiggs/
#targetPath=/home/jongho/Physics/LPC-DM/Signal_cards/year2017and2018/Monojet/
#targetPath=/home/jongho/Physics/LPC-DM/Signal_cards/year2017and2018/MonoWMatch/
targetPath=/home/jongho/Physics/LPC-DM/Signal_cards/year2017and2018/MonoZMatch/
DarkHiggsMass=mHs90
count=0

for Med in 195 200 295 300 495 500 995 1000 1995 2000 2495 2500 2995 3000
do
    for Mchi in 100 150 250 500 750 1000 1250 1500  
    do
        filename=ZpHiggs_UFO_$Med\_70_$Mchi\_700.tgz
        #targetDir=DarkHiggs_MonoHs_LO_MZprime-$Med\_Mhs-90_Mchi-$Mchi\_gSM-0p25_gDM-1p0_th-0p01_13TeV-madgraph
        #targetDir=DarkHiggs_MonoJet_LO_MZprime-$Med\_Mchi-$Mchi\_gSM-0p25_gDM-1p0_th-0p01_13TeV-madgraph
        #targetDir=DarkHiggs_MonoW_LO_MZprime-$Med\_Mchi-$Mchi\_gSM-0p25_gDM-1p0_th-0p01_13TeV-madgraph
        targetDir=DarkHiggs_MonoZ_LO_MZprime-$Med\_Mchi-$Mchi\_gSM-0p25_gDM-1p0_th-0p01_13TeV-madgraph
        if [ -e $filename ]; then
            #echo "The file $filename exists!"
            #cp $filename $targetPath/$DarkHiggsMass/$targetDir ## Mono-Dark Higgs
            cp $filename $targetPath/$targetDir ## Mono-jet, Mono-V
            #echo "cp $filename $targetPath/$targetDir"
            (( count++ ))
        fi
    done
done

echo "Copy $count times!"
