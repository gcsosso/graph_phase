#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from glcutn import cut_distance
import matplotlib.pyplot as plt
import seaborn as sns

def erdos_renyi(n, p):
    random_matrix = np.random.rand(n, n)
    adjacency_matrix = np.triu(random_matrix < p, 1)
    adjacency_matrix += adjacency_matrix.T
    return adjacency_matrix.astype(int)

dp = 0.01
min_p = 0
max_p = 1
N = 1 + np.floor((max_p - min_p) / dp).astype(np.int16)
p = np.zeros(N)
p[0] = min_p
for i in range(1, N):
    p[i] = p[i - 1] + dp

n = 100
t = 10
cells = np.empty((np.size(p), t), dtype=object)

for j in range(0, t):
    for i in range(0, np.size(p)):
        cells[i,j] = erdos_renyi(n, p[i])
    print(f"Generated graphs for iteration {j}")

Distance = np.zeros((np.size(p), np.size(p)))

for j in range(0, t):
    for i1 in range(0, np.size(p) - 1):
        for i2 in range(i1 + 1, np.size(p)):
            dist = cut_distance(cells[i1, j], cells[i2, j])
            Distance[i1, i2] += dist
        print(j, "_", i1)

Distance /= t
Distance = Distance + Distance.T
Distance = np.flipud(Distance)

plt.figure(figsize=(7, 5.5))
plt.title(r'$\mathbb{E}(\text{d}_{\text{cut}}(G(n,\mathcal{P}_1), G(n,\mathcal{P}_2)))$')

tick_positions = [0, int(N/2), N-1]
tick_labels = [0, 0.5, 1]
sns.heatmap(Distance, xticklabels=np.round(p, 2), yticklabels=np.round(p, 2), cmap="viridis")
plt.xticks(tick_positions, tick_labels)
plt.yticks(tick_positions, tick_labels[::-1])
plt.savefig("heatmap", dpi=300)
plt.show()

