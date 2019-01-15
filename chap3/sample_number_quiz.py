import random

answer = random.randint(1, 10)
message = 'guess a number (1 ~ 10)'

while True:
    number = int(input(message + '>'))
    
    if number < answer:
        message = 'guess a bigger number b(-_- )'
    elif number > answer:
        message = 'guess a smaller number q(-_- )'
    else:
        print('Bingo! (b>_^)b')
        break

print('(>^_^)>end of program<(^_^<)')
