import numpy as np
import soundfile as sf
from sksound.sounds import Sound

mySound = Sound("data/Hindustani/mp3/Des/des1.mp3")
mySound.write_wav("data/Hindustani/wav/Des/des1.wav")
