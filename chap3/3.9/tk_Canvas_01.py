# coding: utf-8

# Tkinter 라이브러리 임포트
import tkinter as tk # Python3
#import Tkinter as tk # Python2

# Tk 객체 인스턴스 생성
root = tk.Tk()

# Canvas 객체 인스턴스 생성
# 너비는 500, 높이는 500
c = tk.Canvas(root, width = 500, height = 500)
# Canvas 배치
c.pack()

# 선을 그림
# 좌표(0, 0)에서 (50, 50), 색은 검정
c.create_line(0, 0, 50, 50)

# 사각형을 그림
# 좌표(100, 100)에서 (150, 150), 색은 빨강
c.create_rectangle(100, 100, 150, 150, fill = 'red')

# 원을 그림
# 좌표(100, 200)에서 (150, 250), 색은 파랑
c.create_oval(100, 200, 150, 250, fill = 'blue')

# 다각형을 그림
# 8개 좌표를 연결한 팔각형, 색은 녹색
c.create_polygon(250, 200, 350, 200, 400, 250, 400, 350, 350, 400, 250, 400,\
                200, 350, 200, 250, fill = 'green')

# root 표시
root.mainloop()
