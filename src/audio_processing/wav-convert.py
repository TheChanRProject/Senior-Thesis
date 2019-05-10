import numpy as np
import soundfile as sf
from sksound.sounds import Sound
import os

desFiles = os.listdir("data/Hindustani/mp3/Des")


for file in desFiles:
    mySound = Sound(file)
    mySound.write_wav()
