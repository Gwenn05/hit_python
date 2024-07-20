def tongcuauoc(n) :
    sum = 0
    for i in range(1, n) :
        if n % i == 0 :
            sum += i
    return sum
n = int(input('nhap n : '))
for i in range(1, (n + 1)) :
    sum = tongcuauoc(i)
    if tongcuauoc(sum) == i and sum < i :
        print(i, ' ', sum)  