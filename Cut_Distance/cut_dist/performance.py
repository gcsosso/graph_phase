#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from glcutn import cut_distance
import time

def erdos_renyi(n, p):
    random_matrix = np.random.rand(n, n)
    adjacency_matrix = np.triu(random_matrix < p, 1)
    adjacency_matrix += adjacency_matrix.T
    return adjacency_matrix.astype(int)

# n = 0, 200, 400, ..., 4000
n_set = np.arange(0, 4000+1, 200)
t = 10;
time_ = np.zeros((1+len(n_set)), dtype = "int")

pointer = 1
for n in n_set:
    dp = 0.01
    min_p = 0
    max_p = 1;
    N = 1+np.floor((max_p-min_p)/dp).astype(np.int16);
    p = np.zeros(N);
    p[0] = min_p
    for i in range(1, N):
        p[i] = p[i-1] + dp;

    cells = np.empty((np.size(p),t),dtype=object);

    for j in range(0,t):
        for i in range(0,np.size(p)):
            cells[i,j] = erdos_renyi(n, p[i])
        print("generate graph n=", n, "_ j = ", j)

    Distance = np.ones((np.size(p),t));
    
    time_start = time.time();
    
    for j in range(0,t):
        for i in range(0,np.size(p)):
            dist = cut_distance(cells[0,j], cells[i,j]);
        print("compute distance n=", n, "_ j = ", j)
    
    time_end = time.time();
    time_used = time_end - time_start;
    time_[pointer] = time_used
    pointer = pointer + 1;


avg_time_ = time_ / (101*t)

np.save("time_results.npy", time_, allow_pickle=True)
np.save("avg_results.npy", avg_time_, allow_pickle=True)           



