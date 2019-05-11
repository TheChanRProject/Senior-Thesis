import os
import numpy as np
import soundfile as sf
from librosa.feature import chroma_stft
from librosa.display import specshow
import matplotlib.pyplot as plt
bhup_files = os.listdir("data/Hindustani/wav/Bhup")
print(bhup_files)

for h,i in enumerate(bhup_files):
    os.system(f"mkdir data/chroma_files/bhup-chromas/bhup{h+1}")

chroma_dict = {}
for j in range(len(bhup_files)):
    rate = sf.info(f"data/Hindustani/wav/Bhup/bhup{j+1}.wav").samplerate
    block_gen = sf.blocks(f"data/Hindustani/wav/Bhup/bhup{j+1}.wav", blocksize=rate*60)
    chroma_dict[f"bhup{j+1}"] = []

    for bl in block_gen:
        y = np.mean(bl, axis=1)
        chroma_dict[f"bhup{j+1}"].append(chroma_stft(y, sr=rate))

    for k, chroma in enumerate(chroma_dict[f"bhup{j+1}"]):
        specshow(chroma, x_axis="time", y_axis="chroma", vmin=0, vmax=1)
        plt.title(f"Chromagram of Bhup{j+1}_{k+1}")
        plt.savefig(f"data/chroma_files/bhup-chromas/bhup{j+1}/bhup{j+1}_{k+1}.png")

    
