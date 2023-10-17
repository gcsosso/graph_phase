#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 0, 100, 900, 1000, 10000, 10100, 15000, 15100, 19900, 20000.

total_simulation_number = 10;

quenching = 20000;

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

heat = np.zeros((sep,sep), dtype = "float32");

for sim in range(total_simulation_number):
    file_name = "ratio_" + str(quenching) + "/sim_" + str(int(sim)) + "/answer/heat_I_" + str(int(quenching/10)) + ".npy";
    data = np.load(file_name, allow_pickle = True);
    heat = heat + data;

heat = heat / total_simulation_number;

v = 0.8;
heat = heat - v
for i in range(sep):
    heat[i,i] = 0;

plt.title("$\mathcal{T} = 50000$")
# plt.figure(figsize=(4,4))
# sns.heatmap(heat);
# plt.matshow(heat);
plt.imshow(heat, cmap = 'hot', interpolation = 'nearest', aspect='equal',origin='upper');
plt.colorbar()
plt.xlabel("Percentage of B particles (p%)")
plt.ylabel("Percentage of B particles (p%)")
# plt.savefig("/Users/dmr/Desktop/heat" + str(quenching) + ".png", dpi = 300);
plt.show()

