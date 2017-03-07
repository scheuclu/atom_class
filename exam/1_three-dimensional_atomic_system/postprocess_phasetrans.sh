




for quantity in Lx TotEng PotEng KinEng Press Density Temp; do
for ((temp=26;temp<=230;temp=temp+1)); do

  ${LOG2TXT} ./logfiles/phasetrans/temp${temp}.log\
             ./results/phasetrans/temp${temp}_${quantity}.txt\
             Time ${quantity}
done
done
