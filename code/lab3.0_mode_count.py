# -*- coding: utf-8 -*-
#
# Copyright 2020 by Branislav Gerazov
#
# See the file LICENSE for the license associated with this software.
#
# Author(s):
#   Branislav Gerazov, Nov 2020
#
"""
Electroacoustics

Count modes.

"""
import numpy as np
import matplotlib.pyplot as plt
import itertools

# %% init
c = 343  # m/s
dims = 8.5, 3.9, 3.9  # lx, ly, lz
n_max = 3
ns = itertools.product(
    range(n_max+1),
    range(n_max+1),
    range(n_max+1)
    )
ns = list(ns)[1:]

# %% loop through modes
fs = []
for n in ns:
    k = np.pi * np.sqrt(
            (n[0]/dims[0])**2
            + (n[1]/dims[1])**2
            + (n[2]/dims[2])**2
            )
    lamda = 2*np.pi / k
    f = c / lamda
    fs.append(f)

# %% sort and plot
ns = np.array(ns)
fs = np.array(fs)
inds = np.argsort(fs)

ns_sorted = ns[inds]
fs_sorted = fs[inds]

plt.figure()
plt.hist(fs, 100)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Mode count')
plt.grid()
