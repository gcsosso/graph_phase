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
measure_10 = np.zeros((init_number), dtype = "object")

for i in range(init_number):
    
    name_0 = "simulation/md_" + str(i) + "/answer/sop_0.npy"
    name_1 = "simulation/md_" + str(i) + "/answer/sop_50.npy"
    name_2 = "simulation/md_" + str(i) + "/answer/sop_100.npy"
    name_3 = "simulation/md_" + str(i) + "/answer/sop_150.npy"
    name_4 = "simulation/md_" + str(i) + "/answer/sop_200.npy"
    name_5 = "simulation/md_" + str(i) + "/answer/sop_250.npy"
    name_6 = "simulation/md_" + str(i) + "/answer/sop_300.npy"
    name_7 = "simulation/md_" + str(i) + "/answer/sop_350.npy"
    name_8 = "simulation/md_" + str(i) + "/answer/sop_400.npy"
    name_9 = "simulation/md_" + str(i) + "/answer/sop_450.npy"
    name_10 = "simulation/md_" + str(i) + "/answer/sop_500.npy"
    
    
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
    file_10 = np.load(name_10, allow_pickle = True)

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
    measure_10[i] = file_10
    
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
measure_10_avg = np.sum(measure_10)/init_number

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
measure_10_avg = measure_10_avg[0:sep]

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
f10 ,= plt.plot(T, measure_10_avg)

plt.legend([f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10], ['$n_0=0$', '$n_1=500$', '$n_2=1000$', '$n_3=1500$', '$n_4=2000$', '$n_5=2500$', '$n_6=3000$', '$n_7=3500$', '$n_8=4000$', '$n_9=4500$', '$n_{10}=5000$'], loc='best')

plt.xlabel("Temperature ($\epsilon/k_B$)")
plt.ylabel("Structural order parameters")
# plt.savefig("dop.png", dpi = 300)
plt.show()



