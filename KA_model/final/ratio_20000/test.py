#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 0, 100, 900, 1000, 10000, 10100, 15000, 15100, 19900, 20000.

total_simulation_number = 10;

choose = 0;
frame = 2000;

gap = 100;
T_min = 4100;
T_max = 8000 + gap;
sep = np.floor((T_max - T_min) / gap).astype(np.int16);
T = np.zeros(sep, dtype = "float64");
T[0] = T_min;
T[1] = T_min + gap;
for i in range(2, sep):
    T[i] = T[i-1] + gap;
T = T.astype(np.float32);

times = np.zeros((sep), dtype = "int");

delta = 1

for i in range(sep):
    times[i] = delta * (T[i] / T[0]);
    
