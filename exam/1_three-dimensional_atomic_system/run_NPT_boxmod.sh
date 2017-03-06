
readarray -t dampvals < ./scriptinput/dampvals
readarray -t boxsizes < ./scriptinput/boxsizes

#echo $cellnums_scales

#for i in ${cellnums_scales[@]}; do
  #echo $i
#done


CURDIR=$(pwd)

rm logfiles/NPT/boxmod*

while read -r cellnum boxsize; do
  echo "cellnum:$cellnum  scalefac:$scalefac"
  for dampval in ${dampvals[@]};do
    echo dampval:${dampval}
    cp ./in.NPT_boxmod_template ./in.temp_${cellnum}_${dampval}
    sed -i "s/<dampval>/${dampval}/g" ./in.temp_${cellnum}_${dampval}
    sed -i "s/<cellnum>/${cellnum}/g" ./in.temp_${cellnum}_${dampval}
    sed -i "s/<scaleval>/${scalefac}/g" ./in.temp_${cellnum}_${dampval}
    sed -i "s/<boxsize>/${boxsize}/g" ./in.temp_${cellnum}_${dampval}
    COMMAND="module load openmpi/openmpi161_intel13; cd ${CURDIR}; mpirun -np 4 ${LAMMPSBIN} < in.temp_${cellnum}_${dampval}; sleep 100000s"
    echo ${COMMAND} > temp_${cellnum}_${dampval}.sh
    qsub -l nodes=1:ppn=4 temp_${cellnum}_${dampval}.sh
    #mpirun -np 4 ${LAMMPSBIN} < ./in.temp
  done
done < ./scriptinput/boxsizes




