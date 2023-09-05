#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import linecache as lc

ratio_B = 0.55
simulation_number = 0

quench = 50000;

record = int(1+quench/10)
q6 = np.zeros((record), dtype = np.int32)

file = "sim_" + str(int(simulation_number)) + "/simulation/T_" + str(ratio_B) + "/nuc.log"
for p in range(record):
    txt = str.split(lc.getline(file, 224+p))
    txt = txt[6];
    if txt == "-1e+20":
        q6[p] = 0
    else:
        q6[p] = np.int32(txt)



# plt.plot(diff);
plt.plot(q6)
plt.xlabel("t (0.2*(m*sigma^2/epsilon)^(1/2))")
# plt.xlim((35000,record))
# plt.ylabel("Q6 diff")
# plt.legend(["Q6 diff"])

plt.show()
