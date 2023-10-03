#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import linecache as lc

Temp = 0.5

N_frame = 1001;

N = np.zeros((N_frame), dtype = "int")
for i in range(N_frame):
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

parameter = np.zeros((init_number), dtype = "object")

for i in range(init_number):
    name = "simulation/md_" + str(i) + "/output/T_" + str(Temp) + "/nuc_" + str(Temp) + "_run_462431.log"
    v_max_n = np.zeros((N_frame), dtype="int")
    for j in range(N_frame):
        txt = str.split(lc.getline(name, 293 + j))
        num_str = txt[4];
        if num_str == "-1e+20":
            v_max_n[j] = 1
        else:
            v_max_n[j] = int(num_str)
    parameter[i] = v_max_n
    plt.plot(N, parameter[i])

plt.title("Temperature T = " + str(Temp) + " $(\epsilon/k_B)$")

plt.xlabel("Time $100*(0.2*(m*\sigma^2/\epsilon)^{1/2})$")
plt.ylabel("Local bond order $Q_6$")

plt.savefig("q6_" + str(Temp) + ".png", dpi = 300)
plt.show()


