# coding: utf-8
# 파일 유무를 조사하기 위해 모듈을 임포트
import os.path

# 경로와 파일명을 filename에 저장
filename = '/home/pi/python_output/myInterview.csv'

# 표 헤더
header = 'name,age,food'

# 키보드에서 입력받은 문자열을 저장할 변수
personalData = ''

# 파일이 없으면 새로 작성해서 헤더 쓰기
if not os.path.exists(filename):
    with open(filename, mode = 'w') as f:
        f.write(header + '\n')
    
# 키보드로 입력받은 문자열 추가하기
personalData += input('input your name(>^_^)>') + ','
personalData += input('input your age(>^_^)>') + ','
personalData += input('input your favorite food(*^o^)>') + '\n'

# 파일을 append 모드로 열어서 문자열 써넣기
with open(filename, mode = 'a') as f:
    f.write(personalData)
    
# 파일 내용 표기하기
print('\n <The contents of file are ...> \n')
with open (filename, mode = 'r') as f:
    for line in f:
        print(line)
