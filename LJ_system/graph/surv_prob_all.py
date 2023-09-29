#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import linecache as lc

# gap_G = 200
# G_min = 200
# G_max = 1000+gap_G
# sep_G = np.floor((G_max - G_min) / gap_G).astype(np.int16)
# G = np.zeros(sep_G, dtype = "float64")
# G[0] = G_min
# G[1] = G_min + gap_G
# for i in range(2, sep_G):
#     G[i] = G[i-1] + gap_G
# G = G.astype(np.float32)

gap = 0.01
T_min = 0.01
T_max = 2.4
sep = np.floor((T_max - T_min) / gap).astype(np.int16)
T = np.zeros(sep, dtype = "float64")
T[0] = T_min
T[1] = T_min + gap
for i in range(2, sep):
    T[i] = T[i-1] + gap
T = T.astype(np.float32)

t_1 = 100
t_2 = 400
t_3 = 800
t_4 = 1000

data_1 = np.load("results/sur_prob_thr_" + str(int(t_1)) + ".npy", allow_pickle=True)
data_2 = np.load("results/sur_prob_thr_" + str(int(t_2)) + ".npy", allow_pickle=True)
data_3 = np.load("results/sur_prob_thr_" + str(int(t_3)) + ".npy", allow_pickle=True)
data_4 = np.load("results/sur_prob_thr_" + str(int(t_4)) + ".npy", allow_pickle=True)


fig_1 ,= plt.plot(T, data_1)
fig_2 ,= plt.plot(T, data_2)
fig_3 ,= plt.plot(T, data_3)
fig_4 ,= plt.plot(T, data_4)

plt.legend(handles=[fig_1,fig_2,fig_3,fig_4],labels=['threshold=100','threshold=400','threshold=800','threshold=1000'],loc='best')

plt.xlabel("Final temperature T ($\epsilon/k_B$)")
plt.ylabel("Survivial probability")
plt.savefig("/Users/dmr/Desktop/ans.png", dpi = 300)





