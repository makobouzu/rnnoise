# wavutils

wavutils is a tool set that process wav file. like follow:

```bash
bin/
├── pcm2wav - convert pcm to wav
├── wav2pcm - convert wav to pcm
└── wavinfo - show info of wav
```

## install

```bash
git clone https://github.com/smallmuou/wavutils
cd wavutils
sudo ./install.sh
```

## usage
* pcm2wav - convert pcm to wav

```bash
pcm2wav channel samplerate bitspersample pcmfile wavfile

# sample
pcm2wav 1 44100 16 audioSample/input.pcm output.wav
```

* wav2pcm - convert wav to pcm

```bash
wav2pcm wavfile pcmfile

#sample
pcm2wav audioSample/input.wav output.pcm
```

* wavinfo - show information of wav

```bash
wavinfo wavfile

#sample
wavinfo audioSample/input.wav

++++++++++++++++++++++++++++++++++++++++++++++
+          WAVEFORM INFORMATION              +
++++++++++++++++++++++++++++++++++++++++++++++
    Audio Format:   1 (0x0001)
    Num Channels:   1 (0x0002)
     Sample Rate:   44100 (0x0000ac44)
 Bits Per Sample:   16 (0x0010)
        PCM Size:   622592 (0x00098000)
```

* 16kHz-48kHz.py - convert wav(mono, 16kHz, 16bit) to wav(mono, 48kHz, 16bit)  

```bash
python 16kHz-48kHz.py folder

#sample
python 16kHz-48kHz.py audioSample/16kHz
```


* 441kHz-48kHz.py - convert wav(mono, 44.1kHz, 16bit) to wav(mono, 48kHz, 16bit)  

```bash
python 441kHz-48kHz.py folder

#sample
python 441kHz-48kHz.py audioSample/441kHz
```

* noisysignal_synthesizer.py - Create composite wav of signal.wav and noise.wav  

```bash
python noisysignal_synthesizer.py signal.wav noise.wav noisysignal.wav
```

* wav_connect.py - Combining wav files in a folder  

```bash
python wav_connect.py folder output.wav
```

## license

The script follow MIT license.
