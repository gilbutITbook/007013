# coding: utf-8

# Tkinter 라이브러리 임포트
import tkinter as tk # Python3
#import Tkinter as tk # Python2

# Tk 객체 인스턴스 생성
root = tk.Tk()

# Enter 키(리턴 키)를 눌렀을 때 동작
def func(ev):
    # Label 표시를 변경
    label.config(text = e.get())

# 라벨 생성
label = tk.Label(root, text = 'Input Text')
# 라벨 배치
label.pack()

# 텍스트 박스를 생성
e = tk.Entry(root)

# 텍스트 박스 배치
e.pack()

# 리턴 키를 눌렀을 때의 이벤트 추가
e.bind('<Return>', func)

# root 표시
root.mainloop()
