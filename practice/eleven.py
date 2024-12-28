# if 수업 점수에 태도점수 포함 (수행평가)

attitudes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

for attitude in attitudes:
    print(attitude)
    attitude = attitude + 1

print("참조하는 attitudes에 더한것--attitudes: call by value")
print(attitudes)

for i in range(len(attitudes)):
    attitudes[i] = attitudes[i] + 1

print("attitudes에 더한값을 넣어준것--attitudes[i]: call by reference")
print(attitudes)

# 10명이 10문제 쪽지시험
#객관식 10점
#0~9학생,문제

#student = [[1,2,3,4,5,1,2,3,4,5],[2,2,2,2,2,2,2,2,2,2] 등

#answer = []

student = []
for i in range(10): #i번째 학생
    student = []



print("----------------------------------")


for attitude in attitudes:
    print(attitude)
    attitude = attitude + 1

print("attitude에 값을 더한것")
print(attitudes)

for i in range(len(attitudes)):
    attitudes[i] = attitudes[i] + 1

print("attitudes에 더한 값을 넣어준 것")
print(attitudes)




print("--------------------------")\



