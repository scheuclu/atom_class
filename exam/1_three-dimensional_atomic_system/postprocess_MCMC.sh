readarray -t dampvals < ./scriptinput/dampvals

for dampval in ${dampvals[@]};do
  for quantity in PotEng Press Temp KinEng TotEng; do

    ${LOG2TXT} logfiles/NVT_gcmc_damp${dampval}.txt\
               ./results/MCMC/${quantity}_damp${dampval}_cellnum5\
               Step ${quantity}

    ${LOG2TXT} logfiles/log.NVT_damp${dampval}_cellnum5\
                 ./results/NVTstep/${quantity}_damp${dampval}_cellnum5\
                 Step ${quantity}

    ../../plotsimple.py ./results/MCMC/${quantity}_damp${dampval}_cellnum5\
                        ./plots/MCMC/simple_${quantity}_damp${dampval}\
                        Step ${quantity}\
                        ${quantity}_over_Stepnum
  done
done



