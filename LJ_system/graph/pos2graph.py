#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from read_traj import read_xyz_traj

gap = 0.01;
T_min = 0.01;
T_max = 2.4;
sep = np.floor((T_max - T_min) / gap).astype(np.int16);
T = np.zeros(sep, dtype = "float64");
T[0] = T_min;
T[1] = T_min + gap;
for i in range(2, sep):
    T[i] = T[i-1] + gap;
T = T.astype(np.float32);

cell = np.zeros((sep), dtype = object);

time_start = 500;
time_end = 600;

# os.system("rm -rf matrix");
# os.system("mkdir matrix");

for t in range(sep):
    # The method to get the absolute address of a file
    f = "output/T_" + str(T[t]) + "/T_" + str(T[t]) + ".xyz";
    rr = read_xyz_traj(f);
    pos_a = rr[time_start][1][0];
    n_a = len(pos_a);
    pos_b = rr[time_end][1][0];
    n_b = len(pos_b);
    adj_a = np.zeros((n_a, n_a), dtype = "float32");
    adj_a_topo = np.zeros((n_a, n_a), dtype = "float32");
    adj_a_topo_ten = np.zeros((n_a, n_a), dtype = "float32");
    adj_b = np.zeros((n_b, n_b), dtype = "float32");
    adj_b_topo = np.zeros((n_b, n_b), dtype = "float32");
    adj_b_topo_ten = np.zeros((n_b, n_b), dtype = "float32");
    for i in range(n_a):
        for j in range(i+1, n_a):
            x_i = pos_a[i][0];
            y_i = pos_a[i][1];
            z_i = pos_a[i][2];
            x_j = pos_a[j][0];
            y_j = pos_a[j][1];
            z_j = pos_a[j][2];
            x_p = pos_b[i][0];
            y_p = pos_b[i][1];
            z_p = pos_b[i][2];
            x_q = pos_b[j][0];
            y_q = pos_b[j][1];
            z_q = pos_b[j][2];
            r1 = np.sqrt(np.power(x_i-x_j,2)+np.power(y_i-y_j,2)+np.power(z_i-z_j,2));
            r2 = np.sqrt(np.power(x_p-x_q,2)+np.power(y_p-y_q,2)+np.power(z_p-z_q,2));
            if r1 <= 10:
                adj_a[i,j] = r1;
                adj_a_topo[i,j] = 1;
                adj_a_topo_ten[i][j] = 10;
            if r2 <= 10:
                adj_b[i,j] = r2;
                adj_b_topo[i,j] = 1;
                adj_b_topo_ten[i][j] = 10;
        if i%800==0:
            print("T =", T[t],", i =", i)
    adj_a = adj_a + np.transpose(adj_a);
    adj_a_topo = adj_a_topo + np.transpose(adj_a_topo);
    adj_a_topo_ten = adj_a_topo_ten + np.transpose(adj_a_topo_ten);
    name_a = "matrix/cut_10_t_" + str(time_start) + "_T_" + str(T[t]);
    name_a_topo = "matrix/topo_cut_10_t_" + str(time_start) + "_T_" + str(T[t]);
    name_a_topo_ten = "matrix/topo_ten_cut_10_t_" + str(time_start) + "_T_" + str(T[t]);
    
    adj_b = adj_b + np.transpose(adj_b);
    adj_b_topo = adj_b_topo + np.transpose(adj_b_topo);
    adj_b_topo_ten = adj_b_topo_ten + np.transpose(adj_b_topo_ten);
    name_b = "matrix/cut_10_t_" + str(time_end) + "_T_" + str(T[t]);
    name_b_topo = "matrix/topo_cut_10_t_" + str(time_end) + "_T_" + str(T[t]);
    name_b_topo_ten = "matrix/topo_ten_cut_10_t_" + str(time_end) + "_T_" + str(T[t]);
    
    np.save(name_a, adj_a, allow_pickle=True);
    np.save(name_a_topo, adj_a_topo, allow_pickle=True);
    np.save(name_a_topo_ten, adj_a_topo_ten, allow_pickle=True);
    np.save(name_b, adj_b, allow_pickle=True);
    np.save(name_b_topo, adj_b_topo, allow_pickle=True);
    np.save(name_b_topo_ten, adj_b_topo_ten, allow_pickle=True);
    
    
    
    
    