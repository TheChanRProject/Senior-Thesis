import os
import numpy as np
from librosa import load, stft, amplitude_to_db, power_to_db
from librosa.feature import melspectrogram, chroma_cqt, tonnetz
from librosa.display import specshow, waveplot
import matplotlib.pyplot as plt

sampFile = os.listdir("data/Hindustani/mp3/Bhairav")

my_file = f"data/Hindustani/mp3/Bhairav/{sampFile[0]}"

y, sr = load(my_file)

D = np.abs(stft(y))

specshow(amplitude_to_db(D, ref=np.max), y_axis='log', x_axis='time')
plt.title("Power Spectrogram")
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()

chroma_cq = chroma_cqt(y=y,sr=sr)
specshow(chroma_cq, y_axis='chroma', x_axis='time')
plt.title("Chromagram Constant Q Transform")
plt.colorbar()
plt.tight_layout()

tonnetz = tonnetz(y=y, sr=sr)
specshow(tonnetz, y_axis='tonnetz')
plt.title("Tonnetz Example")
plt.colorbar()
plt.tight_layout()

ms = melspectrogram(y=y, sr=sr)
specshow(power_to_db(ms, ref=np.max), y_axis='mel', fmax=8000, x_axis='time')
plt.title("Mel Spectrogram Example")
plt.colorbar(format="%+2.0f dB")
plt.tight_layout()

waveplot(y=y, sr=sr)
plt.title("Audio Waveplot")
plt.tight_layout()
