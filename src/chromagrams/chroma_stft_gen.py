import numpy as np
!pip install pysoundfile
import soundfile as sf
from librosa.feature import chroma_stft
from librosa.display import specshow
import matplotlib.pyplot as plt
# Bhairav Block Wise Reading

## Bhairav 1

block_gen = sf.blocks('data/Hindustani/wav/Bhairav/bhairav1.wav', blocksize=2646000)
rate = sf.info("data/Hindustani/wav/Bhairav/bhairav1.wav").samplerate
info = sf.info("data/Hindustani/wav/Bhairav/bhairav1.wav")
print(info)
chromas = []

for bl in block_gen:
    y = np.mean(bl, axis=1)
    chromas.append(chroma_stft(y, sr=rate))

len(chromas)
for j, chroma in enumerate(chromas):
    specshow(chroma, x_axis="time", y_axis="chroma", vmin=0, vmax=1)
    plt.title(f"Chromagram of Bhairav1_{j}")
    plt.savefig(f"data/chroma_files/bhairav-chromas/bhairav1/bhairav1_{j}.png")



## Bhairav 2

block_gen = sf.blocks('data/Hindustani/wav/Bhairav/bhairav2.wav', blocksize=2646000)
rate = sf.info("data/Hindustani/wav/Bhairav/bhairav2.wav").samplerate
info = sf.info("data/Hindustani/wav/Bhairav/bhairav2.wav")
print(info)

chromas = []

for bl in block_gen:
    y = np.mean(bl, axis=1)
    chromas.append(chroma_stft(y, sr=rate))

len(chromas)
for j, chroma in enumerate(chromas):
    specshow(chroma, x_axis="time", y_axis="chroma", vmin=0, vmax=1)
    plt.title(f"Chromagram of Bhairav2_{j}")
    plt.savefig(f"data/chroma_files/bhairav-chromas/bhairav2/bhairav2_{j}.png")

## Bhairav 3

block_gen = sf.blocks('data/Hindustani/wav/Bhairav/bhairav3.wav', blocksize=2646000)
rate = sf.info("data/Hindustani/wav/Bhairav/bhairav3.wav").samplerate
info = sf.info("data/Hindustani/wav/Bhairav/bhairav3.wav")
print(info)
chromas = []

for bl in block_gen:
    y = np.mean(bl, axis=1)
    chromas.append(chroma_stft(y, sr=rate))

len(chromas)
for j, chroma in enumerate(chromas):
    specshow(chroma, x_axis="time", y_axis="chroma", vmin=0, vmax=1)
    plt.title(f"Chromagram of Bhairav1_{j}")
    plt.savefig(f"data/chroma_files/bhairav-chromas/bhairav3/bhairav3_{j}.png")

## Bhairav 4

block_gen = sf.blocks('data/Hindustani/wav/Bhairav/bhairav4.wav', blocksize=2646000)
rate = sf.info("data/Hindustani/wav/Bhairav/bhairav4.wav").samplerate
info = sf.info("data/Hindustani/wav/Bhairav/bhairav4.wav")
print(info)
chromas = []

for bl in block_gen:
    y = np.mean(bl, axis=1)
    chromas.append(chroma_stft(y, sr=rate))

len(chromas)
for j, chroma in enumerate(chromas):
    specshow(chroma, x_axis="time", y_axis="chroma", vmin=0, vmax=1)
    plt.title(f"Chromagram of Bhairav4_{j}")
    plt.savefig(f"data/chroma_files/bhairav-chromas/bhairav4/bhairav4_{j}.png")

## Bhairav 5

block_gen = sf.blocks('data/Hindustani/wav/Bhairav/bhairav5.wav', blocksize=2646000)
rate = sf.info("data/Hindustani/wav/Bhairav/bhairav5.wav").samplerate
info = sf.info("data/Hindustani/wav/Bhairav/bhairav5.wav")
print(info)
chromas = []

for bl in block_gen:
    y = np.mean(bl, axis=1)
    chromas.append(chroma_stft(y, sr=rate))

len(chromas)
for j, chroma in enumerate(chromas):
    specshow(chroma, x_axis="time", y_axis="chroma", vmin=0, vmax=1)
    plt.title(f"Chromagram of Bhairav5_{j}")
    plt.savefig(f"data/chroma_files/bhairav-chromas/bhairav5/bhairav5_{j}.png")

## Bhairav 6

block_gen = sf.blocks('data/Hindustani/wav/Bhairav/bhairav6.wav', blocksize=2646000)
rate = sf.info("data/Hindustani/wav/Bhairav/bhairav6.wav").samplerate
info = sf.info("data/Hindustani/wav/Bhairav/bhairav6.wav")
print(info)
chromas = []

for bl in block_gen:
    y = np.mean(bl, axis=1)
    chromas.append(chroma_stft(y, sr=rate))

len(chromas)
for j, chroma in enumerate(chromas):
    specshow(chroma, x_axis="time", y_axis="chroma", vmin=0, vmax=1)
    plt.title(f"Chromagram of Bhairav6_{j}")
    plt.savefig(f"data/chroma_files/bhairav-chromas/bhairav6/bhairav6_{j}.png")

## Bhairav 7

block_gen = sf.blocks('data/Hindustani/wav/Bhairav/bhairav7.wav', blocksize=2646000)
rate = sf.info("data/Hindustani/wav/Bhairav/bhairav7.wav").samplerate
info = sf.info("data/Hindustani/wav/Bhairav/bhairav7.wav")
print(info)
chromas = []

for bl in block_gen:
    y = np.mean(bl, axis=1)
    chromas.append(chroma_stft(y, sr=rate))

len(chromas)
for j, chroma in enumerate(chromas):
    specshow(chroma, x_axis="time", y_axis="chroma", vmin=0, vmax=1)
    plt.title(f"Chromagram of Bhairav7_{j}")
    plt.savefig(f"data/chroma_files/bhairav-chromas/bhairav7/bhairav7_{j}.png")

## Bhairav 8

block_gen = sf.blocks('data/Hindustani/wav/Bhairav/bhairav8.wav', blocksize=2646000)
rate = sf.info("data/Hindustani/wav/Bhairav/bhairav8.wav").samplerate
info = sf.info("data/Hindustani/wav/Bhairav/bhairav8.wav")
print(info)
chromas = []

for bl in block_gen:
    y = np.mean(bl, axis=1)
    chromas.append(chroma_stft(y, sr=rate))

len(chromas)
for j, chroma in enumerate(chromas):
    specshow(chroma, x_axis="time", y_axis="chroma", vmin=0, vmax=1)
    plt.title(f"Chromagram of Bhairav8_{j}")
    plt.savefig(f"data/chroma_files/bhairav-chromas/bhairav8/bhairav8_{j}.png")

## Bhairav 9

block_gen = sf.blocks('data/Hindustani/wav/Bhairav/bhairav9.wav', blocksize=2646000)
rate = sf.info("data/Hindustani/wav/Bhairav/bhairav9.wav").samplerate
info = sf.info("data/Hindustani/wav/Bhairav/bhairav9.wav")
print(info)
chromas = []

for bl in block_gen:
    y = np.mean(bl, axis=1)
    chromas.append(chroma_stft(y, sr=rate))

len(chromas)
for j, chroma in enumerate(chromas):
    specshow(chroma, x_axis="time", y_axis="chroma", vmin=0, vmax=1)
    plt.title(f"Chromagram of Bhairav9_{j}")
    plt.savefig(f"data/chroma_files/bhairav-chromas/bhairav9/bhairav9_{j}.png")

## Bhairav 10

block_gen = sf.blocks('data/Hindustani/wav/Bhairav/bhairav10.wav', blocksize=2646000)
rate = sf.info("data/Hindustani/wav/Bhairav/bhairav10.wav").samplerate
info = sf.info("data/Hindustani/wav/Bhairav/bhairav10.wav")
print(info)
chromas = []

for bl in block_gen:
    y = np.mean(bl, axis=1)
    chromas.append(chroma_stft(y, sr=rate))

len(chromas)
for j, chroma in enumerate(chromas):
    specshow(chroma, x_axis="time", y_axis="chroma", vmin=0, vmax=1)
    plt.title(f"Chromagram of Bhairav10_{j}")
    plt.savefig(f"data/chroma_files/bhairav-chromas/bhairav10/bhairav10_{j}.png")
