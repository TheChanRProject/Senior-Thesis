import os
import numpy as np
import soundfile as sf
from librosa.feature import chroma_stft
from librosa.display import specshow
import matplotlib.pyplot as plt
des_files = os.listdir("data/Hindustani/wav/Des")
print(des_files)

for h,i in enumerate(des_files):
    os.system(f"mkdir data/chroma_files/des-chromas/des{h+1}")

chroma_dict = {}
for j in range(len(des_files)):
    rate = sf.info(f"data/Hindustani/wav/Des/des{j+1}.wav").samplerate
    block_gen = sf.blocks(f"data/Hindustani/wav/Des/des{j+1}.wav", blocksize=rate*60)
    chroma_dict[f"des{j+1}"] = []

    for bl in block_gen:
        y = np.mean(bl, axis=1)
        chroma_dict[f"des{j+1}"].append(chroma_stft(y, sr=rate))

    for k, chroma in enumerate(chroma_dict[f"des{j+1}"]):
        specshow(chroma, x_axis="time", y_axis="chroma", vmin=0, vmax=1)
        plt.title(f"Chromagram of Des{j+1}_{k+1}")
        plt.savefig(f"data/chroma_files/des-chromas/des{j+1}/des{j+1}_{k+1}.png")
