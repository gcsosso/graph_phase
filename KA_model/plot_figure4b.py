#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

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

plt.rcParams['font.size'] = 20
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(16,14))

P_1 = np.load("ratio_5000/swap/surv_prob.npy", allow_pickle = True)
P_1 = (P_1 - np.min(P_1)) / (np.max(P_1) - np.min(P_1))
sop_1 = np.load("ratio_5000/swap/sop.npy", allow_pickle = True)
sop_1 = (sop_1 - np.min(sop_1)) / (np.max(sop_1) - np.min(sop_1))
sop_diff_1 = np.load("ratio_5000/swap/sop_diff.npy", allow_pickle = True)
sop_diff_1 = (sop_diff_1 - np.min(sop_diff_1)) / (np.max(sop_diff_1) - np.min(sop_diff_1))
dop_1 = np.load("ratio_5000/swap/dop.npy", allow_pickle = True)
dop_1 = (dop_1 - np.min(dop_1)) / (np.max(dop_1) - np.min(dop_1))
dop_diff_1 = np.load("ratio_5000/swap/dop_diff.npy", allow_pickle = True)
dop_diff_1 = (dop_diff_1 - np.min(dop_diff_1)) / (np.max(dop_diff_1) - np.min(dop_diff_1))

P_2 = np.load("ratio_20000/swap/surv_prob.npy", allow_pickle = True)
P_2 = (P_2 - np.min(P_2)) / (np.max(P_2) - np.min(P_2))
sop_2 = np.load("ratio_20000/swap/sop.npy", allow_pickle = True)
sop_2 = (sop_2 - np.min(sop_2)) / (np.max(sop_2) - np.min(sop_2))
sop_diff_2 = np.load("ratio_20000/swap/sop_diff.npy", allow_pickle = True)
sop_diff_2 = (sop_diff_2 - np.min(sop_diff_2)) / (np.max(sop_diff_2) - np.min(sop_diff_2))
dop_2 = np.load("ratio_20000/swap/dop.npy", allow_pickle = True)
dop_2 = (dop_2 - np.min(dop_2)) / (np.max(dop_2) - np.min(dop_2))
dop_diff_2 = np.load("ratio_20000/swap/dop_diff.npy", allow_pickle = True)
dop_diff_2 = (dop_diff_2 - np.min(dop_diff_2)) / (np.max(dop_diff_2) - np.min(dop_diff_2))

P_3 = np.load("ratio_50000/swap/surv_prob.npy", allow_pickle = True)
P_3 = (P_3 - np.min(P_3)) / (np.max(P_3) - np.min(P_3))
sop_3 = np.load("ratio_50000/swap/sop.npy", allow_pickle = True)
sop_3 = (sop_3 - np.min(sop_3)) / (np.max(sop_3) - np.min(sop_3))
sop_diff_3 = np.load("ratio_50000/swap/sop_diff.npy", allow_pickle = True)
sop_diff_3 = (sop_diff_3 - np.min(sop_diff_3)) / (np.max(sop_diff_3) - np.min(sop_diff_3))
dop_3 = np.load("ratio_50000/swap/dop.npy", allow_pickle = True)
dop_3 = (dop_3 - np.min(dop_3)) / (np.max(dop_3) - np.min(dop_3))
dop_diff_3 = np.load("ratio_50000/swap/dop_diff.npy", allow_pickle = True)
dop_diff_3 = (dop_diff_3 - np.min(dop_diff_3)) / (np.max(dop_diff_3) - np.min(dop_diff_3))


ax1 = plt.subplot(231)
ax1.plot(T, P_1, markerfacecolor='r', label='$\mathcal{P}$')
ax1.plot(T, sop_1, markerfacecolor='g', label='$\mathcal{D}_s$')
ax1.plot(T, sop_diff_1, markerfacecolor='b', label='$\partial \mathcal{D}_s / \partial p$')
ax1.set_title('$\mathcal{T} = 5000$',  fontsize=25)
ax1.set_ylabel('Normalized structural measurements', fontsize=22)
ax1.legend(fontsize = 20, loc='lower center')
plt.tight_layout()

ax2 = plt.subplot(232)
ax2.plot(T, P_2, markerfacecolor='r', label='$\mathcal{P}$')
ax2.plot(T, sop_2, markerfacecolor='g', label='$\mathcal{D}_s$')
ax2.plot(T, sop_diff_2, markerfacecolor='b', label='$\partial \mathcal{D}_s / \partial p$')
ax2.set_title('$\mathcal{T} = 20000$',  fontsize=25)
# ax2.legend(fontsize = 20, loc='lower left')
plt.tight_layout()

ax3 = plt.subplot(233)
ax3.plot(T, P_3, markerfacecolor='r', label='$\mathcal{P}$')
ax3.plot(T, sop_3, markerfacecolor='g', label='$\mathcal{D}_s$')
ax3.plot(T, sop_diff_3, markerfacecolor='b', label='$\partial \mathcal{D}_s / \partial p$')
ax3.set_title('$\mathcal{T} = 50000$',  fontsize=25)
plt.tight_layout()


ax4 = plt.subplot(234)
ax4.plot(T, P_1, markerfacecolor='r', label='$\mathcal{P}$')
ax4.plot(T, dop_1, markerfacecolor='g', label='$\mathcal{D}_d$')
ax4.plot(T, dop_diff_1, markerfacecolor='b', label='$\partial \mathcal{D}_d / \partial p$')
ax4.set_xlabel('Proportion of B particles $p$')
ax4.set_ylabel('Normalized dynamic measurements', fontsize=22)
ax4.legend(fontsize = 20, loc='center')
plt.tight_layout()

ax5 = plt.subplot(235)
ax5.plot(T, P_2, markerfacecolor='r', label='$\mathcal{P}$')
ax5.plot(T, dop_2, markerfacecolor='g', label='$\mathcal{D}_d$')
ax5.plot(T, dop_diff_2, markerfacecolor='b', label='$\partial \mathcal{D}_d / \partial p$')
ax5.set_xlabel('Proportion of B particles $p$')
plt.tight_layout()


ax6 = plt.subplot(236)
ax6.plot(T, P_3, markerfacecolor='r', label='$\mathcal{P}$')
ax6.plot(T, dop_3, markerfacecolor='g', label='$\mathcal{D}_d$')
ax6.plot(T, dop_diff_3, markerfacecolor='b', label='$\partial \mathcal{D}_d / \partial p$')
ax6.set_xlabel('Proportion of B particles $p$')
plt.tight_layout()

# plt.savefig("/Users/dmr/Desktop/ans.png", dpi = 300)

plt.show()
