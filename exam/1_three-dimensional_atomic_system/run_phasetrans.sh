


mpirun -np 4 ${LAMMPSBIN} < in.phasetrans
for ((temp=26;temp<=230;temp=temp+1)); do
  
  cp ./in.phasetrans_template in.temp
  sed -i "s/<temp>/$temp/g" in.temp
  mpirun -n 4 $LAMMPSBIN < in.temp
done
