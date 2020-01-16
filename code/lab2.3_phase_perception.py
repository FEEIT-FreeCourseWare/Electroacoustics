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

Psychoacoustics - phase perception.

"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile
import os
import ea

# %% generate sound
f = 440
fs = 44100
ts = 1 / fs
t = np.arange(0, 1, ts)
sound_500 = 0.8 * np.sin(2*np.pi*t*500)
sound_1500 = 0.2 * np.sin(2*np.pi*t*1500)

# %% sum with different phase offset
sound_sum1 = sound_500 + sound_1500
sound_sum2 = sound_500 - sound_1500

# %% plot sound
plt.figure()
plt.plot(t, sound_500)
plt.plot(t, sound_1500)
plt.plot(t, sound_sum1)
plt.plot(t, sound_sum2)
plt.grid()
plt.axis([0, .005, -1, 1])
plt.legend(['500', '1500', 'sum1', 'sum2'])
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# %% plot spectrogram
spectrogram = ea.get_spectrogram(fs, sound_sum1, 2048)
spectrogram = ea.get_spectrogram(fs, sound_sum2, 2048)

# %% play sound
wavfile.write('sound_sum1.wav', fs, np.int16(sound_sum1 * 2**15))
os.system('play sound_sum1.wav')

# %% play sound
wavfile.write('sound_sum2.wav', fs, np.int16(sound_sum2 * 2**15))
os.system('play sound_sum2.wav')
