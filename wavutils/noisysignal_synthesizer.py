# -*- coding:utf-8 -*-
#python noisysignal_synthesizer.py signal.wav noise.wav noisy_signal.wav
#input signal wav + noise.wav -> noisy_signal,wav
#@author: Makoto Amano 2020

import numpy as np
import soundfile as sf
import os
import sys
import configparser as CP

# Function to read audio
def audioread(path, norm = True, start=0, stop=None):
    x, sr = sf.read(path, start=start, stop=stop)

    if len(x.shape) == 1:  # mono
        if norm:
            rms = (x ** 2).mean() ** 0.5
            scalar = 10 ** (-25 / 20) / (rms)
            x = x * scalar
        return x, sr
    else:  # multi-channel
        x = x.T
        x = x.sum(axis=0)/x.shape[0]
        if norm:
            rms = (x ** 2).mean() ** 0.5
            scalar = 10 ** (-25 / 20) / (rms)
            x = x * scalar
        return x, sr
    
# Funtion to write audio
def audiowrite(data, fs, name, norm=False):
    if norm:
        rms = (data ** 2).mean() ** 0.5
        scalar = 10 ** (-25 / 10) / (rms+eps)
        data = data * scalar
        if max(abs(data))>=1:
            data = data/max(abs(data), eps)
    sf.write(name, data, fs)
    return

# Function to mix clean speech and noise at various SNR levels
def snr_mixer(clean, noise, snr):
    # Normalizing to -25 dB FS
    rmsclean = (clean**2).mean()**0.5
    scalarclean = 10 ** (-25 / 20) / rmsclean
    clean = clean * scalarclean
    rmsclean = (clean**2).mean()**0.5

    rmsnoise = (noise**2).mean()**0.5
    scalarnoise = 10 ** (-25 / 20) /rmsnoise
    noise = noise * scalarnoise
    rmsnoise = (noise**2).mean()**0.5
    # Set the noise level for a given SNR
    noisescalar = np.sqrt(rmsclean / (10**(snr/20)) / rmsnoise)
    noisenewlevel = noise * noisescalar
    noisyspeech = clean + noisenewlevel
    return clean, noisenewlevel, noisyspeech

#-------------------------------------------------------------------------------
if __name__=="__main__":
    args = sys.argv
    snr_lower = float(0)
    snr_upper = float(40)
    total_snrlevels = float(5)
    SNR = np.linspace(int(snr_lower), int(snr_upper), int(total_snrlevels))
    
    #clean file
    cleanfilename = args[1]
    clean, fs = audioread(cleanfilename)
    
    #noise file
    noisefilename = args[2]
    noise, fs = audioread(noisefilename)
       
    
    clean_snr, noise_snr, noisy_snr = snr_mixer(clean=clean, noise=noise, snr=SNR[0])
    noisyfilename = args[3]
    audiowrite(noisy_snr, fs, noisyfilename, norm=False)
    print(noisyfilename)
