#사용자에게 수학점수를 입력받아 상/중/하반으로 분류하기
# 상 - 90이상
# 중 - 70이상
# 하 - 나머지

size = int(input("수학 점수 입력"))
print(size)

if size >= 90 and size <= 100:
    print("상")

elif size >= 70 and size < 90:
    print("중")

elif size >= 0 and size < 70:
    print("하")

else:
    print("잘못된 점수입니다.")


