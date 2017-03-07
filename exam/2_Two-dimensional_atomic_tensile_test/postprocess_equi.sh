readarray -t tdampvals < ./scriptinput/Tdamp
readarray -t pdampvals < ./scriptinput/pdamp


rm ./results/NVT_*
rm ./plots/equi/simple_*

for pdamp in ${pdampvals[@]}; do
  for tdamp in ${tdampvals[@]}; do
    for quantity in Lx TotEng PotEng KinEng Press Density Temp; do
      ${LOG2TXT} ./logfiles/equi/equi_${pdamp}_${tdamp}.log\
                 ./results/equi/NVT_${quantity}_${pdamp}_${tdamp}.txt\
                 Time ${quantity}
      ../../plotsimple.py ./results/equi/NVT_${quantity}_${pdamp}_${tdamp}.txt\
                          ./plots/equi/simple_NVT_${quantity}_pdamp${pdamp}_tdamp${tdamp}.png\
                          Time ${quantity}\
                          ${quantity}_over_time
    done
  done
done
