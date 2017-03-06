readarray -t dampvals < ./scriptinput/dampvals


CURDIR=$(pwd)


rm logfiles/log.equi_gcmc*

for dampval in ${dampvals[@]}; do
    cp ./in.NVT_MCMC in.temp_MCMC_damp${dampval}
    sed -i "s/<dampval>/$dampval/g" in.temp_MCMC_damp${dampval}
    COMMAND="module load openmpi/openmpi161_intel13; cd ${CURDIR}; mpirun -np 4 ${LAMMPSBIN} < in.temp_MCMC_damp${dampval}; sleep 100000s"
    echo ${COMMAND} > temp_damp${dampval}.sh
    qsub temp_damp${dampval}.sh
    #mpirun -np 4 ${LAMMPSBIN} < in.temp_damp${dampval}
done

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




