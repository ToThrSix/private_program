import numpy as np
from matplotlib import pyplot as plt
import soundfile as sf
from scipy import signal as sn

data, samplerate = sf.read(
    'C:\\Users\\NK22\\Downloads\\02 - Sam Houghton and Joe Collinson - The Rhythm King.mp3')

print(len(data))

print(
    f'File Info : Play Time : {len(data)/samplerate}, Samplerate : {samplerate}')

'''
def calc_stft(nperseg):
    freq, time, Zxx = sn.stft(data[:, 0], samplerate, nperseg=nperseg)
    plt.pcolormesh(time, freq, np.abs(Zxx), vmin=0,
                   vmax=0.003, shading='gouraud')
    plt.ylim([20, 20000])
    plt.show()


calc_stft(4800)
'''

'''
def calc_stft(i, nperseg):
    freq, time, Zxx = sn.stft(
        data[i*480:(i+1)*480, 0], samplerate, nperseg=nperseg)
    plt.pcolormesh(time + 0.01*i, freq, np.abs(Zxx), vmin=0,
                   vmax=0.01, shading='gouraud')
    plt.ylim([20, 20000])
    plt.show
    plt.pause(0.01)
    plt.clf()


for j in range(0, int(5584896/480), 1):
    calc_stft(j, 480)
'''


def calc_stft(i, nperseg):
    freq, time, Zxx = sn.stft(
        data[i*2400:(i+1)*2400, 0], samplerate, nperseg=nperseg*2)
    plt.pcolormesh(time + 0.05*i, freq, np.abs(Zxx)*100, vmin=0,
                   vmax=1, shading='gouraud')
    plt.show
    plt.pause(0.05)
    plt.clf()


for j in range(0, int(5584896/2400), 1):
    calc_stft(j, 2400)
