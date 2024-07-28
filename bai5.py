n = int(input('nhap n : '))
a = [int(input()) for _ in range(n)]
result = [x for x in a if x % 2 != 0]
result.sort()
print(len(result))
print(result) 