import os
import numpy as np
import soundfile as sf
from librosa.feature import chroma_stft
from librosa.display import specshow
import matplotlib.pyplot as plt
yaman_files = os.listdir("data/Hindustani/wav/Yaman")
print(yaman_files)

chroma_dict = {}
for j,yaman_file in enumerate(yaman_files):
    rate = sf.info(f"data/Hindustani/wav/Yaman/yaman{j+1}.wav").samplerate
    block_gen = sf.blocks(f"data/Hindustani/wav/Yaman/yaman{j+1}.wav", blocksize=rate*60)
    chroma_dict[f"yaman{j+1}"] = []

    for bl in block_gen:
        y = np.mean(bl, axis=1)
        chroma_dict[f"yaman{j+1}"].append(chroma_stft(y, sr=rate))

    for k, chroma in enumerate(chroma_dict[f"yaman{j+1}"]):
        specshow(chroma, x_axis="time", y_axis="chroma", vmin=0, vmax=1)
        plt.title(f"Chromagram of Yaman{j+1}_{k+1}")
        plt.savefig(f"data/chroma_files/yaman-chromas/yaman{j+1}/yaman{j+1}_{k+1}.png") 
