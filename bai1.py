
n = int(input("nhap so nguyen n = "))
l = [x for x in range(0, n+1)]
print(l)
x = int(input('nhap x : '))
print('xuat hien {} lan trong list'.format(l.count(x)))
l[2:7] = [8, 5, 4, 0, 1, 3]
print('list sau khi thay doi : ', l)
a = l;
a.sort()
print('min element : ', a[0])
print('max element : ', a[-1])
del a
y = int(input('nhap y : '))
l.insert(y, 0)
print('list sau khi chen : ', l)
if sorted(l) == l:
    print('TANG')
elif sorted(l, reverse=True) == l:
    print('GIAM')
else :
    print('NO')
new_l = []
for i in range(1, len(l), 1):
    new_l.append(sum(l[:i - 1]))
print(new_l)
new_l2 = [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
new_l2.sort()
print('list sau khi sap xep : ', new_l2)
new_l2 = sorted(new_l2, key=abs)
print('list sau khi sap xep theo gia tri tuyet doi : ', new_l2)