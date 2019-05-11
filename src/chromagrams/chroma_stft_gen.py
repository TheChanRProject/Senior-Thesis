import numpy as np
!pip install pysoundfile
import soundfile as sf
from librosa.feature import chroma_stft

# Bhairav Block Wise Reading

## Bhairav 1

block_gen = sf.blocks('data/Hindustani/wav/Bhairav/bhairav1.wav', blocksize=1024, overlap=512)
rate = sf.info("data/Hindustani/wav/Bhairav/bhairav1.wav").samplerate

chromas = []

for bl in block_gen:
    y = np.mean(bl, axis=1)
    chromas.append(chroma_stft(y, sr=rate))

len(chromas)
print(chromas[1])
