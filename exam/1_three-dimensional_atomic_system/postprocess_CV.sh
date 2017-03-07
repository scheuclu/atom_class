


for quantity in Lx PotEng Density Press Temp KinEng TotEng; do

  ${LOG2TXT} logfiles/CV/equi.log\
             ./results/CV/equi_${quantity}.txt\
             Time ${quantity}

  ../../plotsimple.py ./results/CV/equi_${quantity}.txt\
                      ./plots/CV/simple_equi_${quantity}.png\
                      Time ${quantity}\
                      ${quantity}_over_Time

  ${LOG2TXT} logfiles/CV/NVT.log\
             ./results/CV/NVT_${quantity}.txt\
             Time ${quantity}

  ../../plotsimple.py ./results/CV/NVT_${quantity}.txt\
                      ./plots/CV/simple_NVT_${quantity}.png\
                      Time ${quantity}\
                      ${quantity}_over_Time
done




for dir in plus minus; do
for quantity in Lx PotEng Density Press Temp KinEng TotEng; do
  ${LOG2TXT} logfiles/CV/NVT_${dir}.log\
             ./results/CV/NVT_${dir}_${quantity}.txt\
             Time ${quantity}

  ../../plotsimple.py ./results/CV/NVT_${dir}_${quantity}.txt\
                      ./plots/CV/simple_NVT_${dir}_${quantity}.png\
                      Time ${quantity}\
                      ${quantity}_over_Time
done
done



