# coding: utf-8

# GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

# Tkinter 라이브러리 임포트
import tkinter as tk # Python3
#import Tkinter as tk # Python2

# 핀 번호 할당 방법은 커넥터 핀 번호로 설정
GPIO.setmode(GPIO.BOARD)

# 사용할 핀 번호 할당
LED = 11

# 11번 핀을 출력 핀으로 설정, 초기 출력은 로우 레벨
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

# LED를 켜고 끄는 함수를 정의
def func():

    # 11번 핀에서 나오는 입력 값을 반전해서 출력
    GPIO.output(LED, not GPIO.input(LED))

# Tk 객체 인스턴스 root 작성
root = tk.Tk()

# root에 표시할 라벨 정의
label = tk.Label(root, text='press button')

# 라벨 배치
label.pack()

# root에 표시할 버튼 정의
button = tk.Button(root, text='LED', command=func)

# 버튼 배치
button.pack()

# root 표시
root.mainloop()

# GPIO 개방
GPIO.cleanup()
