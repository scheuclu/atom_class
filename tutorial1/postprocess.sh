
LOG2TXT=/home/lukas/Downloads/lammps/tools/python/log2txt.py
export LAMMPS_PYTHON_TOOLS=/home/lukas/Downloads/lammps/tools/python/pizza

$LOG2TXT log.argon.equilibrium results/data.argon.equi.Step_PotEng.txt Step PotEng

$LOG2TXT log.argon.equilibrium results/data.argon.equi.Step_PotEng.txt Step Lx

../plotsimple.py results/data.argon.equi.Step_PotEng.txt plots/equi.Step_PotEng.png Step Energy Equilibriation-Energy-development

../plotsimple.py results/data.argon.equi.Step_PotEng.txt plots/equi.Step_PotEng.png Step Energy Equilibriation-Cellsize-development

