
fibonacci_list = [1,1]
n = 1

while fibonacci_list[n-1]+fibonacci_list[n] < 100:
        fibonacci_list.append(fibonacci_list[n-1]+fibonacci_list[n])
        n = n+1

print(fibonacci_list)

