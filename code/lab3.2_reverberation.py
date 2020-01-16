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

Measuring reverberation.

"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile
import scipy.signal as sig
import os
import ea

# %% generate sine sweep
fs = 44100
ts = 1 / fs
T = 4
t = np.arange(0, T, ts)
f_l = 100
f_h = 1e4
w_l = 2*np.pi*f_l
w_h = 2*np.pi*f_h
r_w = np.log(w_l/w_h)
sweep = np.sin(w_l*T/r_w * (np.exp(-t*r_w/T) - 1))

# %% plot sound
plt.figure()
plt.plot(t, sweep)
plt.axis((0, .06,-1,1))
plt.grid()

# %% plot spectrum
f, spec = ea.get_spectrum(fs, sweep)
plt.figure()
plt.plot(f, spec)
plt.xscale('log')
plt.axis((100, 1e4,-60,-20))
plt.grid()

# %% plot spectrogram
spectrogram = ea.get_spectrogram(fs, sweep, 2048)

# %% play sound
wavfile.write('sweep.wav', fs, np.int16(sweep * 2**15))
os.system('play sweep.wav')

# %% generate inverse
th_m = -T/r_w * np.exp(t*r_w/T)
modulation = np.sin(th_m)
inverse = sweep[::-1] * modulation

# %% plot spectrum
f, spec_inv = ea.get_spectrum(fs, inverse)
plt.figure()
plt.plot(f, spec_inv)
plt.xscale('log')
plt.axis((100, 1e4, -80, -40))
plt.grid()

# %% plot spectrogram
spectrogram_rev = ea.get_spectrogram(fs, inverse, 2048)

# %% record and load reverb_log
fs, reverb_log = wavfile.read('audio/reverb_log.wav')
reverb_log = reverb_log / 2**15
t_frames, f, spec_reverb = ea.get_spectrogram(fs, reverb_log, 2048)
plt.axis([0, t_frames[-1], 0, 10e3])

# %% convolve
room_response = sig.convolve(reverb_log, inverse)

# %% plot sound
plt.figure()
plt.plot(room_response)
plt.grid()

# %% isolate impulse response
room_response = room_response / np.max(np.abs(room_response))
max_ind = np.argmax(room_response)
t_minus = 0.01  # s
t_plus = 1  # s
room_response_trimmed = room_response[
    int(max_ind - t_minus*fs): int(max_ind + t_plus*fs)
    ]

# %% time domain in dB
plt.figure()
t = np.arange(0, room_response_trimmed.size/fs, ts)
plt.plot(t, 20*np.log10(room_response_trimmed))

# %% transfer function (spectrum)
f, transfer_func = ea.get_spectrum(fs, room_response_trimmed)
plt.figure()
plt.plot(f, transfer_func)
plt.xscale('log')

# %% spectrogram
t_frame, f, frames_spec = ea.get_spectrogram(fs, room_response_trimmed, 2048)

# %% waterfall diagram
from mpl_toolkits.mplot3d import axes3d
fig = plt.figure()
ax = fig.gca(projection='3d')
X, Y = np.meshgrid(t_frame, np.log10(f[:512]))
ax.plot_wireframe(X, Y, frames_spec[:512, :], rstride=0, cstride=4)

# %% play impulse response
wavfile.write('room_response.wav', fs, np.int16(room_response_trimmed * 2**15))
os.system('play room_response.wav')
