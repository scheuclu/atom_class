# Three-dimensional atomic system

[up_dir](../)

## Structure
### [logfiles](logfiles)
Contains all logfiles created during the simulations.

### [results](results)
Contains all the .csv files extracted from the logfiles.

### [plots](plots)
Contains all plots created from the results-files.

### [scriptinput](scripinput)
contains input files that control the automatic parameter variation.

### [dump](dump)
Contains the dump files that store system trajectories during the simulations.

## Scripts
### Run-Scripts
[run_latticeconst.sh](run_latticeconst.sh)
Runs the minimiazation process to determine the lattice cosntant.

[run_NPT_boxmod.sh](run_NPT_boxmod.sh)
Runs the simulations with a Nose-Hover thermostat and a modified box-size, according to the equilibrium box-sizes obtained previously.


[run_NPT.sh](run_NPT.sh)
Runs the simulations with a Nose-Hoover barostat.

[run_NVEBer.sh](run_NVEBer.sh)
Runs the simulations with a weakly-coupled Berendsen algorithm.

[run_NVT_MCMC.sh](run_NVT_MCMC.sh)
Runs the simulations usins a Markov-chain Monte Carlo approach.

[run_NVT.sh](run_NVT.sh)
Runs the simulations with Nose-Hover thermostat.

[run_phasetrans.sh](run_phasetrans.sh)
Runs the phase transition analysis.

### Postprocessing-Scripts

[postprocess_CV.sh](postprocess_CV.sh)
Extracts data from the logfiles and stores it into text-based data files in ./results/ .

[postprocess_latticeconst.sh](postprocess_latticeconst.sh)3
Extracts data from the logfiles and stores it into text-based data files in ./results/ .

[postprocess_MCMC.sh](postprocess_MCMC.sh)
Extracts data from the logfiles and stores it into text-based data files in ./results/ .

[postprocess_NPT_boxmod.sh](postprocess_NPT_boxmod.sh)
Extracts data from the logfiles and stores it into text-based data files in ./results/ .

[postprocess_NPT.sh](postprocess_NPT.sh)
Extracts data from the logfiles and stores it into text-based data files in ./results/ .

[postprocess_NVEBer.sh](postprocess_NVEBer.sh)
Extracts data from the logfiles and stores it into text-based data files in ./results/ .

[postprocess_NVT.sh](postprocess_NVT.sh)
Extracts data from the logfiles and stores it into text-based data files in ./results/ .

[postprocess_phasetrans.sh](postprocess_phasetrans.sh)
Extracts data from the logfiles and stores it into text-based data files in ./results/ .

### Plotting-Scripts

[plot_boxsizesim.py](plot_boxsizesim.py)

[plot_cellnum_study.py](plot_cellnum_study.py)

[plot_CV.py](plot_CV.py)

[plot_dampstudy.py](plot_dampstudy.py)

[plot_MCMC_vs_NVT.py](plot_MCMC_vs_NVT.py)

[plot_NVT_vs_NVEBer.py](plot_NVT_vs_NVEBer.py)

[plot_phasetrans.py](plot_phasetrans.py)

[plot_phasetrans_reduced.py](plot_phasetrans_reduced.py)

[calc_CV.py](calc_CV.py)

