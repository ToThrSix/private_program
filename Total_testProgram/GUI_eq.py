import numpy as np
from matplotlib import pyplot as plt
import soundfile as sf
from scipy import signal as sn

data, samplerate = sf.read(
    'C:\\Users\\NK22\\Downloads\\keys-of-moon-warm-memories.mp3')

print(
    f'File Info : Play Time : {len(data)/samplerate}, Samplerate : {samplerate}')


def calc_stft(nperseg):
    freq, time, Zxx = sn.stft(
        data[:, 0], samplerate, nperseg=nperseg)
    # print(np.abs(Zxx))
    plt.plot(time, np.abs(Zxx[700]))
    # print(time)
    print(len(time))
    # plt.show()


20, 50, 100,

calc_stft(44100)
