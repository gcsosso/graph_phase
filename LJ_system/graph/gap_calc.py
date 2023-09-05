#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

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

gap_head = np.zeros((init_number), dtype = "object")
gap_tail = np.zeros((init_number), dtype = "object")

for i in range(init_number):
    name_head = "simulation/md_" + str(i) + "/answer/gap_bt_800_900.npy"
    name_tail = "simulation/md_" + str(i) + "/answer/gap_bt_900_1000.npy"
    file_head = np.load(name_head, allow_pickle = True)
    file_tail = np.load(name_tail, allow_pickle = True)
    gap_head[i] = file_head
    gap_tail[i] = file_tail
    
gap_head_avg = np.sum(gap_head)/init_number
gap_tail_avg = np.sum(gap_tail)/init_number

plt.plot(T, gap_head_avg)
plt.plot(T, gap_tail_avg)
plt.show()



