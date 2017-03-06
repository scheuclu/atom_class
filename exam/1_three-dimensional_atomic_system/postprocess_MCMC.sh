readarray -t dampvals < ./scriptinput/dampvals

for dampval in ${dampvals[@]};do
  for quantity in PotEng Press Temp KinEng TotEng; do

    ${LOG2TXT} logfiles/NVT_gcmc_damp${dampval}.txt\
               ./results/MCMC/${quantity}_damp${dampval}_cellnum5\
               Time ${quantity}

    ../../plotsimple.py ./results/MCMC/${quantity}_damp${dampval}_cellnum5\
                        ./plots/MCMC/simple_${quantity}_damp${dampval}\
                        Time ${quantity}\
                        ${quantity}_over_Time
  done
done



