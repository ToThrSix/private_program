import numpy as np
import soundfile as sf
import cv2 as cv
import colorsys as cs
from scipy import signal as sn

width = 1024
height = 720
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)

thickness = -1
rect_w = 3
rect_h = 3
int_x = 3
int_y = 3
screen_start_x = 137
screen_start_y = 658

#data, samplerate = sf.read('music file name')

'''
def anal_mic_sig(nperseg):
    freq, time, Zxx = sn.stft(
        data[:, 0], samplerate, nperseg=nperseg)
'''


def GUI():

    # 각 주파수별 크기 계산 부분

    # 화면에 표시할 이퀄 설정
    for x in range(0, 250, 1):
        for y in range(0, 200, 1):

            start_x = screen_start_x + x * int_x
            start_y = screen_start_y - y * int_y
            cv.rectangle(img, (start_x, screen_start_y),
                         (start_x + rect_w, start_y + rect_h), (255, 255, 255), thickness)

    # 이퀄 화면 출력
    cv.imshow('Sample Title', img)
    cv.waitKey(0)


GUI()
