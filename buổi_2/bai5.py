def check(n):
    a = 0
    m = n
    while n > 0:
        a += (n % 10) ** 3
        n //= 10
    return a == m
n = int(input('nhap n : '))
for i in range(1, n + 1) :
    if check(i) :
        print(i)