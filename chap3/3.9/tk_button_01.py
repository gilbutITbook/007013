# coding: utf-8

# Tkinter 라이브러리 임포트
import tkinter as tk # Python3
#import Tkinter as tk # Python2

# Tk 객체 인스턴스 생성
root = tk.Tk()

# 버튼을 눌렀을 때 처리
def func():
    # 메시지를 파이썬 셸에 출력
    print ('Pushed')

# 버튼 생성
button = tk.Button(root, text = 'Push!', command = func)

# 버튼 배치
button.pack()

# root 표시
root.mainloop()
