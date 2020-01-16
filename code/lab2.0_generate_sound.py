# -*- coding: utf-8 -*-
#
# Copyright 2016 - 2020 by Branislav Gerazov
#
# See the file LICENSE for the license associated with this software.
#
# Author(s):
#   Branislav Gerazov, Nov 2016
#
"""
Electroacoustics

Psychoacoustics - frequency upper limit.

"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile
import os

# %% generate sound
f = 12000
fs = 44100
ts = 1 / fs
t = np.arange(0, 1, ts)
sound = np.sin(2*np.pi*f * t)

# %% plot sound
plt.figure()
plt.plot(t, sound)

# %% play sound
wavfile.write('sound.wav', fs, np.int16(sound * 2**15))
os.system('play sound.wav')
