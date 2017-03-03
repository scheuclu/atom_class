#readarray -t timesteps < ./scriptinput/timesteps
#readarray -t dampvals < ./scriptinput/dampvals
#readarray -t numsteps < ./scriptinput/numsteps
#readarray -t outfreqs < ./scriptinput/outfreqs
#readarray -t translatevals < ./scriptinput/translatevals


rm plots/gcmc/*
rm results/gcmc/*

for quantity in PotEng Press Temp KinEng TotEng; do
  ${LOG2TXT} ./logfiles/equi.txt\
             ./results/equi_${quantity}.txt\
             Time ${quantity}

  ../plotsimple.py ./results/equi_${quantity}.txt\
                   ./plots/equi_${quantity}.png\
                   Time ${quantity}\
                   Equilibriation_${quantity}
done

#for quantity in Temp v_p2 v_p3 v_p4 KinEng PotEng Press; do
  #${LOG2TXT} ./logfiles/equi.txt\
             #./results/equi_${quantity}.txt\
             #Time ${quantity}

  #../plotsimple.py ./results/equi_${quantity}.txt\
                   #./plots/equi_${quantity}.png\
                   #Time ${quantity}\
                   #Equilibriation_${quantity}
#done

