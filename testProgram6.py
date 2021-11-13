# To Control the other programs volume, use pyaudio

import pyaudio
import wave
import sys

CHUNK = 1024

if len(sys.argv) < 2:

    print("Plays a .wav file. \n\n Usage: %s.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], "rb")
p = pyaudio.PyAudio()

stream = p.open()