# -*- coding: utf-8 -*-
from pydub import AudioSegment
import sys
import glob


if __name__ == "__main__":
    args = sys.argv

    folder = glob.glob(args[1] + "/*.wav")
    initial = False
    for file in folder:
        soundfile = AudioSegment.from_file(file, "wav")
        if initial == False:
            soundfile.export(args[2], format = "wav")
            initial = True
        else:
            outfile = AudioSegment.from_file(args[2], "wav")
            sound = outfile + soundfile
            sound.export(args[2], format="wav")
            print("connect " + file)
