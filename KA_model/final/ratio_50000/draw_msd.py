#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import linecache as lc

ratio_B = 0.0;
simulation_number = 6

quench = 50000

record = int(1+quench/10);
msd = np.zeros((record), dtype = "float64");

file = "sim_" + str(int(simulation_number)) + "/simulation/T_" + str(ratio_B) + "/nuc.log";
for p in range(record):
    txt = str.split(lc.getline(file, 224+p));
    txt = txt[3];
    if txt == "-1e+20":
        msd[p] = 0;
    else:
        msd[p] = np.float64(txt);


plt.plot(msd)
plt.xlabel("t 100*(0.2*(m*sigma^2/epsilon)^(1/2))")
# plt.xlim((35000,record))
# plt.ylabel("Q6 diff")
# plt.legend(["Q6 diff"])

plt.show()



