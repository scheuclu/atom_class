readarray -t dampvals < ./scriptinput/dampvals

while read -r cellnum scalefac; do
  echo "cellnum:$cellnum  scalefac:$scalefac"
  for dampval in ${dampvals[@]};do
    for quantity in Lx Ly Lz Press PotEng Density Temp; do

      ${LOG2TXT} logfiles/NPT/boxmod_damp${dampval}_cellnum${cellnum}\
                 ./results/NPT/boxmod_${quantity}_damp${dampval}_cellnum${cellnum}\
                 Time ${quantity}

      ../../plotsimple.py ./results/NPT/boxmod_${quantity}_damp${dampval}_cellnum${cellnum}\
                          ./plots/NPT/simple_boxmod_${quantity}_damp${dampval}_cellnum${cellnum}\
                          Time ${quantity}\
                          ${quantity}_over_Time
    done
  done
done < ./scriptinput/cellnums



