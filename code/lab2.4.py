#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 2016

@author: Branislav Gerazov

Copyright 2016 by Branislav Gerazov

See the file LICENSE for the license associated with this software.
"""
from __future__ import division
import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile
import scipy.signal as sig
import os
import ea

#%% generate sound
fs = 44100
ts = 1 / fs
t = np.arange(0, 4, ts)
f = 261
sound_C3 = 0.8 * np.sin(2*np.pi*t*f)
sound_C4 = 0.8 * np.sin(2*np.pi*t*2*f)  # oktava
sound_G3 = 0.8 * np.sin(2*np.pi*t*3/2*f)  # kvinta
sound_E3 = 0.8 * np.sin(2*np.pi*t*5/4*f)  # golema terca
sound_Cis3 = 0.8 * np.sin(2*np.pi*t*25/24*f)  # mala sekunda

#%%
sound_oct = (sound_C3 + sound_C4)/2
sound_quint = (sound_C3 + sound_G3)/2
sound_terz = (sound_C3 + sound_E3)/2
sound_sec = (sound_C3 + sound_Cis3)/2

#%% plot sound
plt.figure()
plt.plot(t, sound_oct)
plt.plot(t, sound_quint)
plt.plot(t, sound_terz)
plt.plot(t, sound_sec)
plt.grid()
plt.axis([0,.1,-1,1])
plt.legend(['oct','quint','terz','sec'])


#%% plot sound
plt.figure()
plt.plot(t, sound_oct)
plt.plot(t, sound_quint)
plt.plot(t, sound_terz)
plt.plot(t, sound_sec)
plt.grid()
plt.axis([0,.1,-1,1])
plt.legend(['oct','quint','terz','sec'])




##%%
#suma = np.array([sound_C3, sound_oct, sound_quint,sound_terz, sound_sec])
#suma = suma.ravel()
#spectrogram = ea.get_spectrogram(fs, suma, 2048)
#%% play sound
wavfile.write('sound_oct.wav',fs ,
              np.array(suma * 2**15,
                       dtype='int16'))
os.system('play sound_oct.wav')

#%% play sound
wavfile.write('sound_quint.wav',fs ,
              np.array(sound_quint * 2**15,
                       dtype='int16'))
os.system('play sound_quint.wav')

#%% play sound
wavfile.write('sound_terz.wav',fs ,
              np.array(sound_terz * 2**15,
                       dtype='int16'))
os.system('play sound_terz.wav')

#%% play sound
wavfile.write('sound_sec.wav',fs,
              np.array(sound_sec * 2**15,
                       dtype='int16'))
os.system('play sound_sec.wav')


#%%
sound_b = 0.8 * np.sin(2*np.pi*t*50/49*f)  # mala sekunda
sound_beat = (sound_C3 + sound_b)/2
plt.figure()
plt.plot(t, sound_beat)
plt.grid()
plt.axis([0,.4,-1,1])
st = u'Време [s]'
plt.xlabel(st)
st = u'Амплитуда'
plt.ylabel(st)
