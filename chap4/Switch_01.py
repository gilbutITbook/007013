# coding: utf-8

# GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

# 핀 번호 할당 방법을 커넥터 핀 번호로 설정
GPIO.setmode(GPIO.BOARD)

# 사용하는 핀 번호를 할당
SW = 7
LED = 11

# 11번 핀을 출력 핀으로 설정, 초기 출력은 로우 레벨
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

# 7번 핀을 입력 핀으로 설정
GPIO.setup(SW, GPIO.IN)

# 예외 처리
try:
    # 무한 반복
    while 1:
        # 스위치 상태를 변수 key_in에 할당
        key_in = GPIO.input(SW)
        # 변수 key_in 상태 판별
        if key_in==0:
            # 하이 레벨 출력
            GPIO.output(LED, GPIO.HIGH)
        else:
            # 로우 레벨 출력
            GPIO.output(LED, GPIO.LOW)

# 키보드 예외 검출
except KeyboardInterrupt:
    # 아무것도 하지 않음
    pass

# GPIO 개방
GPIO.cleanup()
