#!/bin/bash

Type=${1}

if [ ${Type} = "Vector" ]; then
    vectorCount=0
    mkdir -p MG5_vectorCards
    for Med in 10 100 300 500 750 1000 1500 1750 2000 2250 2500 
    do
        for Mchi in 1 10 40 100 150 200 300 400 500 600 700 
        do
            vectorModel=DMsimp_s_spin1_${Med}_${Mchi}_800
            dirNameW=Vector_MonoW_NLO_Mphi-${Med}_Mchi-${Mchi}_gSM-0p25_gDM-1p0_13TeV-madgraph
            dirNameZ=Vector_MonoZ_NLO_Mphi-${Med}_Mchi-${Mchi}_gSM-0p25_gDM-1p0_13TeV-madgraph
            if [ -e VectorModel/${vectorModel} ]; then
                #echo ${vectorModel}
                ((vectorCount++))
                
                #cd VectorModel
                #tar -zcf ${vectorModel}.tgz ${vectorModel}
                #cd ../
                
                mkdir -p MG5_vectorCards/${dirNameW}

                ## run_card.dat
                cp run_card.dat MG5_vectorCards/${dirNameW}/${dirNameW}_run_card.dat

                ## customizedcards.dat
                if [ -e MG5_vectorCards/${dirNameW}/${dirNameW}_customizecards.dat ]; then
                    rm MG5_vectorCards/${dirNameW}/${dirNameW}_customizecards.dat
                fi
                echo "#put card customizations here (change top and higgs mass for example)" >> MG5_vectorCards/${dirNameW}/${dirNameW}_customizecards.dat
                echo "set param_card mass  55 ${Med}" >> MG5_vectorCards/${dirNameW}/${dirNameW}_customizecards.dat  
                echo "set param_card mass  18 ${Mchi}" >> MG5_vectorCards/${dirNameW}/${dirNameW}_customizecards.dat
                echo "set param_card decay 55 auto" >> MG5_vectorCards/${dirNameW}/${dirNameW}_customizecards.dat

                ## extramodels.dat
                if [ -e MG5_vectorCards/${dirNameW}/${dirNameW}_extramodels.dat ]; then
                    rm MG5_vectorCards/${dirNameW}/${dirNameW}_extramodels.dat
                fi
                echo "${vectorModel}.tgz" >> MG5_vectorCards/${dirNameW}/${dirNameW}_extramodels.dat
               
                ## proc_card.dat
                cp MonoW.dat MG5_vectorCards/${dirNameW}/${dirNameW}_proc_card.dat
                sed -i "1s/.*/import "${vectorModel}"/g" MG5_vectorCards/${dirNameW}/${dirNameW}_proc_card.dat
                sed -i "7s/.*/output "${dirNameW}"/g" MG5_vectorCards/${dirNameW}/${dirNameW}_proc_card.dat

                ## copy models 
                cp VectorModel/${vectorModel}.tgz MG5_vectorCards/${dirNameW}

                mkdir -p MG5_vectorCards/${dirNameZ}
                ## run_card.dat
                cp run_card.dat MG5_vectorCards/${dirNameZ}/${dirNameZ}_run_card.dat

                ## customizedcards.dat
                if [ -e MG5_vectorCards/${dirNameZ}/${dirNameZ}_customizecards.dat ]; then
                    rm MG5_vectorCards/${dirNameZ}/${dirNameZ}_customizecards.dat
                fi
                echo "#put card customizations here (change top and higgs mass for example)" >> MG5_vectorCards/${dirNameZ}/${dirNameZ}_customizecards.dat
                echo "set param_card mass  55 ${Med}" >> MG5_vectorCards/${dirNameZ}/${dirNameZ}_customizecards.dat  
                echo "set param_card mass  18 ${Mchi}" >> MG5_vectorCards/${dirNameZ}/${dirNameZ}_customizecards.dat
                echo "set param_card decay 55 auto" >> MG5_vectorCards/${dirNameZ}/${dirNameZ}_customizecards.dat

                ## extramodels.dat
                if [ -e MG5_vectorCards/${dirNameZ}/${dirNameZ}_extramodels.dat ]; then
                    rm MG5_vectorCards/${dirNameZ}/${dirNameZ}_extramodels.dat
                fi
                echo "${vectorModel}.tgz" >> MG5_vectorCards/${dirNameZ}/${dirNameZ}_extramodels.dat
               
                ## proc_card.dat
                cp MonoZ.dat MG5_vectorCards/${dirNameZ}/${dirNameZ}_proc_card.dat
                sed -i "1s/.*/import "${vectorModel}"/g" MG5_vectorCards/${dirNameZ}/${dirNameZ}_proc_card.dat
                sed -i "5s/.*/output "${dirNameZ}"/g" MG5_vectorCards/${dirNameZ}/${dirNameZ}_proc_card.dat
                
                ## copy models 
                cp VectorModel/${vectorModel}.tgz MG5_vectorCards/${dirNameZ}
            fi
        done
    done
    echo ${vectorCount}
fi


if [ ${Type} = "Axial" ]; then
    axialCount=0
    mkdir -p MG5_axialCards
    for Med in 10 100 300 500 750 1000 1500 1750 2000 2250 2500 
    do
        for Mchi in 1 10 40 100 150 200 300 400 500 600 700 
        do
            axialModel=DMsimp_s_spin1_${Med}_${Mchi}_801
            dirNameW=Axial_MonoW_NLO_Mphi-${Med}_Mchi-${Mchi}_gSM-0p25_gDM-1p0_13TeV-madgraph
            dirNameZ=Axial_MonoZ_NLO_Mphi-${Med}_Mchi-${Mchi}_gSM-0p25_gDM-1p0_13TeV-madgraph
            if [ -e AxialModel/${axialModel} ]; then
                #echo ${axialModel}
                ((axialCount++))
                
                cd AxialModel
                tar -zcf ${axialModel}.tgz ${axialModel}
                cd ../
                
                mkdir -p MG5_axialCards/${dirNameW}

                ## run_card.dat
                cp run_card.dat MG5_axialCards/${dirNameW}/${dirNameW}_run_card.dat

                ## customizedcards.dat
                if [ -e MG5_axialCards/${dirNameW}/${dirNameW}_customizecards.dat ]; then
                    rm MG5_axialCards/${dirNameW}/${dirNameW}_customizecards.dat
                fi
                echo "#put card customizations here (change top and higgs mass for example)" >> MG5_axialCards/${dirNameW}/${dirNameW}_customizecards.dat
                echo "set param_card mass  55 ${Med}" >> MG5_axialCards/${dirNameW}/${dirNameW}_customizecards.dat  
                echo "set param_card mass  18 ${Mchi}" >> MG5_axialCards/${dirNameW}/${dirNameW}_customizecards.dat
                echo "set param_card decay 55 auto" >> MG5_axialCards/${dirNameW}/${dirNameW}_customizecards.dat

                ## extramodels.dat
                if [ -e MG5_axialCards/${dirNameW}/${dirNameW}_extramodels.dat ]; then
                    rm MG5_axialCards/${dirNameW}/${dirNameW}_extramodels.dat
                fi
                echo "${axialModel}.tgz" >> MG5_axialCards/${dirNameW}/${dirNameW}_extramodels.dat
               
                ## proc_card.dat
                cp MonoW.dat MG5_axialCards/${dirNameW}/${dirNameW}_proc_card.dat
                sed -i "1s/.*/import "${axialModel}"/g" MG5_axialCards/${dirNameW}/${dirNameW}_proc_card.dat
                sed -i "7s/.*/output "${dirNameW}"/g" MG5_axialCards/${dirNameW}/${dirNameW}_proc_card.dat

                ## copy models 
                cp AxialModel/${axialModel}.tgz MG5_axialCards/${dirNameW}

                mkdir -p MG5_axialCards/${dirNameZ}
                ## run_card.dat
                cp run_card.dat MG5_axialCards/${dirNameZ}/${dirNameZ}_run_card.dat

                ## customizedcards.dat
                if [ -e MG5_axialCards/${dirNameZ}/${dirNameZ}_customizecards.dat ]; then
                    rm MG5_axialCards/${dirNameZ}/${dirNameZ}_customizecards.dat
                fi
                echo "#put card customizations here (change top and higgs mass for example)" >> MG5_axialCards/${dirNameZ}/${dirNameZ}_customizecards.dat
                echo "set param_card mass  55 ${Med}" >> MG5_axialCards/${dirNameZ}/${dirNameZ}_customizecards.dat  
                echo "set param_card mass  18 ${Mchi}" >> MG5_axialCards/${dirNameZ}/${dirNameZ}_customizecards.dat
                echo "set param_card decay 55 auto" >> MG5_axialCards/${dirNameZ}/${dirNameZ}_customizecards.dat

                ## extramodels.dat
                if [ -e MG5_axialCards/${dirNameZ}/${dirNameZ}_extramodels.dat ]; then
                    rm MG5_axialCards/${dirNameZ}/${dirNameZ}_extramodels.dat
                fi
                echo "${axialModel}.tgz" >> MG5_axialCards/${dirNameZ}/${dirNameZ}_extramodels.dat
               
                ## proc_card.dat
                cp MonoZ.dat MG5_axialCards/${dirNameZ}/${dirNameZ}_proc_card.dat
                sed -i "1s/.*/import "${axialModel}"/g" MG5_axialCards/${dirNameZ}/${dirNameZ}_proc_card.dat
                sed -i "5s/.*/output "${dirNameZ}"/g" MG5_axialCards/${dirNameZ}/${dirNameZ}_proc_card.dat
                
                ## copy models 
                cp AxialModel/${axialModel}.tgz MG5_axialCards/${dirNameZ}
            fi
        done
    done
    echo ${axialCount}
fi

if [ ${Type} = "Scalar" ]; then
    scalarCount=0
    mkdir -p MG5_scalarCards
    for Med in 10 20 50 100 200 300 350 400 500 750 1000 
    do
        for Mchi in 0 1 10 40 50 100 200 350 450  
        do
            scalarModel=DMsimp_s_spin0_${Med}_${Mchi}_805
            dirNameZ=Scalar_MonoZ_NLO_Mphi-${Med}_Mchi-${Mchi}_gSM-0p25_gDM-1p0_13TeV-madgraph
            if [ -e ScalarModel/${scalarModel} ]; then
                #echo ${scalarModel}
                ((scalarCount++))
                mkdir -p MG5_scalarCards/${dirNameZ}
                
                cd ScalarModel
                tar -zcf ${scalarModel}.tgz ${scalarModel}
                cd ../
                
                ## run_card.dat
                cp run_card.dat MG5_scalarCards/${dirNameZ}/${dirNameZ}_run_card.dat

                ## customizedcards.dat
                if [ -e MG5_scalarCards/${dirNameZ}/${dirNameZ}_customizecards.dat ]; then
                    rm MG5_scalarCards/${dirNameZ}/${dirNameZ}_customizecards.dat
                fi
                echo "#put card customizations here (change top and higgs mass for example)" >> MG5_scalarCards/${dirNameZ}/${dirNameZ}_customizecards.dat
                echo "set param_card mass  55 ${Med}" >> MG5_scalarCards/${dirNameZ}/${dirNameZ}_customizecards.dat  
                echo "set param_card mass  18 ${Mchi}" >> MG5_scalarCards/${dirNameZ}/${dirNameZ}_customizecards.dat
                echo "set param_card decay 55 auto" >> MG5_scalarCards/${dirNameZ}/${dirNameZ}_customizecards.dat

                ## extramodels.dat
                if [ -e MG5_scalarCards/${dirNameZ}/${dirNameZ}_extramodels.dat ]; then
                    rm MG5_scalarCards/${dirNameZ}/${dirNameZ}_extramodels.dat
                fi
                echo "${scalarModel}.tgz" >> MG5_scalarCards/${dirNameZ}/${dirNameZ}_extramodels.dat
               
                ## proc_card.dat
                cp MonoZ.dat MG5_scalarCards/${dirNameZ}/${dirNameZ}_proc_card.dat
                sed -i "1s/.*/import "${scalarModel}"/g" MG5_scalarCards/${dirNameZ}/${dirNameZ}_proc_card.dat
                sed -i "5s/.*/output "${dirNameZ}"/g" MG5_scalarCards/${dirNameZ}/${dirNameZ}_proc_card.dat
                
                ## copy models 
                cp ScalarModel/${scalarModel}.tgz MG5_scalarCards/${dirNameZ}
            fi
        done
    done
    echo ${scalarCount}
fi

if [ ${Type} = "Pseudo" ]; then
    pseudoCount=0
    mkdir -p MG5_pseudoCards
    for Med in 10 20 50 100 200 300 350 400 500 750 1000 
    do
        for Mchi in 0 1 10 40 50 100 200 350 450  
        do
            pseudoModel=DMsimp_s_spin0_${Med}_${Mchi}_806
            dirNameZ=Pseudo_MonoZ_NLO_Mphi-${Med}_Mchi-${Mchi}_gSM-0p25_gDM-1p0_13TeV-madgraph
            if [ -e PseudoModel/${pseudoModel} ]; then
                #echo ${pseudoModel}
                ((pseudoCount++))
                mkdir -p MG5_pseudoCards/${dirNameZ}
                
                cd PseudoModel
                tar -zcf ${pseudoModel}.tgz ${pseudoModel}
                cd ../
                
                ## run_card.dat
                cp run_card.dat MG5_pseudoCards/${dirNameZ}/${dirNameZ}_run_card.dat

                ## customizedcards.dat
                if [ -e MG5_pseudoCards/${dirNameZ}/${dirNameZ}_customizecards.dat ]; then
                    rm MG5_pseudoCards/${dirNameZ}/${dirNameZ}_customizecards.dat
                fi
                echo "#put card customizations here (change top and higgs mass for example)" >> MG5_pseudoCards/${dirNameZ}/${dirNameZ}_customizecards.dat
                echo "set param_card mass  55 ${Med}" >> MG5_pseudoCards/${dirNameZ}/${dirNameZ}_customizecards.dat  
                echo "set param_card mass  18 ${Mchi}" >> MG5_pseudoCards/${dirNameZ}/${dirNameZ}_customizecards.dat
                echo "set param_card decay 55 auto" >> MG5_pseudoCards/${dirNameZ}/${dirNameZ}_customizecards.dat

                ## extramodels.dat
                if [ -e MG5_pseudoCards/${dirNameZ}/${dirNameZ}_extramodels.dat ]; then
                    rm MG5_pseudoCards/${dirNameZ}/${dirNameZ}_extramodels.dat
                fi
                echo "${pseudoModel}.tgz" >> MG5_pseudoCards/${dirNameZ}/${dirNameZ}_extramodels.dat
               
                ## proc_card.dat
                cp MonoZ.dat MG5_pseudoCards/${dirNameZ}/${dirNameZ}_proc_card.dat
                sed -i "1s/.*/import "${pseudoModel}"/g" MG5_pseudoCards/${dirNameZ}/${dirNameZ}_proc_card.dat
                sed -i "5s/.*/output "${dirNameZ}"/g" MG5_pseudoCards/${dirNameZ}/${dirNameZ}_proc_card.dat
                
                ## copy models 
                cp PseudoModel/${pseudoModel}.tgz MG5_pseudoCards/${dirNameZ}
            fi
        done
    done
    echo ${pseudoCount}
fi
