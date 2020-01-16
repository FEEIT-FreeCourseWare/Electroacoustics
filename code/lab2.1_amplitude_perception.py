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

Psychoacoustics - amplitude perception.

"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile
import os

# %% generate sound
f = 440
fs = 44100
ts = 1 / fs
t = np.arange(0, .05, ts)
sound = np.sin(2*np.pi*f*t)

# %% fade out
lin_fade = np.linspace(1, 0, sound.size)
log_fade = np.exp((lin_fade-1)/.2)

plt.figure()
plt.plot(t, lin_fade)
plt.plot(t, log_fade)
plt.grid()
plt.legend(['linear', 'exponential'])
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.show()

# %% apply fading
sound_lin = sound * lin_fade
sound_log = sound * log_fade

# %% plot sound
plt.figure()
plt.plot(t, sound, label=u'original')
plt.plot(t, sound_lin, label=u'linear')
plt.plot(t, sound_log, label=u'exponential')
plt.axis((0, t[-1], -1.1, 1.1))
plt.grid()
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# %% play sound
wavfile.write('sound.wav', fs, np.int16(sound * 2**15))
os.system('play sound.wav')

# %% play sound
wavfile.write('sound_lin.wav', fs, np.int16(sound_lin * 2**15))
os.system('play sound_lin.wav')

# %% play sound
wavfile.write('sound_log.wav', fs, np.int16(sound_log * 2**15))
os.system('play sound_log.wav')
