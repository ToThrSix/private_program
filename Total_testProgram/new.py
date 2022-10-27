import numpy as np
import soundfile as sf
import cv2 as cv
import colorsys as cs
from scipy import signal as sn
import math as mt

width = 1024
height = 720
bpp = 3

thickness = -1
rect_w = 1
rect_h = 1
int_x = 3
int_y = 3
screen_start_x = 137
screen_start_y = 658

flname1 = 'keys-of-moon-warm-memories.mp3'
flname2 = '02 - Sam Houghton and Joe Collinson - The Rhythm King.mp3'

data, samplerate = sf.read(
    "C:\\Users\\NK22\\Downloads\\" + flname1)


def anal_mic_sig(nperseg):
    freq, time, Zxx = sn.stft(
        data[:, 0], samplerate, nperseg=nperseg/25)
    return time, Zxx


def GUI():

    # 각 주파수별 크기 계산 부분
    time, Zxx = anal_mic_sig(samplerate)
    mag = np.abs(Zxx[50:300, :])

    # 주파수 별 최댓값을 저장할 배열 생성
    max_val = np.zeros(250, np.uint8)

    # 화면에 표시할 이퀄 설정

    # 시간에 따른 작업(0.5초)
    for t in range(0, len(time), 1):

        # 0.5초당 500개의 프레임 생성
        for frame in range(0, 1, 1):

            # 화면 리셋(검은색 화면)
            img = np.zeros((height, width, bpp), np.uint8)

            # 단일 프레임 생성(50Hz부터 300Hz까지 순차적으로 생성)
            for x in range(0, 250, 1):

                max_val[x] = 200 * ((mag[x, t] - 1) ** (4095) + 1)
                y = int(max_val[x])

                start_x = screen_start_x + x * int_x
                cv.rectangle(img, (start_x, 3 * (220 - y)),
                             (start_x + rect_w, 660), (0, 255 * (1 - (y//153)), 255 * (y//153)), thickness)
                '''
                cv.rectangle(img, (start_x, 60),
                             (start_x + rect_w, 3 * (220 - y)), (0, 0, 0), thickness)
                '''

            #max_val = 0.9*max_val
            # 이퀄 화면 출력
            cv.imshow('Sample Title', img)
            cv.waitKey(20)


GUI()
