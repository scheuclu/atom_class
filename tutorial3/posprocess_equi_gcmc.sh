#readarray -t timesteps < ./scriptinput/timesteps
readarray -t dampvals < ./scriptinput/dampvals
#readarray -t numsteps < ./scriptinput/numsteps
#readarray -t outfreqs < ./scriptinput/outfreqs
readarray -t translatevals < ./scriptinput/translatevals


rm plots/gcmc/*
rm results/gcmc/*

for quantity in PotEng Press Temp KinEng TotEng; do
  for translateval in ${translatevals[@]};do
    for dampval in ${dampvals[@]}; do
      ${LOG2TXT} ./logfiles/log.equi_gcmc_trans${translateval}_damp${dampval}.txt\
                 ./results/gcmc/equi_${quantity}_trans${translateval}_damp${dampval}.txt\
                 Step ${quantity}

      ../plotsimple.py ./results/gcmc/equi_${quantity}_trans${translateval}_damp${dampval}.txt\
                       ./plots/gcmc/equi_${quantity}_trans${translateval}_damp${dampval}.png\
                       Time ${quantity}\
                       GCMC_equilibrium_${quantity}_damp${dampval}
    done
      ../plotsimple_3.py\
                     results/gcmc/equi_${quantity}_trans${translateval}_damp${dampvals[0]}.txt\
                     results/gcmc/equi_${quantity}_trans${translateval}_damp${dampvals[1]}.txt\
                     results/gcmc/equi_${quantity}_trans${translateval}_damp${dampvals[2]}.txt\
                     plots/gcmc_dampstudy/${quantity}_trans${translateval}.png\
                     Time\
                     ${quantity}\
                     dampval=${dampvals[0]}\
                     dampval=${dampvals[1]}\
                     dampval=${dampvals[2]}\
                     ${quantity}_trans${translateval}
  done
done


plot_autocorrelations.py

##loop over timesteps and corresponding numstep
#for i in 0 1 2  ; do
  #for dampval in ${dampvals[@]}; do
    #for quantity in PotEng Press Temp KinEng TotEng; do
      #${LOG2TXT} logfiles/log.argonNVT_dt${timesteps[i]}_damp${dampval} results/NVT_covergence_${quantity}_dt${timesteps[i]}_damp${dampval}.txt Time ${quantity}


      #../plotsimple.py results/NVT_covergence_${quantity}_dt${timesteps[i]}_damp${dampval}.txt\
                       #plots/NVT/covergence_${quantity}_dt${timesteps[i]}_damp${dampval}.png\
                       #Time ${quantity} NVT_${quantity}_over_time_dt${timesteps[i]}_damp${dampval}
    #done
  #done
#done
