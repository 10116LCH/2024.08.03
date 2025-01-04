(x,y) = (0,0)
answer = int(input("1, 2, 3, or 4: "))

while 0 <= x <= 100 and 0 <= y <= 100:


 if answer == 1:
    y = y + 1
    print(x,y)

 elif answer == 2:
    y = y - 1
    print(x,y)

 elif answer == 3:
    x = x + 1
    print(x,y)

 elif answer == 4:
    x = x - 1
    print(x,y)

else:
    print("잘못된 입력입니다.")