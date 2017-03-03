#export LAMMPSBIN=/home/lscheuch/Downloads/lammps-17Nov16/src/lmp_mpi
#readarray -t timesteps < ./scriptinput/timesteps
#readarray -t dampvals < ./scriptinput/dampvals
#readarray -t numsteps < ./scriptinput/numsteps
#readarray -t translatevals < ./scriptinput/translatevals


CURDIR=$(pwd)


${LAMMPSBIN} < in.equi


#rm logfiles/log.equi_gcmc*

#for dampval in ${dampvals[@]}; do
  #for translateval in ${translatevals[@]}; do
    #cp ./in.argonNVT_MC_template.txt in.temp_trans${translateval}_damp${dampval}
    #sed -i "s/<translateval>/$translateval/g" in.temp_trans${translateval}_damp${dampval}
    #sed -i "s/<dampval>/$dampval/g" in.temp_trans${translateval}_damp${dampval}
    #COMMAND="module load openmpi/openmpi161_intel13; cd ${CURDIR}; ${LAMMPSBIN} < in.temp_trans${translateval}_damp${dampval}; sleep 100000s"
    #echo ${COMMAND} > temp_trans${translateval}_damp${dampval}.sh
    #qsub temp_trans${translateval}_damp${dampval}.sh
    ##mpirun -np 4 ${LAMMPSBIN} < in.temp_trans${translateval}
    #rm in.temp_trans${translateval}_damp${dampval}
    #rm temp_trans${translateval}_damp${dampval}.sh
  #done
#done

#rm in.temp*



##loop over timesteps and corresponding numstep
#for i in 0 1 2 ; do
  #for dampval in ${dampvals[@]}
  #do
    #cp ./in.argonNVT_template.txt in.temp
    #sed -i "s/<timestep>/${timesteps[i]}/g" in.temp
    #sed -i "s/<dampval>/${dampval}/g" in.temp
    #sed -i "s/<numsteps>/${numsteps[i]}/g" in.temp
    #sed -i "s/<outfreq>/${outfreqs[i]}/g" in.temp
    #mpirun -n 4 ${LAMMPSBIN} < in.temp 
  #done

#done

#rm in.temp




