#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 0, 100, 900, 1000, 10000, 10100, 15000, 15100, 19900, 20000.

total_simulation_number = 10;

choose = 0;
frame = 2000;

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
    file_name = "sim_" + str(int(sim)) + "/answer/gap_s_I_" + str(int(frame-10)) + "_" + str(frame) + ".npy";
    data = np.load(file_name, allow_pickle=True);
    dist_ = data;
    dist = dist + dist_;

dist = dist / total_simulation_number;
dist = dist - dist[0];
dist[0] = dist[1];

dp = 0.1;
d_index = int(dp/gap);
diff_dist = np.zeros((sep), dtype = "float64")
for i in range(d_index, sep):
    diff_dist[i] = (dist[i]-dist[i-d_index]) / (2*dp)

for i in range(d_index):
    diff_dist[i] = diff_dist[d_index]

# np.save("/Users/dmr/Desktop/Data_PRL/KA_model/final/results/dist_20000", dist, allow_pickle=True);
# plt.plot(np.delete(T,int(100*choose)), np.delete(dist,int(100*choose)))
plt.plot(T, diff_dist);
plt.xlabel("Proportion of particle B - p")
plt.ylabel("Graph metric F")
# plt.xlim([0,0.6])
# plt.savefig("/Users/dmr/Desktop/ans.png", dpi = 300);

np.save("swap/dop_diff.npy", diff_dist, allow_pickle=True)

plt.show()

