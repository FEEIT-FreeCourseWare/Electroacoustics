# -*- coding: utf-8 -*-
#
# Copyright 2016 by Branislav Gerazov
#
# See the file LICENSE for the license associated with this software.
#
# Author(s):
#   Branislav Gerazov, Nov 2016

"""
Electroacoustics

Utility functions.

"""
import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sig
import scipy.fftpack as ffp
from scipy.io import wavfile
import os


def gen_sound(f=200, t_end=1, fs=44100):
    t = np.arange(0, t_end * fs) / fs
    sound = np.sin(2 * np.pi * f * t)
    wavfile.write('sound.wav', fs, np.int16(sound*2**15))
    os.system('play sound.wav')


def get_spectrum(fs, wav):
    n = wav.size
    n_fft = 2**np.ceil(np.log(n)/np.log(2))
    n_fft = int(n_fft)
    wav_spec = ffp.fft(wav, n_fft)
    wav_amp = np.abs(wav_spec)
    wav_amp = wav_amp[0: n_fft//2+1]
    wav_amp = wav_amp / n
    wav_amp[1: -1] = wav_amp[1: -1] * 2
    wav_amp = 20*np.log10(wav_amp)
    f = np.linspace(0, fs/2, n_fft//2+1)
    return f, wav_amp


def get_spectrogram(fs, wav, n_win=512):
    m = wav.size
    t = np.arange(0, m/fs, 1/fs)
    nh = int(n_win/2)
    h = int(n_win/2)  # hop size
    win = sig.get_window('hamming', n_win)
    t_frame = np.arange(0, t[-1], h/fs)
    # windowing
    poz = nh  # pozicija na sredinata na prozorecot
    pad = np.zeros(nh)
    wav_pad = np.concatenate((pad, wav, pad))
    m = m + n_win  # wav_pad length
    while poz < m-nh:
        frame = wav_pad[poz-nh: poz+nh] * win
        f_frame, frame_spec = get_spectrum(fs, frame)
        if poz == nh:
            frames_spec = np.array([frame_spec]).T
        else:
            frames_spec = np.hstack((frames_spec, np.array([frame_spec]).T))
        poz += h

    plt.figure()
    plt.imshow(
        frames_spec, aspect='auto',
        origin='lower',
        extent=[0, t[-1], 0, f_frame[-1]],
        vmin=-100, vmax=0, cmap='viridis'
        )
    cbar = plt.colorbar()
    plt.xlabel('Time [s]')
    plt.ylabel('Frequency [Hz]')
    cbar.ax.set_ylabel('Amplitude [dBFS]')
    plt.axis([0, t[-1], 0, 10000])
    return t_frame, f_frame, frames_spec
