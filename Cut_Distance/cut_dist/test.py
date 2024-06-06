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

n = 4000
p_1 = 0.3
p_2 = 0.7

A = erdos_renyi(n, p_1)
B = erdos_renyi(n, p_2)

t_1 = time.time()
s = cut_distance(A, B);
t_2 = time.time()

print("The cut distance d(A,B) = ", s)
print("The time consumption is ", t_2-t_1, " (seconds)")

