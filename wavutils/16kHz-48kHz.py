# -*- coding:utf-8 -*-
#python 16kHz-48kHz.py input.wav output.wav
#Change input(mono 16kHz 16bit) wavfile -> output(mono 48kHz 16bit) wavfile

import numpy as np
import scipy.signal
import wave
import array
import struct
import sys
import glob

def readWav(filename):
    try:
        wf = wave.open(filename)
        fs = wf.getframerate()
        data = np.frombuffer(wf.readframes(wf.getnframes()),dtype="int16")/32768.0
        return (data,fs)
    except Exception as e:
        print(e)
        exit()

def writeWav(filename,data,fs):
    data = [int(x * 32767.0) for x in data]
    binwave = struct.pack("h" * len(data), *data)
    wf = wave.Wave_write(filename)
    wf.setparams((
                    1,                          # channel
                    2,                          # byte width
                    fs,                         # sampling rate
                    len(data),                  # number of frames
                    "NONE", "not compressed"    # no compression
                ))
    wf.writeframes(binwave)
    wf.close()

def upsampling(conversion_rate,data,fs):
    interpolationSampleNum = conversion_rate-1

    # FIR filter
    nyqF = (fs*conversion_rate)/2.0
    cF = (fs/2.0-500.)/nyqF
    taps = 511
    b = scipy.signal.firwin(taps, cF)

    upData = []
    for d in data:
        upData.append(d)
        for i in range(interpolationSampleNum):
            upData.append(0.0)

    resultData = scipy.signal.lfilter(b,1,upData)
    return (resultData,fs*conversion_rate)

if __name__ == "__main__":
    args = sys.argv
    up_conversion_rate = 3
    
    folder = glob.glob(args[1] + "/*.wav")
    for file in folder:
        data,fs = readWav(file)
        upData,upFs = upsampling(up_conversion_rate,data,fs)
        writeWav(file,upData,upFs)
        print("resample 16kHz -> 48kHz : " + file)
