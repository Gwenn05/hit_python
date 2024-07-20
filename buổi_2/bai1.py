#a 5
n = int(input('nhap n : '))
sum = 0
while n % 10 != 0:
    sum += n % 10
    n //= 10
print(sum)
# b)
n = int(input('nhap n : '))
sum = 0
for i in range(1, (int)(n / 2) + 1):
    if n % i == 0 :
     sum += i
     print(i, ' ', ' ')
print(sum)
# c)
print('nhap a, b, c : ')
a = int(input())
b = int(input())
c = int(input())
if a < b + c and b < a + c and c < a + b :
    if a == b == c : 
        print('tam giac deu')
    elif a == b != c :
        print('tam giac can')
    elif a*a > b*b + c*c and b*b > a*a + c*c and c*c > a*a + b*b :
        print('tam giac tu')
    elif a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b :
        print('tam giac vuong')
    else :
        print('tam giac nhon')
else :
    print('khong the tao thanh tam giac')