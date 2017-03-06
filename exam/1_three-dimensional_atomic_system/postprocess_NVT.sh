readarray -t dampvals < ./scriptinput/dampvals

while read -r cellnum scalefac; do
  echo "cellnum:$cellnum  scalefac:$scalefac"
  for dampval in ${dampvals[@]};do
    for quantity in PotEng Density Press Temp KinEng TotEng; do

      ${LOG2TXT} logfiles/log.NVT_damp${dampval}_cellnum${cellnum}\
                 ./results/NVT/${quantity}_damp${dampval}_cellnum${cellnum}\
                 Time ${quantity}

      ../../plotsimple.py ./results/NVT/${quantity}_damp${dampval}_cellnum${cellnum}\
                          ./plots/NVT/${quantity}_damp${dampval}_cellnum${cellnum}\
                          Time ${quantity}\
                          ${quantity}_over_Time
    done
  done
done < ./scriptinput/cellnums



