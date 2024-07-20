def timuoc(n) : 
    sum = 0
    for i in range(1, n // 2 + 1) :
        if (n % i == 0) : 
            sum += i
    return sum == n
n = int(input('nhap n : '))
if (n < 6) :
    print('khong co so hoan hao trong doan tu 1 - ', n)
for i in range(1, n + 1) :
    if timuoc(i) : 
        print(i, end=' ')