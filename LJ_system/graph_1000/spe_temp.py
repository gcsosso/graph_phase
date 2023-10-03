#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

T_1 = 0.5
T_2 = 0.75
T_3 = 1.0

ans_1 = np.zeros((100), dtype = "float32")
ans_2 = np.zeros((100), dtype = "float32")
ans_3 = np.zeros((100), dtype = "float32")



for i in range(10):
    file_1 = "simulation/md_" + str(i) + "/answer/D_" + str(i) + "_Ts_gap_0.5.npy"
    file_2 = "simulation/md_" + str(i) + "/answer/D_" + str(i) + "_Ts_gap_0.75.npy"
    file_3 = "simulation/md_" + str(i) + "/answer/D_" + str(i) + "_Ts_gap_1.0.npy"
    swap_a = np.load(file_1, allow_pickle=True)
    swap_b = np.load(file_2, allow_pickle=True)
    swap_c = np.load(file_3, allow_pickle=True)
    ans_1 = ans_1 + swap_a
    ans_2 = ans_2 + swap_b
    ans_3 = ans_3 + swap_c
        
ans_1 = ans_1/10
ans_2 = ans_2/10
ans_3 = ans_3/10
plt.plot(ans_1)
plt.plot(ans_2)
plt.plot(ans_3)
plt.show()