#!/usr/bin/env python2
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

@author: Branislav Gerazov
"""
from __future__ import division
import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sig 
import scipy.fftpack as ffp
from scipy.io import wavfile
import os 
import matplotlib as mpl
from matplotlib import rc


def gen_sound(f=200, t_end=1, fs=44100):
    t = np.arange(0, t_end*fs) / fs
    sound = np.sin(2*np.pi*f*t)
    wavfile.write('sound.wav',fs, np.array(sound*2**15, dtype='int16'))
    os.system('play sound.wav')

def get_spectrum(fs, wav):
    N = wav.size
    Nfft = 2**np.ceil(np.log(N)/np.log(2))
    Nfft = int(Nfft)
    wav_spec = ffp.fft(wav, Nfft)
    wav_amp = np.abs(wav_spec)
    wav_amp = wav_amp[0:Nfft//2+1]
    wav_amp = wav_amp / N
    wav_amp[1:-1] = wav_amp[1:-1] * 2
    wav_amp = 20*np.log10(wav_amp)
    f = np.linspace(0, fs/2, Nfft//2+1)
    return f, wav_amp

def get_spectrogram(fs, wav, N=512):
    M = wav.size
    t = np.arange(0, M/fs, 1/fs)
    Nh = int(N/2)
    H = int(N/2)  # hop size
    win = sig.get_window('hamming',N)
    t_frame = np.arange(0,t[-1],H/fs)
    # windowing
    poz = Nh  # pozicija na sredinata na prozorecot
    pad = np.zeros(Nh)
    wav_pad = np.concatenate((pad, wav, pad))
    M = M + N  # wav_pad length
    while poz < M-Nh:
        frame = wav_pad[poz-Nh : poz+Nh] * win
        f_frame, frame_spec = get_spectrum(fs, frame)
        if poz == Nh:
            frames_spec = np.array([frame_spec]).T
        else:
            frames_spec = np.hstack((frames_spec,\
                          np.array([frame_spec]).T))
        poz += H                      

#    # plot
##    mpl.rcdefaults() # cбрасываем настройки на "по умолчанию"
#    #mpl.rcParams['font.family'] = 'fantasy'
#    #mpl.rcParams['font.fantasy'] = 'CMU Serif'
#    font = {'family': 'CMU Serif',
#            'weight': 'normal', 
#            'size': 16}
#    rc('font', **font)
    plt.figure()
    plt.imshow(frames_spec, aspect='auto', \
               origin='lower', \
               extent=[0, t[-1], 0, f_frame[-1]],\
               vmin=-100,vmax=0, cmap='viridis')
    cbar = plt.colorbar()
#    st = u'Време [s]'
#    plt.xlabel(st)
#    st = u'Фреквенција [Hz]'
#    plt.ylabel(st)
#    st = u'Амплитуда [dB]'
#    cbar.ax.set_ylabel(st)
    plt.xlabel('Time [s]')
    plt.ylabel('Frequency [Hz]')
    cbar.ax.set_ylabel('Amplitude [dBFS]')
    plt.axis([0, t[-1], 0, 10000])    
    return t_frame, f_frame, frames_spec