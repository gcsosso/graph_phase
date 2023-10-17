#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import linecache as lc

gap = 0.01;
T_min = 0;
T_max = 1 + gap;
sep = np.floor((T_max - T_min) / gap).astype(np.int16);
T = np.zeros(sep, dtype = "float64");
T[0] = T_min;
T[1] = T_min + gap;
for i in range(2, sep):
    T[i] = T[i-1] + gap;
T = T.astype(np.float32);

thr = 1000;
num_sim = 10;

prob_sur = np.zeros((sep), dtype = "float32");

for prob_b in range(sep):
    text_ = 0;
    count = 0;
    for sim in range(num_sim):
        file = "sim_" + str(int(sim)) + "/simulation/T_" + str(T[prob_b]) + "/nuc.log";
        txt = str.split(lc.getline(file, 5224));
        txt = txt[6];
        if txt == "-1e+20":
            text_ = 0;
        else:
            text_ = np.int32(txt);
        if text_ > thr:
            count = count + 1;
    prob_sur[prob_b] = 1 - count / num_sim;

plt.plot(T, prob_sur)
np.save("swap/surv_prob.npy", prob_sur, allow_pickle=True);
plt.savefig("/Users/dmr/Desktop/ans.png", dpi=300);
plt.show()