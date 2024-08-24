a = [100, 96, 87, 100, 1, 12, 123, 1234, 12345, 123456]

print(a[0])
print(a[1])

print(a)
print(a[0:5]) #a[n:m] a의 n번째부터 m-1번째까지
print(a[4:5])
print(a[3:])
print(a[:4])

b = [[1, 2, 3, 4, 5], [-1, -2, -3, -4, -5], [1/1, 1/2, 1/3, 1/4, 1/5]]

c = [[[100, 101, 102], 200, 300, 400, [500, 501], 600 ], 1000, 2000]

print(b[0][4])
print(b[2])
print(b[2][1:])
print(c[0][4][1])

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ경계선ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(" ")
d = [11, 12, 13, 14, 15]
e = d

d[1] = 10

print(d)
print(e)

f = a + d
print(f)

g = a + b
print(g)

h = d * 3
print(h)

print(len(a))
print(len(b))
print(len(b[0]))