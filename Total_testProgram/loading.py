import time
import sys
import soundfile as sf
import numpy as np
from scipy import signal as sn
import os


s_data, samplerate = sf.read(
    "C:\\Users\\NK22\\Downloads\\keys-of-moon-warm-memories.mp3")

print(type(s_data))

frequency, point, Zxx = sn.stft(
    s_data[:, 0], samplerate, nperseg=44100)


def eq():
    arr = []
    test = ''

    #
    for i in range(0, len(point), 1):

        # 0.5초 간격의 주파수별 크기를 절댓값으로 가져옴
        abs_arr = np.abs(Zxx[600:800, i])*10000

        # 단순 시각화 하기 위해서 데이터를 일정 크기로 줄임
        for cnt in range(0, len(abs_arr), 1):
            arr.append(int(abs_arr[cnt])//10)

        height = 20

        # 데이터를 기반으로 시각화
        for scale in range(0, height, 1):

            # 10 단위로 주파수 크기를 *로 나타냄
            for icon in range(0, len(arr), 1):

                if arr[icon] < (height-scale):
                    test += ' '
                else:
                    test += '*'

            # 마지막 행은 줄바꿈 없음
            if scale != height - 1:
                test += '\n'

        os.system('cls')
        sys.stdout.write('\r' + test)

        # 데이터 표시 후 값 초기화
        arr = []
        test = ''

        time.sleep(0.5)


eq()
