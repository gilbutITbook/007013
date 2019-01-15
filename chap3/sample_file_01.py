# coding: utf-8
# 경로와 파일명을 filename에 지정
filename = '/home/pi/python_output/myfile.txt'

# 파일을 읽기(write) 모드로 열어서 f에 할당
# 문자열 Python 써넣기
with open(filename, mode = 'w') as f:
    f.write('Python')
    
# 파일을 read 모드로 열어서 f에 할당
# 한 줄을 읽어서 출력
with open(filename, mode = 'r') as f:
    print(f.readline())