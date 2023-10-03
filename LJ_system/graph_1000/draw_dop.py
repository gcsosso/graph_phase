#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

gap = 0.01
T_min = 0.01
T_max = 2.01
sep = np.floor((T_max - T_min) / gap).astype(np.int16)
T = np.zeros(sep, dtype = "float64")
T[0] = T_min
T[1] = T_min + gap
for i in range(2, sep):
    T[i] = T[i-1] + gap
T = T.astype(np.float32)

init_number = 10

measure_0 = np.zeros((init_number), dtype = "object")
measure_1 = np.zeros((init_number), dtype = "object")
measure_2 = np.zeros((init_number), dtype = "object")
measure_3 = np.zeros((init_number), dtype = "object")
measure_4 = np.zeros((init_number), dtype = "object")
measure_5 = np.zeros((init_number), dtype = "object")
measure_6 = np.zeros((init_number), dtype = "object")
measure_7 = np.zeros((init_number), dtype = "object")
measure_8 = np.zeros((init_number), dtype = "object")
measure_9 = np.zeros((init_number), dtype = "object")

for i in range(init_number):
    
    name_0 = "simulation/md_" + str(i) + "/answer/gap_s_bt_0_100.npy"
    name_1 = "simulation/md_" + str(i) + "/answer/gap_s_bt_100_200.npy"
    name_2 = "simulation/md_" + str(i) + "/answer/gap_s_bt_200_300.npy"
    name_3 = "simulation/md_" + str(i) + "/answer/gap_s_bt_300_400.npy"
    name_4 = "simulation/md_" + str(i) + "/answer/gap_s_bt_400_500.npy"
    name_5 = "simulation/md_" + str(i) + "/answer/gap_s_bt_500_600.npy"
    name_6 = "simulation/md_" + str(i) + "/answer/gap_s_bt_600_700.npy"
    name_7 = "simulation/md_" + str(i) + "/answer/gap_s_bt_700_800.npy"
    name_8 = "simulation/md_" + str(i) + "/answer/gap_s_bt_800_900.npy"
    name_9 = "simulation/md_" + str(i) + "/answer/gap_s_bt_900_1000.npy"
    
    file_0 = np.load(name_0, allow_pickle = True)
    file_1 = np.load(name_1, allow_pickle = True)
    file_2 = np.load(name_2, allow_pickle = True)
    file_3 = np.load(name_3, allow_pickle = True)
    file_4 = np.load(name_4, allow_pickle = True)
    file_5 = np.load(name_5, allow_pickle = True)
    file_6 = np.load(name_6, allow_pickle = True)
    file_7 = np.load(name_7, allow_pickle = True)
    file_8 = np.load(name_8, allow_pickle = True)
    file_9 = np.load(name_9, allow_pickle = True)

    measure_0[i] = file_0
    measure_1[i] = file_1
    measure_2[i] = file_2
    measure_3[i] = file_3
    measure_4[i] = file_4
    measure_5[i] = file_5
    measure_6[i] = file_6
    measure_7[i] = file_7
    measure_8[i] = file_8
    measure_9[i] = file_9
    
measure_0_avg = np.sum(measure_0)/init_number
measure_1_avg = np.sum(measure_1)/init_number
measure_2_avg = np.sum(measure_2)/init_number
measure_3_avg = np.sum(measure_3)/init_number
measure_4_avg = np.sum(measure_4)/init_number
measure_5_avg = np.sum(measure_5)/init_number
measure_6_avg = np.sum(measure_6)/init_number
measure_7_avg = np.sum(measure_7)/init_number
measure_8_avg = np.sum(measure_8)/init_number
measure_9_avg = np.sum(measure_9)/init_number

measure_0_avg = measure_0_avg[0:sep]
measure_1_avg = measure_1_avg[0:sep]
measure_2_avg = measure_2_avg[0:sep]
measure_3_avg = measure_3_avg[0:sep]
measure_4_avg = measure_4_avg[0:sep]
measure_5_avg = measure_5_avg[0:sep]
measure_6_avg = measure_6_avg[0:sep]
measure_7_avg = measure_7_avg[0:sep]
measure_8_avg = measure_8_avg[0:sep]
measure_9_avg = measure_9_avg[0:sep]

plt.figure(figsize=(6,8))
f0 ,= plt.plot(T, measure_0_avg)
f1 ,= plt.plot(T, measure_1_avg)
f2 ,= plt.plot(T, measure_2_avg)
f3 ,= plt.plot(T, measure_3_avg)
f4 ,= plt.plot(T, measure_4_avg)
f5 ,= plt.plot(T, measure_5_avg)
f6 ,= plt.plot(T, measure_6_avg)
f7 ,= plt.plot(T, measure_7_avg)
f8 ,= plt.plot(T, measure_8_avg)
f9 ,= plt.plot(T, measure_9_avg)

plt.legend([f0,f1,f2,f3,f4,f5,f6,f7,f8,f9], ['$(n_0,n_1)=(0,100)$', '$(n_1,n_2)=(100,200)$','$(n_2,n_3)=(200,300)$','$(n_3,n_4)=(300,400)$','$(n_4,n_5)=(400,500)$','$(n_5,n_6)=(500,600)$','$(n_6,n_7)=(600,700)$','$(n_7,n_8)=(700,800)$','$(n_8,n_9)=(800,900)$','$(n_9,n_{10})=(900,1000)$'], loc='best') 

plt.xlabel("Temperature ($\epsilon/k_B$)")
plt.ylabel("Dynamical order parameters")
# plt.savefig("dop.png", dpi = 300)
plt.show()



