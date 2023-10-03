#!/bin/bash
module purge
module load GCC/10.2.0 OpenMPI/4.0.5
mpirun -np 28 /storage/chem/msrgxt/apps/lammps/src/lmp_mpi < in.LAMMPS