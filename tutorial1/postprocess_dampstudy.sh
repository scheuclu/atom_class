readarray -t timesteps < ./scriptinput/timesteps
readarray -t dampvals < ./scriptinput/dampvals
readarray -t numsteps < ./scriptinput/numsteps
readarray -t outfreqs < ./scriptinput/outfreqs


#loop over timesteps and corresponding numstep
for i in 0 1 2  ; do
  for quantity in PotEng Press Temp KinEng TotEng; do
    for ensemble in Ber NVT; do
      for dampval in ${dampvals[@]}; do
         ${LOG2TXT} ./logfiles/log.argon${ensemble}_dt${timesteps[i]}_damp${dampval}\
               results/${ensemble}_covergence_${quantity}_dt${timesteps[i]}_damp${dampval}.txt\
               Time ${quantity}
      done

      ../plotsimple_3.py\
                     results/${ensemble}_covergence_${quantity}_dt${timesteps[i]}_damp${dampvals[0]}.txt\
                     results/${ensemble}_covergence_${quantity}_dt${timesteps[i]}_damp${dampvals[1]}.txt\
                     results/${ensemble}_covergence_${quantity}_dt${timesteps[i]}_damp${dampvals[2]}.txt\
                     plots/dampstudy/${ensemble}_convergence_${quantity}_dt${timesteps[i]}.png\
                     Time\
                     ${quantity}\
                     dampval=${dampvals[0]}\
                     dampval=${dampvals[1]}\
                     dampval=${dampvals[2]}\
                     ${ensemble}_${quantity}_over_time_dt${timesteps[i]}
    done
  done
done
