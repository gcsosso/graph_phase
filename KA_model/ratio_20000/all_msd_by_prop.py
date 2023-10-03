#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import linecache as lc

sim = 0;
quench = 20000;
record = int(1+quench/10);

gap = 0.01;
T_min = 0;
T_max = 1+gap;
sep = np.floor((T_max - T_min) / gap).astype(np.int16);
T = np.zeros(sep, dtype = "float64");
T[0] = T_min;
T[1] = T_min + gap;
for i in range(2, sep):
    T[i] = T[i-1] + gap;
T = T.astype(np.float32);

msd = np.zeros((record,101), dtype = "float32");

dx = 10;
x_min = 0;
x_max = 20000+dx;
sx = np.floor((x_max - x_min) / dx).astype(np.int16);
x = np.zeros(sx, dtype = "float64");
x[0] = x_min;
x[1] = x_min + dx;
for i in range(2, sx):
    x[i] = x[i-1] + dx;
x = x.astype(np.float32);

for i in range(sep):
    file = "sim_" + str(int(sim)) + "/simulation/T_" + str(T[i]) + "/nuc.log";
    for p in range(record):
        txt = str.split(lc.getline(file, 224+p));
        txt = txt[3];
        if txt == "-1e+20":
            msd[p,i] = 0;
        else:
            msd[p,i] = np.float64(txt);

np.save("swap/msd.npy", msd, allow_pickle = True);

plt.plot(x,msd)
plt.xlabel("t 100*(0.2*(m*sigma^2/epsilon)^(1/2))")
plt.ylabel("MSD")
# plt.savefig("/Users/dmr/Desktop/Data_PRL/KA_model/figure/msd_5000.png", dpi = 300);
plt.show()

