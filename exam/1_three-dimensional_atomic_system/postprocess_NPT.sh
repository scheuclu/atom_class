readarray -t dampvals < ./scriptinput/dampvals

while read -r cellnum scalefac; do
  echo "cellnum:$cellnum  scalefac:$scalefac"
  for dampval in ${dampvals[@]};do
    for quantity in Lx Ly Lz Press Density Temp; do

      ${LOG2TXT} logfiles/NPT/damp${dampval}_cellnum${cellnum}\
                 ./results/NPT/${quantity}_damp${dampval}_cellnum${cellnum}\
                 Time ${quantity}

      ../../plotsimple.py ./results/NPT/${quantity}_damp${dampval}_cellnum${cellnum}\
                          ./plots/NPT/simple_${quantity}_damp${dampval}_cellnum${cellnum}\
                          Time ${quantity}\
                          ${quantity}_over_Time
    done
  done
done < ./scriptinput/cellnums



