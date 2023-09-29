#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

surv_prob = np.load("swap/surv_prob.npy", allow_pickle=True)
diff = np.load("swap/sop_diff.npy", allow_pickle=True)
sop =np.load("swap/sop.npy", allow_pickle=True)

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



diff = (diff - np.min(diff)) / (np.max(diff)-np.min(diff))
sop = (sop - np.min(sop)) / (np.max(sop)-np.min(sop))

plt.figure(figsize=(8,8))

plt.plot(T, surv_prob)
plt.plot(T, diff)

plt.title("$\mathcal{T} = 20000$")
plt.xlabel("Proportion of B particles p")
plt.ylabel("Normalized measurements") 

fig_1 ,= plt.plot(T, diff)
fig_2 ,= plt.plot(T, sop)
fig_3 ,= plt.plot(T, surv_prob)

plt.legend(handles=[fig_1,fig_2,fig_3],labels=['$\partial \mathcal{D}_s / \partial p$', '$\mathcal{D}_s$', 'Survivial Prob'],loc='best')

plt.savefig("/Users/dmr/Desktop/ans.png", dpi = 300)
plt.show()

