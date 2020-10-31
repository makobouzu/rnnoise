#!/usr/bin/env python
#python 441kHz-48kHz.py input.wav output.wav
#Change input(mono 44.1kHz 16bit) wavfile -> output(mono 48kHz 16bit) wavfile

from fractions import Fraction

import numpy as np
import scipy as sp
import scipy.signal as sg
import soundfile as sf
import sys

if __name__ == "__main__":
    args = sys.argv
    
    fs_target = 48000
    cutoff_hz = 21000.0
    n_lpf = 4096

    sec = 60

    wav, fs_src = sf.read(args[1])
    wav_origin = wav[:fs_src * sec]

    frac = Fraction(fs_target, fs_src)

    up = frac.numerator
    down = frac.denominator

    # up sampling
    wav_up = np.zeros(np.alen(wav_origin) * up)
    wav_up[::up] = up * wav_origin
    fs_up = fs_src * up

    cutoff = cutoff_hz / (fs_up / 2.0)
    lpf = sg.firwin(n_lpf, cutoff)

    # filtering and down sampling
    wav_down = sg.lfilter(lpf, [1], wav_up)[n_lpf // 2::down]

    # write wave file
    sf.write(args[2], wav_down, fs_target)
