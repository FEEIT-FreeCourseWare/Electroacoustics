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

Psychoacoustics - frequency perception.

"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile
import scipy.signal as sig
import os
import ea

# %% generate sound
f = 440
fs = 44100
ts = 1 / fs
t = np.arange(0, 4, ts)
sound = sig.chirp(t, 100, t[-1], 10000)
sound_log = sig.chirp(t, 100, t[-1], 10000, method='logarithmic')

# %% plot sound
plt.figure()
plt.plot(t, sound)

# %% plot spectrogram
spectrogram = ea.get_spectrogram(fs, sound, 2048)
spectrogram = ea.get_spectrogram(fs, sound_log, 2048)

# %% play sound
wavfile.write('sound.wav', fs, np.int16(sound * 2**15))
os.system('play sound.wav')

# %% play sound
wavfile.write('sound_log.wav', fs, np.int16(sound_log * 2**15))
os.system('play sound_log.wav')
