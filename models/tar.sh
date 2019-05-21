#!/bin/bash

for Med in 195 200 295 300 495 500 995 1000 1995 2000 2495 2500 2995 3000
do
    for Mchi in 100 150 250 500 750 1000 1250 1500
    do
        modelName1=ZpHiggs_UFO_${Med}_50_${Mchi}_700
        modelName2=ZpHiggs_UFO_${Med}_70_${Mchi}_700
        modelName3=ZpHiggs_UFO_${Med}_90_${Mchi}_700
        
        if [ -e ${modelName1} ]; then
            tar czvf ${modelName1}.tgz ${modelName1}/
        fi
        
        if [ -e ${modelName2} ]; then
            tar czvf ${modelName2}.tgz ${modelName2}/
        fi
        
        if [ -e ${modelName3} ]; then
            tar czvf ${modelName3}.tgz ${modelName3}/
        fi

    done
done
