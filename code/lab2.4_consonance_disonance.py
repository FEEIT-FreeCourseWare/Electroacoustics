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

Psychoacoustics - music intervals and consonance/disonance.

"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile
import os

# %% generate sound
fs = 44100
ts = 1 / fs
t = np.arange(0, 4, ts)
c4 = 0.8 * np.sin(2*np.pi*261 * t)
c5 = 0.8 * np.sin(2*np.pi*261 * 2**(12/12)*t)
g4 = 0.8 * np.sin(2*np.pi*261 * 2**(7/12)*t)
f4 = 0.8 * np.sin(2*np.pi*261 * 2**(5/12)*t)
e4 = 0.8 * np.sin(2*np.pi*261 * 2**(4/12)*t)
d4 = 0.8 * np.sin(2*np.pi*261 * 2**(2/12)*t)
cis4 = 0.8 * np.sin(2*np.pi*261 * 2**(1/12)*t)
close = 0.8 * np.sin(2*np.pi*267 * t)

# %% generate music intervals
octave = (c4 + c5)/2
perfect_fifth = (c4 + g4)/2
perfect_fourth = (c4 + f4)/2
major_third = (c4 + e4)/2
major_second = (c4 + d4)/2
minor_second = (c4 + cis4)/2
beat = (c4 + close)/2

# %% plot sound
plt.figure()
plt.plot(t, octave)
plt.plot(t, perfect_fifth)
plt.plot(t, major_third)
plt.plot(t, major_second)
plt.grid()
plt.axis([0, .1, -1, 1])
plt.legend(['oct', 'quint', 'terz', 'sec'])

# %% play sounds
wavfile.write('octave.wav', fs, np.int16(octave * 2**15))
os.system('play octave.wav')

# %% play sounds
wavfile.write('perfect_fifth.wav', fs, np.int16(perfect_fifth * 2**15))
os.system('play perfect_fifth.wav')

# %% play sounds
wavfile.write('perfect_fourth.wav', fs, np.int16(perfect_fourth * 2**15))
os.system('play perfect_fourth.wav')

# %% play sounds
wavfile.write('major_third.wav', fs, np.int16(major_third * 2**15))
os.system('play major_third.wav')

# %% play sounds
wavfile.write('major_second.wav', fs, np.int16(major_second * 2**15))
os.system('play major_second.wav')

# %% play sounds
wavfile.write('minor_second.wav', fs, np.int16(minor_second * 2**15))
os.system('play minor_second.wav')

# %% play sounds
wavfile.write('beat.wav', fs, np.int16(beat * 2**15))
os.system('play beat.wav')
