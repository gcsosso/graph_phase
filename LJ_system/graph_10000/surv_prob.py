#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import linecache as lc

gap = 0.01
T_min = 0.01
T_max = 2.01+gap
sep = np.floor((T_max - T_min) / gap).astype(np.int16)
T = np.zeros(sep, dtype = "float64")
T[0] = T_min
T[1] = T_min + gap
for i in range(2, sep):
    T[i] = T[i-1] + gap
T = T.astype(np.float32)

thr = 1000;
num_sim = 10;

prob_sur = np.zeros((sep), dtype = "float32");

for i in range(sep):
    count = 0
    for j in range(num_sim):
        nuc_file = ""
        temp = T[i]
        num = j
        if(temp == 1):
            nuc_file = "simulation/md_" + str(int(num)) + "/output/T_1.0/nuc_1_run_462431.log"
        else:
            if(temp == 2):
                nuc_file = "simulation/md_" + str(int(num)) + "/output/T_2.0/nuc_2_run_462431.log"
            else:
               nuc_file = "simulation/md_" + str(int(num)) + "/output/T_" + str(temp) + "/nuc_" + str(temp) + "_run_462431.log"
        txt = str.split(lc.getline(nuc_file, 1257));
        txt = txt[4]
        text_ = 0
        if txt == "-1e+20":
            text_ = 0;
        else:
            text_ = np.int32(txt);
        if text_ > thr:
            count = count + 1;
    prob_sur[i] = 1 - count / num_sim;


plt.plot(T, prob_sur)
np.save("results/sur_prob_thr_" + str(int(thr)), prob_sur, allow_pickle=True);
# plt.savefig("/Users/dmr/Desktop/ans.png", dpi=300);
plt.show()

