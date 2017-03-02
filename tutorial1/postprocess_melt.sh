readarray -t timesteps < ./scriptinput/timesteps
readarray -t dampvals < ./scriptinput/dampvals
readarray -t numsteps < ./scriptinput/numsteps
readarray -t outfreqs < ./scriptinput/outfreqs

#loop over timesteps and corresponding numstep
for quantity in Density PotEng Press Temp KinEng TotEng; do
  for ((temp=25;temp<=300;temp=temp+5)); do
    ${LOG2TXT} logfiles/log.argonNPT_melt_temp${temp}\
               results/NPT_melt_${quantity}_temp${temp}\
               Time ${quantity}


    ../plotsimple.py results/NPT_melt_${quantity}_temp${temp}\
                     plots/melt/NPT_${quantity}_temp${temp}\
                     Time ${quantity}\
                     NPT_melt_${quantity}_temp${temp}
  done
done

#plot_melt.py
