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

Simulate mode sound field.

"""
import numpy as np
import sfs

# %% init room
dims = 8.5, 3.9, 3.9  # l * w * h in m3
alpha = 0.01  # wall absorption
n_order = 20  # maximum number of reflections
c = 343  # m/s

# %% plot modes
f = 88
omega = 2*np.pi*f
x0 = dims[0]/2, dims[1]/2, 1  # source location

grid = sfs.util.xyz_grid(
    (0, dims[0]),
    (0, dims[1]),
    dims[2] / 2,
    spacing=.1
    )
p = sfs.fd.source.point_modal(
    omega,
    x0,
    grid,
    dims,
    N=n_order,
    deltan=alpha,
    )
p *= 0.05
sfs.plot2d.amplitude(p, grid)
sfs.plot2d.virtualsource(x0)
