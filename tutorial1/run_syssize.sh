
readarray -t timesteps < ./scriptinput/timesteps
readarray -t dampvals < ./scriptinput/dampvals
readarray -t numsteps < ./scriptinput/numsteps
readarray -t cellnums < ./scriptinput/cellnums

for cellnum in ${cellnums[@]}
do
  cp ./in.argonNVT_syssize_template.txt in.temp
  sed -i "s/<numcells>/${cellnum}/g" in.temp
  mpirun -n 4 ${LAMMPSBIN} < in.temp 
done


#rm in.temp




