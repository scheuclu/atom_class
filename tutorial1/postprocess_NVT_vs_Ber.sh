
readarray -t timesteps < ./scriptinput/timesteps
readarray -t dampvals < ./scriptinput/dampvals
readarray -t numsteps < ./scriptinput/numsteps
readarray -t outfreqs < ./scriptinput/outfreqs


#loop over timesteps and corresponding numstep
for i in 0 1 2  ; do
  for dampval in ${dampvals[@]}; do
    for quantity in PotEng Press Temp KinEng TotEng; do
      for ensemble in Ber NVT; do
        ${LOG2TXT} ./logfiles/log.argon${ensemble}_dt${timesteps[i]}_damp${dampval}\
                 results/${ensemble}_covergence_${quantity}_dt${timesteps[i]}_damp${dampval}.txt\
                 Time ${quantity}
      done


      ../plotsimple_2.py results/NVT_covergence_${quantity}_dt${timesteps[i]}_damp${dampval}.txt\
                       results/Ber_covergence_${quantity}_dt${timesteps[i]}_damp${dampval}.txt\
                       plots/NVTvsBer/convergence_${quantity}_dt${timesteps[i]}_damp${dampval}.png\
                       Time\
                       ${quantity}\
                       NVT\
                       Berendsen\
                       NVTvsBer_${quantity}_over_time_dt${timesteps[i]}_damp${dampval}
    done
  done
done
