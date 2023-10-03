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
# plt.savefig("/Users/dmr/Desktop/sur_prob_5000.png", dpi = 300)





