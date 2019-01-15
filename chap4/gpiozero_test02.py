# coding: utf-8

# GPIO Zero 라이브러리 임포트
import gpiozero

# time 라이브러리 임포트
import time

# 11번 핀을 출력 핀으로 LED 접속
red_led = gpiozero.LED(17)

# LED 점멸
red_led.blink()

# 예외 처리
try:

    # 무한 반복
    while 1:
        time.sleep(1)

# 키보드 예외 검출
except KeyboardInterrupt:

    # 아무것도 하지 않음
    pass

# GPIO 개방
red_led.close()
