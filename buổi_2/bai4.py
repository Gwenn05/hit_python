n = int(input('nhap n > 0: '))
f0 = 0
f1 = 1
if n >= 2 :
    print (f0, f1, end=' ')
elif n == 1 : 
    print(f0) 

for i in range(n - 2) : 
        f2 = f0 + f1
        f0 = f1
        f1 = f2
        print(f2, end=' ')