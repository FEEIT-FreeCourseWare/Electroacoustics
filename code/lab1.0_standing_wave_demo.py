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

Animate waves.

"""
import numpy as np
import matplotlib.pyplot as plt
import time

# %% init
f = .5  # Hz
c = 343  # m/s
lamda = c / f  # m
k = 2*np.pi / lamda  # m-1
A_d = 1  # Pa
x = np.arange(-3*lamda, 0, 0.1)  # m

# %% animate
# init animation plot
plt.ion()
plt.figure()
plot_p_d, = plt.plot(x, x, ':')  # init
plot_p_r, = plt.plot(x, x, ':')  # init
plot_p_sum, = plt.plot(x, x)  # init
plt.grid()
plt.legend(['direct', 'reflected', 'sum'], loc='upper right')
plt.legend(['директен', 'рефлектиран', 'збирен'], loc='upper right')
plt.xlabel('x [m]')
plt.ylabel('p [Pa]')
plt.axis([x[0], x[-1], -3, 3])

# loop and update
t_0 = time.time()  # s
t = 0  # s, init
while t < 1.1:  # t_max = 5 s
    t = time.time() - t_0
    p_d = A_d * np.cos(2*np.pi*f * t + k*x)  # direct wave
    p_r = A_d * np.cos(2*np.pi*f * t - k*x)  # reflected wave
    p_sum = p_d + p_r  # sum wave
    plot_p_d.set_ydata(p_d)
    plot_p_r.set_ydata(p_r)
    plot_p_sum.set_ydata(p_sum)
    plt.draw()
    plt.pause(0.00001)
