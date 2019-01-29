# -*- coding: utf-8 -*-
"""
Created on Nov 23 2016

@author: Branislav Gerazov

Copyright 2016 by Branislav Gerazov

See the file LICENSE for the license associated with this software.
"""
from __future__ import division
import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile
import os

#%% generate sound
f = 440
fs = 44100
ts = 1 / fs
t = np.arange(0, .05, ts)
sound = np.sin(2*np.pi*f*t)

#%% fade out
lin_fade = np.linspace(1, 0, sound.size)
log_fade = np.exp((lin_fade-1)/.2)

import matplotlib as mpl
from matplotlib import rc
mpl.rcdefaults() # cбрасываем настройки на "по умолчанию"
#mpl.rcParams['font.family'] = 'fantasy'
#mpl.rcParams['font.fantasy'] = 'CMU Serif'
font = {'family': 'CMU Serif',
        'weight': 'normal',
        'size': 16}
rc('font', **font)


plt.figure()
plt.plot(t, lin_fade)
plt.plot(t, log_fade)
plt.grid()
#plt.legend(['linear','exponential'])
#plt.show()
st = u'Време [s]'
plt.xlabel(st)
st = u'Амплитуда'
plt.ylabel(st)
plt.show()

#%%
sound_lin = sound * lin_fade
sound_log = sound * log_fade

#%% plot sound
#import matplotlib.font_manager
#print matplotlib.font_manager.findSystemFonts(fontpaths=None)
##%%
plt.figure()
plt.plot(t, sound, label=u'оригинален')
plt.plot(t, sound_lin, label=u'линеарно втишување')
plt.plot(t, sound_log, label=u'експоненцијално втишување')
plt.axis((0,t[-1],-1.1,1.1))
#plt.legend()
plt.grid()
plt.show()
st = u'Време [s]'
plt.xlabel(st)
st = u'Амплитуда'
plt.ylabel(st)
plt.show()

#%% play sound
#wavfile.write('sound.wav',fs ,
#              np.array(sound * 2**15,
#                       dtype='int16'))
#os.system('play sound.wav')
#
##%% play sound
#wavfile.write('sound_lin.wav',fs ,
#              np.array(sound_lin * 2**15,
#                       dtype='int16'))
#os.system('play sound_lin.wav')
#
##%% play sound
#wavfile.write('sound_log.wav',fs ,
#              np.array(sound_log * 2**15,
#                       dtype='int16'))
#os.system('play sound_log.wav')
#
