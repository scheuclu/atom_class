


START=25
END=300
for ((temp=25;temp<=300;temp=temp+5)); do
  
  cp ./in.argonNPT_melt_template.txt in.temp
  sed -i "s/<temperature>/$temp/g" in.temp
  mpirun -n 4 $LAMMPSBIN < in.temp
done
