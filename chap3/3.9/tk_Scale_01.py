# coding: utf-8

# Tkinter 라이브러리 임포트
import tkinter as tk # Python3
#import Tkinter as tk # Python2

# Tk 객체 인스턴스 생성
root = tk.Tk()

# 슬라이드 바의 값을 저장할 Variable 객체 생성(정수형)
val = tk.IntVar()
# 0으로 설정
val.set(0)

# 손잡이를 움직였을 때 처리
def func(scl):
    # Label 표시를 변경
    label.config(text = 'Value = %d' % int(scl))

# 슬라이드 바의 값을 표시하는 라벨 생성
label = tk.Label(root, text = 'Value = %d' % val.get())

# 라벨 배치
label.pack()

# 슬라이드 바 생성
# Scale 라벨 표시. 수평으로 숫자 범위는 0에서 100까지
s = tk.Scale(root, label = 'Scale', orient = 'h', from_ = 0, to = 100, showvalue = False, variable = val, command = func)

# 슬라이드 바 배치
s.pack()

# root 표시
root.mainloop()
