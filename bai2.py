a = list(map(int, input("Nhập các phần tử của list a, cách nhau bởi dấu cách: ").split()))
k = len(a)
n = int(input("Nhập số dòng n: "))
m = int(input("Nhập số cột m: "))


if len(a) < n * m:
         "NO"
    
result = []
for i in range(n):
        row = a[i * m:(i + 1) * m]
        result.append(row)
    

if result == "NO":
    print("NO")
else:
    for row in result:
        print(row)