# -*- coding: utf-8 -*-
from pydub import AudioSegment
import sys
import glob

if __name__ == "__main__":
#    args = sys.argv
#    folder = glob.glob(args[1] + "/*.mp3")
    page_num = 300
    for page in range(page_num):
        page += 8
        folder = glob.glob("page" + str(page) + "/*.mp3")
        for file_ in folder:
            sound = AudioSegment.from_file(file_)
            if sound.channels == 2:
                sound = sound.set_channels(1)
                sound.export(file_, format="mp3")
        print("page" + str(page) + ": change mono!")
