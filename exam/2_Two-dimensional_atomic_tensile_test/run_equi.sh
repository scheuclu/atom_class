
readarray -t tdampvals < ./scriptinput/Tdamp
readarray -t pdampvals < ./scriptinput/pdamp

CURDIR=$(pwd)


rm logfiles/equi/*
qdel all

for pdamp in ${pdampvals[@]}; do
  for tdamp in ${tdampvals[@]}; do
    cp ./in.equi_template ./in.temp_${pdamp}_${tdamp}
    sed -i "s/<pdamp>/${pdamp}/g" ./in.temp_${pdamp}_${tdamp}
    sed -i "s/<tdamp>/${tdamp}/g" ./in.temp_${pdamp}_${tdamp}

    COMMAND="module load openmpi/openmpi161_intel13; cd ${CURDIR}; mpirun -np 4 ${LAMMPSBIN} <\
             ./in.temp_${pdamp}_${tdamp}; sleep 100000s"
    echo ${COMMAND} > ./temp_${pdamp}_${tdamp}.sh
    qsub -l nodes=1:ppn=4 temp_${pdamp}_${tdamp}.sh

  done
done
