# coding: utf-8

# WiringPi 라이브러리 임포트
import wiringpi

# 사용할 핀번호
PIN_LED = 17

# GPIO 초기화
wiringpi.wiringPiSetupGpio()
# LED를 연결한 핀을 출력으로 설정
wiringpi.pinMode(PIN_LED,wiringpi.OUTPUT)

# 예외 처리
try:

    # 무한 반복
    while True:
        # LED 켜기
        wiringpi.digitalWrite(PIN_LED, wiringpi.HIGH)
        # 1초 대기
        wiringpi.delay(1000)
        # LED 끄기
        wiringpi.digitalWrite(PIN_LED, wiringpi.LOW)
        # 1초 대기
        wiringpi.delay(1000)

# 키보드 예외 검출
except KeyboardInterrupt:

    # 아무 것도 하지 않음
    pass

# 핀을 입력으로 바꾸고 LED 끄기
wiringpi.pinMode(PIN_LED, wiringpi.INPUT)
wiringpi.pullUpDnControl(PIN_LED, wiringpi.PUD_DOWN)
