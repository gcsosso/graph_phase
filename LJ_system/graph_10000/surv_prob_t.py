#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import linecache as lc

Temp = 0.75

N_frame = 10001;

n_frame = int((N_frame-1)/10+1)
N = np.zeros((n_frame), dtype = "int")
for i in range(n_frame):
    N[i] = i + 1


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

init_number = 10

thr = 1000

count = np.zeros((n_frame), dtype = "int")

for t in range(n_frame):
    ct = 0
    for i in range(init_number):
        file = "simulation/md_" + str(i) + "/output/T_" + str(Temp) + "/nuc_" + str(Temp) + "_run_462431.log"
        txt = str.split(lc.getline(file, 257 + t))
        txt = txt[4]
        q6 = 0
        if txt == "-1e+20":
            q6 = 1
        else:
            q6 = int(txt)
        if q6 >= thr:
            ct += 1
    count[t] = ct

sur_pro_t = 1 - count / init_number

plt.xlabel("Time $100*(0.2*(m*\sigma^2/\epsilon)^{1/2})$")
plt.ylabel("Survivial Probability")
plt.title("Temperature = " + str(Temp) + " ($\epsilon/k_B$)")
plt.plot(10*N, sur_pro_t)


