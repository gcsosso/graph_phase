#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 0, 100, 900, 1000, 10000, 10100, 15000, 15100, 19900, 20000.

total_simulation_number = 10;

choose = 490;
frame = 500;

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

dist = np.zeros((sep), dtype = "float32");

for sim in range(total_simulation_number):
    file_name = "sim_" + str(int(sim)) + "/answer/gap_s_I_" + str(choose) + "_" + str(frame) + ".npy";
    data = np.load(file_name, allow_pickle=True);
    dist_ = data;
    dist = dist + dist_;

dist = dist / total_simulation_number;
dist = dist - dist[0];
dist[0] = dist[1];
np.save("/Users/dmr/Desktop/Data_PRL/KA_model/final/results/gap_5000", dist, allow_pickle=True);
# plt.plot(np.delete(T,int(100*choose)), np.delete(dist,int(100*choose)))
plt.plot(T, dist);
plt.xlabel("Proportion of particle B - p")
plt.ylabel("Graph metric F")
# plt.xlim([0,0.6])

np.save("swap/dop.npy", dist, allow_pickle=True)

plt.savefig("/Users/dmr/Desktop/ans.png", dpi = 300);
plt.show()

