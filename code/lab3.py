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
#f = 440
fs = 44100
ts = 1 / fs
T = 4
t = np.arange(0, T, ts)
#sound = sig.chirp(t, 100, t[-1] ,10000)
#sound_log = sig.chirp(t, 100, t[-1] ,10000, method='logarithmic')

##%% plot sound
#plt.figure()
#plt.plot(t, sound)
#
##%% plot spectrum
#f, spec_log = ea.get_spectrum(fs, sound_log)
#plt.figure()
#plt.plot(f, spec_log)
#plt.xscale('log')
#plt.axis((100, 1e4,-60,-20))
#plt.grid()
#
##%% plot spectrogram
#spectrogram = ea.get_spectrogram(fs, sound_log, 2048)
#
##%% play sound
#wavfile.write('sound_log.wav',fs ,
#              np.array(sound_log * 2**15,
#                       dtype='int16'))
##os.system('play sound_log.wav')
#
#%% analysis
#fs, reverb_log = wavfile.read('reverb_log.wav')
#reverb_log = reverb_log / 2**15
#t = np.arange(0, reverb_log.size/fs, 1/fs)
#plt.figure()
#plt.plot(t, reverb_log)
#plt.grid()
#
##%%
#spectrogram_rev = ea.get_spectrogram(fs, reverb_log, 2048)
#
##%% construct inverse filter
#inverse = sound_log[::-1]
#
##%% plot spectrum
#f, spec_inv = ea.get_spectrum(fs, inverse)
#plt.figure()
#plt.plot(f, spec_inv)
#plt.xscale('log')
#plt.axis((100, 1e4,-60,-20))
#plt.grid()

#%% add ramp
f_l = 100
f_h = 1e4
w_l = 2*np.pi*f_l
w_h = 2*np.pi*f_h
r_w = np.log(w_l/w_h)
#L = T / np.log(w_l/w_h)
#K = w_l * L
t = np.arange(0, T, ts)
#sweep = np.sin(K*(np.exp(-t/L) - 1))
sweep = np.sin(w_l*T/r_w *(np.exp(-t*r_w/T) - 1))

#%% plot sound
plt.figure()
plt.plot(t, sweep)
plt.axis((0, .9,-1,1))
plt.grid()
#plt.xlabel(')
#%% plot spectrum
f, spec_log = ea.get_spectrum(fs, sweep)
plt.figure()
plt.plot(f, spec_log)
plt.xscale('log')
plt.axis((100, 1e4,-60,-20))
plt.grid()

#%% plot spectrogram
spectrogram = ea.get_spectrogram(fs, sweep, 2048)

#%% play sound
wavfile.write('sweep.wav',fs ,
              np.array(sweep * 2**15,
                       dtype='int16'))
#os.system('play sweep.wav')


#


#%% inverse
th_m = -T/r_w * np.exp(t*r_w/T)
#th_m = -T/r_w * np.exp(-t*r_w/T)
#modulation = np.sin(1/np.exp(t/L))
modulation = np.sin(th_m)
#modulation = np.sin(th_m)

##%% plot spectrum
#f, spec_log = ea.get_spectrum(fs, modulation)
#plt.figure()
#plt.plot(f, spec_log)
#plt.xscale('log')
##plt.axis((100, 1e4,-100,-0))
#plt.xaxis('Frequency [Hz]')
##plt.grid()
#%%
inverse = sweep[::-1] * modulation
#% plot sound
plt.figure()
plt.plot(t, inverse)
#plt.axis((0, .09,-1,1))
plt.grid()
#plt.xlabel(')

#%%
#plt.figure()
#plt.plot(t, sweep)
#spectrogram_rev = ea.get_spectrogram(fs, modulation, 2048)
spectrogram_rev = ea.get_spectrogram(fs, inverse, 2048)
#%% plot spectrum
f, spec_inv = ea.get_spectrum(fs, inverse)
plt.figure()
plt.plot(f, spec_inv)
#plt.plot(t,w)
plt.xscale('log')
plt.xlabel('Frequency [Hz]')
plt.axis((100, 1e4,-80,-50))
plt.grid()

#import scipy.fftpack as ffp
#N = inverse.size
#Nfft = 2**np.ceil(np.log(N)/np.log(2))
#wav_spec = ffp.fft(inverse, Nfft)
#wav_amp = np.abs(wav_spec)
#wav_amp = wav_amp[0:Nfft/2+1]
#wav_amp = wav_amp / N
#wav_amp[1:-1] = wav_amp[1:-1] * 2
#wav_amp = 20*np.log10(wav_amp)
#f = np.linspace(0, fs/2, Nfft/2+1)
#return f, wav_amp


#%% analysis
#fs, reverb_log = wavfile.read('reverb_log.wav')
fs, reverb_log = wavfile.read('reverb_lab.wav')
reverb_log = reverb_log / 2**15
t = np.arange(0, reverb_log.size/fs, 1/fs)
plt.figure()
plt.plot(t, reverb_log)
plt.grid()

#%%
spectrogram_rev = ea.get_spectrogram(fs, reverb_log, 2048)
#

#%% convolve
room_response = sig.convolve(reverb_log, inverse)
#%% plot sound
plt.figure()
t = np.arange(0, room_response.size/fs, ts)
plt.plot(t, room_response)
#plt.axis((3, 5,-50,50))
plt.axis((1.5, 6.5,-50,50))
plt.grid()
plt.xlabel('Time [s]')
#%% sredi
room_response = room_response / np.max(np.abs(room_response))
max_ind = np.argmax(room_response)
t_minus = 0.01
t_plus = 3
room_response_trimmed = room_response[max_ind - int(t_minus*fs) :
                                        max_ind + np.min((int(t_plus*fs),
                                                          room_response.size))]


#%%
plt.figure()
t = np.arange(0, room_response_trimmed.size/fs, ts)
plt.plot(t, 20*np.log10(room_response_trimmed))
#plt.axis((0,room_response.size,-1,1))
#plt.plot(error)
plt.grid()
plt.axis((0, 1,-80,0))
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [dB]')

#%% spectrum
f, transfer_func = ea.get_spectrum(fs, room_response_trimmed)
plt.figure()
plt.plot(f, transfer_func)
plt.xscale('log')
plt.axis((100, 1e4,-80,-30))
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')
plt.grid()

#%%
t_frame, f, frames_spec = ea.get_spectrogram(fs, room_response_trimmed, 2048)


#%%
wavfile.write('room_response.wav',fs ,
              np.array(room_response_trimmed * 2**15,
                       dtype='int16'))
os.system('play room_response.wav')



#%% use deconvolve
from mpl_toolkits.mplot3d import axes3d
#room_response, error = sig.deconvolve(reverb_log, sound_log)
fig = plt.figure()
ax = fig.gca(projection='3d')
#X, Y = np.meshgrid(t_frame, f[:512])
X, Y = np.meshgrid(t_frame, np.log10(f[:512]))
frames_spec[frames_spec < -90] = -90
#ax.set_yscale('log')
#ax.yaxis.set_scale('log')
ax.plot_wireframe(X, Y, frames_spec[:512,:], rstride=0, cstride=4)
yticks = [100, 1000, 10000]
ax.set_yticks(np.log(yticks))
ax.set_yticks([])
ax.set_xticks([])
ax.set_zticks([])

ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_zticklabels([])
#ax.set_ylabel('Frequency [Hz]')
#ax.set_xlabel('Time [s]')
#ax.set_zlabel('Amplitude [dB]')

#ax.set_yticklabels(f[:512])
#ax.set_zlim(-100, 0)
#ax.set_xlim(0, t_frame[-1])
#ax.set_ylim(0, 1e4)
