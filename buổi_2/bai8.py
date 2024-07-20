n = int(input('nhap n : '))
a = [[] for _ in range(n)]
#print(a)
for i in range(n):
    a[i] = [1] * (i + 1)
    # a[i][0] = 1
    # a[i][i] = 1
for i in range(2, n):
    for j in range(1, i):
        a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
        
for row in a:
    print(*row)