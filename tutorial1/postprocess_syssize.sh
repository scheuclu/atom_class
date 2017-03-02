readarray -t timesteps < ./scriptinput/timesteps
readarray -t dampvals < ./scriptinput/dampvals
readarray -t numsteps < ./scriptinput/numsteps
readarray -t outfreqs < ./scriptinput/outfreqs
readarray -t cellnums < ./scriptinput/cellnums

#loop over timesteps and corresponding numstep
for cellnum in ${cellnums[@]}; do
  for quantity in PotEng Press Temp KinEng TotEng; do
    ${LOG2TXT} logfiles/log.NVT_syssize_${cellnum}\
               results/NVT_convergence_syssize_${quantity}_${cellnum}.txt\
               Time ${quantity}
  done
done

./plot_syssize_dependence.py
