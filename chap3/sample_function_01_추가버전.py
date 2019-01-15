import random
print('This contents makeface function')    # 추가한 부분
a = 5    # 추가한 부분

def makeFace():
    face = ['(x_x)', '(O_O)', '(-_-#)', '(>_<)', '(^o^)', '=^Y^=', '(`_^)',
    'd-_-b', 'p(^o^)q']
    numFace = len(face)
    index = random.randint(0, numFace - 1)
    return face[index]
    
print(makeFace()) 
