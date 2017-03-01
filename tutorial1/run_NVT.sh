
readarray -t timesteps < ./scriptinput/timesteps
readarray -t dampvals < ./scriptinput/dampvals
readarray -t numsteps < ./scriptinput/numsteps
readarray -t outfreqs < ./scriptinput/outfreqs

#loop over timesteps and corresponding numstep
for i in 0 1 2 ; do
  for dampval in ${dampvals[@]}
  do
    cp ./in.argonNVT_template.txt in.temp
    sed -i "s/<timestep>/${timesteps[i]}/g" in.temp
    sed -i "s/<dampval>/${dampval}/g" in.temp
    sed -i "s/<numsteps>/${numsteps[i]}/g" in.temp
    sed -i "s/<outfreq>/${outfreqs[i]}/g" in.temp
    mpirun -n 4 ${LAMMPSBIN} < in.temp 
  done

done

#rm in.temp




