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
import os

#%% generate sound
f = 12000
fs = 44100
ts = 1 / fs
t = np.arange(0, 1, ts)
sound = np.sin(2*np.pi*f*t)

#%% plot sound
#plt.figure()
#plt.plot(t, sound)

#%% play sound
wavfile.write('sound.wav',fs ,
              np.array(sound * 2**15,
                       dtype='int16'))
os.system('play sound.wav')
