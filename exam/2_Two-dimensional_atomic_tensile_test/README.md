#Two dimensional atomistic tensile test

[up_dir](../)
## Structure
### [logfiles](logfiles)
Contains all logfiles created during the simulations.

### [results](results)
Contains all the .csv files extracted from the logfiles.

### [plots](plots)
Contains all plots created from the results-files.

### [data](data)
Contains system snapshots to be read again.

### [scriptinput](scripinput)
contains input files that control the automatic parameter variation.

### [dump](dump)
Contains the dump files that store system trajectories during the simulations.


## Scripts

### [run_equi.sh](run_equi.sh)
Runs the equilibriation of the system for different combinations of damping parameters.

### [run_tensiltest.sh](run_tensiltest.sh)
Runs the tensile-test based on the system status saved by a previous equilibriation process.

### [postprocess_equi.sh](postprocess_equi.sh)
Extracts data from the logfiles of the equilibriation simulation and stores thhem into [results](results).

### [plot_equi_NVT.py](plot_equi_NVT.py)
Plots the time convergence of thermodynamic quantities during the equilibriation simulations with different damping parameter combinations.

### [plot_stress_strain.py](plot_stress_strain.py)
Plots the stress-strain relation obtained by the tensile-test.

### [cleanall.sh](cleanall.sh)
Cleans the directory from temporary files that are created by some scripts.
