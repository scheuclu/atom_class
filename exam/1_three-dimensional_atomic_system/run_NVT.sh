
readarray -t dampvals < ./scriptinput/dampvals

#echo $cellnums_scales

#for i in ${cellnums_scales[@]}; do
  #echo $i
#done


CURDIR=$(pwd)

rm logfiles/log.NVT*

while read -r cellnum scalefac; do
  echo "cellnum:$cellnum  scalefac:$scalefac"
  for dampval in ${dampvals[@]};do
    echo dampval:${dampval}
    cp ./in.NVT_template ./in.temp_${cellnum}_${scalefac}_${dampval}
    sed -i "s/<dampval>/${dampval}/g" ./in.temp_${cellnum}_${scalefac}_${dampval}
    sed -i "s/<cellnum>/${cellnum}/g" ./in.temp_${cellnum}_${scalefac}_${dampval}
    sed -i "s/<scaleval>/${scalefac}/g" ./in.temp_${cellnum}_${scalefac}_${dampval}
    COMMAND="module load openmpi/openmpi161_intel13; cd ${CURDIR}; mpirun -np 4 ${LAMMPSBIN} < in.temp_${cellnum}_${scalefac}_${dampval}; sleep 100000s"
    echo ${COMMAND} > temp_${cellnum}_${scalefac}_${dampval}.sh
    qsub -l nodes=1:ppn=4 temp_${cellnum}_${scalefac}_${dampval}.sh
    #mpirun -np 4 ${LAMMPSBIN} < ./in.temp
  done
done < ./scriptinput/cellnums




