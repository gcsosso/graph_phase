#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import networkx as nx
from glcutn import cut_distance
import matplotlib.pyplot as plt

dp = 0.01
min_p = 0
max_p = 1;
N = 1+np.floor((max_p-min_p)/dp).astype(np.int16);
p = np.zeros(N);
p[0] = min_p
for i in range(1, N):
    p[i] = p[i-1] + dp;
    

n = 100
t = 10;
cells = np.empty((np.size(p),t),dtype=object);

for j in range(0,t):
    for i in range(0,np.size(p)):
        G = nx.erdos_renyi_graph(n, p[i]);
        cells[i,j] = np.array(nx.adjacency_matrix(G).todense());
    print(j)

Distance = np.ones((np.size(p),t));
for j in range(0,t):
    for i in range(0,np.size(p)):
        dist = cut_distance(cells[0,j], cells[i,j]);
        Distance[i,j] = dist;
    print(j)

D_avg = np.mean(Distance,1)

plt.figure(figsize=(5,4))
plt.title(r'$\mathbb{E}(\text{d}_{\text{cut}}(G(n,0), G(n,\mathcal{P})))$', fontsize=14)
plt.xlabel("$\mathcal{P}$")
plt.ylabel("The expectation of cut distance")

plt.plot(p,D_avg)
plt.savefig("dist", dpi=300)
plt.show()


