import numpy as np
import soundfile as sf
from sksound.sounds import Sound
import os

desFiles = os.listdir("data/Hindustani/mp3/Des")


mySound = Sound(desFiles[0])
mySound.write_wav("data/Hindustani/wav/Des/des1.wav")


mySound = Sound(desFiles[1])
mySound.write_wav("data/Hindustani/wav/Des/des2.wav")

mySound = Sound(desFiles[2])
mySound.write_wav("data/Hindustani/wav/Des/des3.wav")

mySound = Sound(desFiles[3])
mySound.write_wav("data/Hindustani/wav/Des/des4.wav")

mySound = Sound(desFiles[4])
mySound.write_wav("data/Hindustani/wav/Des/des5.wav")

mySound = Sound(desFiles[5])
mySound.write_wav("data/Hindustani/wav/Des/des6.wav")

mySound = Sound(desFiles[6])
mySound.write_wav("data/Hindustani/wav/Des/des7.wav")

mySound = Sound(desFiles[7])
mySound.write_wav("data/Hindustani/wav/Des/des8.wav")

mySound = Sound(desFiles[8])
mySound.write_wav("data/Hindustani/wav/Des/des9.wav")

mySound = Sound(desFiles[9])
mySound.write_wav("data/Hindustani/wav/Des/des10.wav")
