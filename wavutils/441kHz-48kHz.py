#!/usr/bin/env python
#python 441kHz-48kHz.py input.wav output.wav
#Change input(mono 44.1kHz 16bit) wavfile -> output(mono 48kHz 16bit) wavfile

from fractions import Fraction

import numpy as np
import scipy as sp
import scipy.signal as sg
import soundfile as sf
import sys
import glob

if __name__ == "__main__":
    args = sys.argv
    
    fs_target = 48000
    cutoff_hz = 21000.0
    n_lpf = 4096

    sec = 60
    
    folder = glob.glob(args[1] + "/*.wav")
    for file in folder:
        wav, fs_src = sf.read(file)
        wav_origin = wav[:fs_src * sec]
        frac = Fraction(fs_target, fs_src)
        up = frac.numerator
        down = frac.denominator
        wav_up = np.zeros(np.alen(wav_origin) * up)
        wav_up[::up] = up * wav_origin
        fs_up = fs_src * up
        cutoff = cutoff_hz / (fs_up / 2.0)
        lpf = sg.firwin(n_lpf, cutoff)
        wav_down = sg.lfilter(lpf, [1], wav_up)[n_lpf // 2::down]
        sf.write(file, wav_down, fs_target)
        print("resample 44.1kHz -> 48kHz : " + file)
