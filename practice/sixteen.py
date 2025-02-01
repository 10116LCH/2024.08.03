d = {"key":"value", 2.3: "value", 5:1, 5:"111", (1,2,3):3}
print(d)

a = dict()
print(a)

print(d.keys())
print(d.values())
print("-----------------------------")

inventory = {"물":"1000", "콜라":"1200", "사이다":"1100", "커피":"500"}
#사용자 모드
#음료는 물, 콜라, 사이다, 커피
#가격은 1000, 1200, 1100, 500
#질문 대답
#해당음료가 있으면 o
#해당음료가 없으면 x
if not inventory :
    print("X")
elif inventory :
    answer = input("선택")
    if inventory.key == answer:
        print("O")
    else:
        print("X")

#관리자 모드
#원하는 음료와 가격 작성
#만약 기존에 있다면 가격 변동
#없다면 새로 추가
c = input("입력")
if c in inventory:
    print()
elif not c in inventory:
    print()