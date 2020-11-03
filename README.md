# RNNoise
A noise suppression library based on a recurrent neural network.

## Change

Output Noise Sound  

## Build

Prerequisite
* macOS: `brew install libsndfile libsoxr sox`
* Debian/Ubuntu: `sudo apt install libsndfile1-dev libsoxr-dev libsox-dev`

To compile, just type:
```shell
make
```

Sample noisy file `sample.wav` was included, and you can run `make check` to generate the processed one, `clean.wav`.

## Test

While it is meant to be used as a library, a simple command-line tool is
provided as an example. It can be used as:
```shell
examples/rnnoise_demo sample.wav output.wav
```
Sound file info:
- Samplerate: 48kHz
- Bitdepth: 16bit
- Channels: mono

## Training

### Audio feature extract

Build audio feature extraction tool
```shell
make src/denoise_training
```

Prepare signal.wav, noise.wav (ex. [microsoft/MS-SNSD](https://github.com/microsoft/MS-SNSD)) 
```shell
cd wavutils  
wav2pcm signal.wav signal.raw/signal.pcm
wav2pcm noise.wav noise.raw/noise.pcm
```

Use the tool `denoise_training` to get the audio feature array from speech and noise audio clip
```shell
src/denoise_training signal.raw noise.raw 500000 > training.f32
```
(note the matrix size and replace 500000 87 below)

### RNN model traning

Pick feature array to "training" dir and go through the training process.
```shell
cd training
python bin2hdf5.py ../src/training.f32 500000 87 training.h5
python rnn_train.py
python dump_rnn.py weights.hdf5 rnn_data.c rnn_data.txt orig
```

Training process will generate the RNN model weight code file (default is `rnn_data.c`) and layer definition header file (default is `rnn_data.h`).
They can be used to refresh the `src/rnn_data.c`, `src/rnn_data.h` and rebuild the rnnoise library and/or examples.

```shell
cd ../
mv training/rnn_data.c src/rnn_data.c
make clean
make
```

## License

`rnnoise` is freely redistributable under the revised BSD license.
Use of this source code is governed by a BSD-style license that can be found in the `COPYING` file.
