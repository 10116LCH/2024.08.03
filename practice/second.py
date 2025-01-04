a = 158
print(a)
a = "700"
print(a)
a = 3.09
print(a)

b = input("값을 넣으시오 : ")
print(b + "(이)가 입력되었습니다.")

b = "158"
c = int(b) + 151
print(c)

d = c
print("c의 값은", c)
print("d의 값은", d)
c = 610
print("c의 값은", c)
print("d의 값은", d)

e = [158, 1008, 309, 610]
f = e
print(e)
print(f)
e.append(300)
print(e)
print(f)

e = e + [100]
print(e)
print(f)
e = [116, 111]
print(e)
print(f)
e.append(724)
print(e)
print(f)