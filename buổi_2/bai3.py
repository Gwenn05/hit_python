# a
n = int(input('nhap n : '))
sum = 0
for i in range(1, n + 1) :
    if i % 2 == 0 :
        sum -= i
    else :
        sum += i
print(sum)
# b
n = int(input('nhap n : '))
sum = 0
for i in range(1, n + 1) :
    sum += 1 / i
print(round(sum, 3))
# c
a = int(input('nhap a : '))
b = int(input('nhap b : '))
c = int(input('nhap c : '))

if a == 0 : 
        if b == 0 : 
            if c == 0 : 
                print('phuong trinh co vo so nghiem')
            else : 
                print('phuong trinh vo nghiem')
        else : 
            x = -c / b
            print('phuong trinh co 1 nghiem duy nhat : ', x)
else : 
        delta = b * b - 4 * a * c
        if delta < 0 : 
            print('phuong trinh vo nghiem')
        elif delta == 0 : 
            x = -b / (2 * a)
            print('phuong trinh co nghiem kep : ', x)
        else : 
            x1 = (-b + delta ** 0.5) / (2 * a)
            x2 = (-b - delta ** 0.5) / (2 * a)
            print('phuong trinh co 2 nghiem phan biet : ', round(x1, 4), 'va', round(x2, 4))