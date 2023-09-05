#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import numpy as np
import random as rm

core = 64;
seed = 462431;
init_velocity = rm.randint(1000000, 9999999);
run_step = 100000;

lmp_exe = "/storage/chem/msrgxt/apps/lammps/src/lmp_mpi";


gap = 0.01;
T_min = 0.01;
# T_max = 0.04;
T_max = 2.4;
sep = np.floor((T_max - T_min) / gap).astype(np.int16);
T = np.zeros(sep, dtype = "float64");
T[0] = T_min;
T[1] = T_min + gap;
for i in range(2, sep):
    T[i] = T[i-1] + gap;
T = T.astype(np.float32);


menu = "simulation/md_" + str(seed) + "_" + str(init_velocity);

os.system("mkdir " + menu);
os.system("mkdir " + menu + "/input");
os.system("mkdir " + menu + "/output");
os.system("cp -a code/* " + menu + "/input");
lmp_script = menu + "/input/in.LAMMPS";
run_script = menu + "/input/lmp.sh";

cmd_lmp = "mpirun -np " + str(core) + " " + lmp_exe + " < " + lmp_script;

ls = [];
with open(run_script, 'r') as f:
    ls = f.readlines();
ls[3] = cmd_lmp;
with open(run_script, 'w') as f:
    for data in ls:
        f.write(data);
    f.flush();


for p in range(sep):
    menu_save = menu + "/output/T_" + str(T[p]);
    lines = [];
    with open(lmp_script, 'r') as f:
        lines = f.readlines();
    lines[10] = "variable temp equal (" + str(T[p]) + ")    # temperature to simulate at" + "\n";
    lines[11] = "variable rng equal (" + str(seed) + ")   # random number seed" + "\n";
    lines[60] = "velocity all create 2.4 " + str(init_velocity) + " mom yes dist gaussian # Assign velocities" + "\n";
    lines[131] = "run " + str(run_step) + " # 5000000  # Run for this many steps" + "\n";
    with open(lmp_script, 'w') as f:
        for data in lines:
            f.write(data);
        f.flush();
    
    os.system(menu + "/input/lmp.sh");
    os.system("rm -rf " + menu_save);
    os.system("mkdir " + menu_save);
    os.system("cp -a data.* log.* nuc_* traj_* " + menu_save);
    os.system("rm -rf data.* log.* nuc_* traj_*");
    os.system("cp -a " + menu_save + "/traj_*.dcd " + "convert/traj_" + str(seed) + "_" + str(init_velocity) + "_" + str(T[p]) + ".dcd");
    os.system("convert/convert convert/traj_" + str(seed) + "_" + str(init_velocity) + "_" + str(T[p]) + ".dcd convert/T_" + str(T[p]) +".xyz");
    os.system("mv convert/T_" + str(T[p]) + ".xyz " + menu_save);
    os.system("rm -rf convert/traj_" + str(seed) + "_" + str(init_velocity) + "_" + str(T[p]) + ".dcd");
    
    print("The " + str(p) + "-th temperature " + str(T[p]) + " is done.");



