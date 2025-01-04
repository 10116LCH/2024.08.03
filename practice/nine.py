#---------- 기본 틀 -------------------

#1. 정답을 랜덤으로 생성
# -> 각 자리수의 숫자가 겹치면 안됨.
# -> 겹쳤을때 어떻게 할것인가 or 안겹치게 어떻게 생성을 할것인가
# -> 자릿수에 대한 포인트는 : list(*), 숫자

#import random
#value = random.randrange(1,10) # 리스트를 쓰는 경우
#value = random.randrange(1,1000) # 숫자를 쓰는 경우

#2. 사용자의 입력을 받아야함.
#-> 숫자가 있는지 -> 그 숫자가 그 자리인지
#-> 결과에 따른 출력

#3. 사용자가 종료 입력을 하면 종료
#-> 사용자가 정답을 맞춘 이후에 다음문제 출제

#---------- 응용 -------------------
#4. turn 수 제한
#-> 10번으로 제한, 10번안에 못맞추면 fail

import random

result = 0

#result % 10
## (result // 10) % 10
### result // 100

while result // 100 == (result // 10) % 10 or result // 100 == result % 10 or (result // 10) % 10 == result % 10
    result = random.randrange( start 1, stop 1000) #숫자 사용 경우\

