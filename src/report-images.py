import os
import numpy as np
from librosa import load, stft, amplitude_to_db
from librosa.feature import melspectrogram, chroma_cqt, tonnetz
from librosa.display import specshow
import matplotlib.pyplot as plt

sampFile = os.listdir("data/Hindustani/mp3/Bhairav")

my_file = f"data/Hindustani/mp3/Bhairav/{sampFile[0]}"

y, sr = load(my_file)

D = np.abs(stft(y))

specshow(amplitude_to_db(D, ref=np.max), y_axis='log', x_axis='time')
plt.title("Power Spectrogram")
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()
