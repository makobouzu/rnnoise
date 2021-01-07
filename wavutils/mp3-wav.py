#!/usr/bin/env python
import pydub
import sys
import glob

if __name__ == "__main__":
    args = sys.argv

    page_num = 300
    for page in range(page_num):
        page += 1
        print("page"+ page + ": change mp3 to wav")

        mp3_folder = glob.glob("page" + str(page) + "/*.mp3")
#        mp3_folder = glob.glob(args[1] + "/*.mp3")
        for file in mp3_folder:
            audio = pydub.AudioSegment.from_file(file)
            wav = file.split('.')[0] + ".wav"
            audio.export(wav, format='wav')
