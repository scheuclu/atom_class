readarray -t timesteps < ./scriptinput/timesteps
readarray -t dampvals < ./scriptinput/dampvals
readarray -t numsteps < ./scriptinput/numsteps
readarray -t outfreqs < ./scriptinput/outfreqs

#loop over timesteps and corresponding numstep
for i in 0 1 2  ; do
  for dampval in ${dampvals[@]}; do
    for quantity in PotEng Press Temp KinEng TotEng; do
      ${LOG2TXT} logfiles/log.argonNVT_dt${timesteps[i]}_damp${dampval} results/NVT_covergence_${quantity}_dt${timesteps[i]}_damp${dampval}.txt Time ${quantity}


      ../plotsimple.py results/NVT_covergence_${quantity}_dt${timesteps[i]}_damp${dampval}.txt\
                       plots/NVT/covergence_${quantity}_dt${timesteps[i]}_damp${dampval}.png\
                       Time ${quantity} NVT_${quantity}_over_time_dt${timesteps[i]}_damp${dampval}
    done
  done
done
