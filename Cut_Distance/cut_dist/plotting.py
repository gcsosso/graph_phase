#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# n = 0, 200, 400, ..., 4000
n = np.arange(0, 4000+1, 200)
D = np.load("avg_results.npy", allow_pickle=True)

C = n**2

# Aligning theoretical and experimental results at n = 4000
C = (C-np.min(C))/(np.max(C)-np.min(C))*np.max(D)

plt.figure(figsize=(5,4))
plt.title("The performance of the approximation algorithm")
plt.xlabel("The number of nodes")
plt.ylabel("Average time consumption (second)")
f1 ,= plt.plot(n, D)
f2 ,= plt.plot(n, C)
plt.legend(handles=[f1,f2], labels=["Experiment", "Theory"])
plt.savefig("performance.png", dpi=300)
plt.show()

