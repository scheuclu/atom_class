
#loop over timesteps and corresponding numstep
for quantity in PotEng c_eatoms Density; do
    ${LOG2TXT} logfiles/latticeconst.log\
               results/latticeconst/${quantity}_over_Lx\
               Lx ${quantity}
done

../../plotsingle.py results/latticeconst/PotEng_over_Lx\
                 plots/latticeconst/PotEng_over_Lx.png\
                 'lattice_size [$\AA$]' 'Potential Energy [$\frac{kcal}{mole}$]'\
                 PotEng_over_cellsize\
                 final True

../../plotsingle.py results/latticeconst/Density_over_Lx\
                 plots/latticeconst/Density_over_Lx.png\
                 'lattice_size [$\AA$]' 'Density [gram/cm^3]'\
                 Density_over_cellsize\
                 final True
#plot_melt.py
